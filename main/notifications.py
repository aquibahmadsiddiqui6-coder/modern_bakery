import json
import logging
import os
import re
from urllib.request import Request, urlopen


logger = logging.getLogger(__name__)


def _api_key():
    return os.environ.get("BREVO_API_KEY", "").strip()


def _post(path, payload):
    request = Request(
        f"https://api.brevo.com/v3/{path}",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "accept": "application/json",
            "api-key": _api_key(),
            "content-type": "application/json",
        },
        method="POST",
    )
    with urlopen(request, timeout=8) as response:
        return response.status


def _phone(value):
    digits = re.sub(r"\D", "", value or "")
    if len(digits) == 10:
        return f"91{digits}"
    return digits


def _image_url(product):
    base_url = os.environ.get("PUBLIC_SITE_URL", "https://modernbakery-mu.vercel.app").rstrip("/")
    try:
        if product.image:
            return f"{base_url}{product.image.url}"
    except ValueError:
        pass
    photo = product.images.first()
    if photo:
        return f"{base_url}{photo.image.url}"
    return ""


def send_order_notifications(order_id, customer_name, customer_phone, customer_email, rows, total):
    """Send best-effort order notifications without interrupting checkout."""
    if not _api_key():
        logger.info("Order %s notifications skipped: BREVO_API_KEY is not configured", order_id)
        return

    owner_email = os.environ.get("ORDER_NOTIFICATION_EMAIL", "aquibahmadsiddiqui6@gmail.com").strip()
    owner_phone = _phone(os.environ.get("ORDER_NOTIFICATION_PHONE", "8127442301"))
    sender_email = os.environ.get("BREVO_SENDER_EMAIL", "").strip()
    sender_name = os.environ.get("BREVO_SENDER_NAME", "Modern Tea & Bakery").strip()
    lines = "".join(
        f"<li><strong>{row['product'].name}</strong> × {row['quantity']} — ₹{row['line_total']}</li>"
        for row in rows
    )
    image_blocks = "".join(
        f'<p><img src="{image_url}" alt="{row["product"].name}" style="max-width:240px;max-height:180px;object-fit:cover;"></p>'
        for row in rows
        if (image_url := _image_url(row["product"]))
    )
    image_attachments = [
        {"url": image_url, "name": f"order-{order_id}-{row['product'].id}.jpg"}
        for row in rows
        if (image_url := _image_url(row["product"]))
    ]
    owner_html = f"""
        <h2>New Modern Tea &amp; Bakery order #{order_id}</h2>
        <p><strong>Customer:</strong> {customer_name}<br><strong>Phone:</strong> {customer_phone}</p>
        <ul>{lines}</ul>
        <p><strong>Total: ₹{total}</strong></p>
        {image_blocks}
    """
    customer_html = f"""
        <h2>Order received · Modern Tea &amp; Bakery</h2>
        <p>Hello {customer_name}, we received your order <strong>#{order_id}</strong>.</p>
        <ul>{lines}</ul>
        <p><strong>Total: ₹{total}</strong></p>
        <p>We will contact you shortly to confirm the order and delivery details.</p>
    """
    if sender_email:
        recipients = []
        if owner_email:
            recipients.append({"email": owner_email, "name": "Modern Tea & Bakery"})
        if customer_email:
            recipients.append({"email": customer_email, "name": customer_name})
        for recipient in recipients:
            html = owner_html if recipient["email"] == owner_email else customer_html
            try:
                email_payload = {
                    "sender": {"email": sender_email, "name": sender_name},
                    "to": [recipient],
                    "subject": f"Order #{order_id} received",
                    "htmlContent": html,
                }
                if recipient["email"] == owner_email and image_attachments:
                    email_payload["attachment"] = image_attachments
                _post("smtp/email", email_payload)
            except Exception:
                logger.exception("Email notification failed for order %s", order_id)

    sms_text = f"Modern Bakery order #{order_id} received. Total ₹{total}. We will confirm shortly."
    sms_recipients = {number for number in (owner_phone, _phone(customer_phone)) if number}
    sms_sender = os.environ.get("BREVO_SMS_SENDER", "MODERN").strip()
    if sms_sender:
        for recipient in sms_recipients:
            try:
                _post("transactionalSMS/send", {
                    "sender": sms_sender,
                    "recipient": recipient,
                    "content": sms_text,
                    "type": "transactional",
                })
            except Exception:
                logger.exception("SMS notification failed for order %s", order_id)
