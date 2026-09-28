const lightbox = document.querySelector("[data-pastry-lightbox]");

if (lightbox) {
    const image = lightbox.querySelector("[data-lightbox-image]");
    const caption = lightbox.querySelector("[data-lightbox-caption]");
    const items = [];
    let current = 0;

    const render = (index) => {
        if (!items.length) return;
        current = (index + items.length) % items.length;
        image.src = items[current].src;
        image.alt = items[current].alt;
        caption.textContent = items[current].alt;
    };

    const open = (images, index) => {
        items.length = 0;
        images.forEach((item) => items.push(item));
        render(index);
        lightbox.hidden = false;
        lightbox.setAttribute("aria-hidden", "false");
        document.body.classList.add("lightbox-open");
    };

    const close = () => {
        lightbox.hidden = true;
        lightbox.setAttribute("aria-hidden", "true");
        document.body.classList.remove("lightbox-open");
    };

    lightbox.querySelectorAll("[data-lightbox-close]").forEach((button) => button.addEventListener("click", close));
    lightbox.querySelector("[data-lightbox-prev]")?.addEventListener("click", () => render(current - 1));
    lightbox.querySelector("[data-lightbox-next]")?.addEventListener("click", () => render(current + 1));

    document.querySelectorAll("[data-product-image]").forEach((productImage) => {
        productImage.addEventListener("click", () => open([{ src: productImage.src, alt: productImage.alt }], 0));
    });

    document.querySelectorAll("[data-pastry-carousel]").forEach((carousel) => {
        const carouselImages = [...carousel.querySelectorAll("[data-carousel-slide] img")].map((carouselImage) => ({
            src: carouselImage.src,
            alt: carouselImage.alt,
        }));
        carousel.querySelectorAll("[data-carousel-slide] img").forEach((carouselImage, index) => {
            carouselImage.addEventListener("click", () => open(carouselImages, index));
        });
    });

    document.addEventListener("keydown", (event) => {
        if (lightbox.hidden) return;
        if (event.key === "Escape") close();
        if (event.key === "ArrowLeft") render(current - 1);
        if (event.key === "ArrowRight") render(current + 1);
    });
}
