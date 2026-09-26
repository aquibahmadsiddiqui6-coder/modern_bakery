import Lenis from "https://cdn.jsdelivr.net/npm/lenis@1.3.26/+esm";

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const knowMoreTrigger = document.querySelector(".know-more-trigger");
const aboutMore = document.querySelector("#about-more");
const shopStatus = document.querySelector("[data-shop-status]");
const statusLabel = document.querySelector("[data-status-label]");
const menuFilters = document.querySelectorAll("[data-menu-filter]");
const menuCards = document.querySelectorAll("[data-menu-category]");
const menuEmpty = document.querySelector("[data-menu-empty]");
const menuCount = document.querySelector("[data-menu-count]");

knowMoreTrigger?.addEventListener("click", () => {
    if (!aboutMore) return;
    const isOpen = knowMoreTrigger.getAttribute("aria-expanded") === "true";
    knowMoreTrigger.setAttribute("aria-expanded", String(!isOpen));
    aboutMore.hidden = isOpen;
    aboutMore.classList.toggle("is-open", !isOpen);
    knowMoreTrigger.textContent = isOpen ? "Know More" : "Show Less";
});

const updateShopStatus = () => {
    if (!shopStatus || !statusLabel) return;

    const timeParts = new Intl.DateTimeFormat("en-US", {
        timeZone: "Asia/Kolkata",
        hour: "2-digit",
        minute: "2-digit",
        hour12: false,
    }).formatToParts(new Date());
    const hours = Number(timeParts.find((part) => part.type === "hour")?.value || 0);
    const minutes = Number(timeParts.find((part) => part.type === "minute")?.value || 0);
    const currentMinutes = hours * 60 + minutes;
    const isOpen = currentMinutes >= 630 && currentMinutes < 1320;

    shopStatus.classList.toggle("is-open", isOpen);
    shopStatus.classList.toggle("is-closed", !isOpen);
    statusLabel.textContent = isOpen ? "Open now" : "Closed now";
};

updateShopStatus();
window.setInterval(updateShopStatus, 60000);

const filterMenu = (category) => {
    let visibleCount = 0;

    menuCards.forEach((card) => {
        const matches = category === "all" || card.dataset.menuCategory === category;
        card.classList.toggle("is-filtered-out", !matches);
        if (matches) visibleCount += 1;
    });

    menuFilters.forEach((filter) => {
        const isActive = filter.dataset.menuFilter === category;
        filter.classList.toggle("is-active", isActive);
        filter.setAttribute("aria-selected", String(isActive));
    });

    if (menuCount) menuCount.textContent = String(visibleCount);
    if (menuEmpty) menuEmpty.hidden = visibleCount > 0;
};

menuFilters.forEach((filter) => {
    filter.addEventListener("click", () => filterMenu(filter.dataset.menuFilter));
});

filterMenu("all");

if (!reduceMotion) {
    document.body.classList.add("js-motion");
    document.documentElement.classList.add("lenis");

    const hero = document.querySelector(".hero");
    const intro = document.querySelector(".intro");
    const navbar = document.querySelector(".navbar");

    const lenis = new Lenis({
        autoRaf: false,
        lerp: 0.085,
        smoothWheel: true,
        syncTouch: false,
        anchors: true,
    });

    const revealItems = document.querySelectorAll("[data-reveal]");
    const revealObserver = new IntersectionObserver(
        (entries, observer) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("is-visible");
                    if (!entry.target.hasAttribute("data-reveal-loop")) {
                        observer.unobserve(entry.target);
                    }
                } else if (entry.target.hasAttribute("data-reveal-loop")) {
                    entry.target.classList.remove("is-visible");
                }
            });
        },
        { rootMargin: "18% 0px 18% 0px", threshold: 0.04 }
    );

    revealItems.forEach((item, index) => {
        item.style.setProperty("--reveal-delay", `${Math.min(index * 45, 360)}ms`);
        revealObserver.observe(item);
    });

    const parallaxImage = document.querySelector("[data-parallax='hero-image']");
    lenis.on("scroll", ({ scroll }) => {
        const heroHeight = hero?.offsetHeight || window.innerHeight;
        const heroProgress = Math.min(Math.max(scroll / (heroHeight * 0.9), 0), 1);
        const introProgress = Math.min(Math.max((scroll - heroHeight * 0.5) / (window.innerHeight * 0.8), 0), 1);

        hero?.style.setProperty("--hero-opacity", `${1 - heroProgress * 0.72}`);
        hero?.style.setProperty("--hero-scale", `${1 - heroProgress * 0.045}`);
        intro?.style.setProperty("--intro-shift", `${(1 - introProgress) * 24}px`);
        navbar?.classList.toggle("is-scrolled", scroll > 32);

        if (!parallaxImage) return;
        const progress = Math.min(scroll / Math.max(window.innerHeight, 1), 1);
        parallaxImage.style.setProperty("--parallax-y", `${progress * 7}%`);

        document.querySelectorAll("[data-depth]").forEach((item) => {
            const bounds = item.getBoundingClientRect();
            const distance = (bounds.top + bounds.height / 2 - window.innerHeight / 2) / window.innerHeight;
            item.style.setProperty("--depth-y", `${Math.max(-10, Math.min(10, distance * -10))}px`);
        });
    });

    let frameId;
    const raf = (time) => {
        lenis.raf(time);
        frameId = requestAnimationFrame(raf);
    };

    frameId = requestAnimationFrame(raf);

    window.addEventListener("pagehide", () => {
        cancelAnimationFrame(frameId);
        lenis.destroy();
    }, { once: true });
}
