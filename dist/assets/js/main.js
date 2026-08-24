/* SHARK — shared front-end behaviour. No frameworks, no dependencies. */
(function(){
  "use strict";

  document.addEventListener("DOMContentLoaded", function(){

    /* ---------- Footer year ---------- */
    document.querySelectorAll("[data-year]").forEach(function(el){
      el.textContent = new Date().getFullYear();
    });

    /* ---------- Homepage hero background slider ---------- */
    var heroSlider = document.getElementById("heroSlider");
    if(heroSlider){
      var slides = Array.prototype.slice.call(heroSlider.querySelectorAll(".hero-slide"));
      var dots = Array.prototype.slice.call(document.querySelectorAll(".hero-dots .dot"));
      var reducedMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      /* The first slide is already marked .active in the HTML, so the page
         opens directly on it with no JS needed — no loading/intro delay.
         With reduced motion, just leave it there and skip auto-advance. */
      if(slides.length > 1 && !reducedMotion){
        var current = 0;
        var ADVANCE_MS = 4600;
        setInterval(function(){
          var next = (current + 1) % slides.length;
          slides[current].classList.remove("active");
          if(dots[current]) dots[current].classList.remove("active");
          slides[next].classList.add("active");
          if(dots[next]) dots[next].classList.add("active");
          current = next;
        }, ADVANCE_MS);
      }
    }

    /* ---------- Header compact-on-scroll ---------- */
    var header = document.querySelector(".site-header");
    if(header){
      var lastY = window.scrollY;
      var onScroll = function(){
        var y = window.scrollY;
        header.classList.toggle("compact", y > 40);
        lastY = y;
      };
      window.addEventListener("scroll", onScroll, { passive:true });
      onScroll();
    }

    /* ---------- Mobile drawer ---------- */
    var burger = document.querySelector(".burger");
    var drawer = document.querySelector(".mobile-drawer");
    var drawerClose = document.querySelector(".drawer-close");
    function openDrawer(){ drawer.classList.add("open"); document.body.classList.add("drawer-open"); }
    function closeDrawer(){ drawer.classList.remove("open"); document.body.classList.remove("drawer-open"); }
    if(burger && drawer){
      burger.addEventListener("click", openDrawer);
      if(drawerClose) drawerClose.addEventListener("click", closeDrawer);
      drawer.querySelectorAll("a").forEach(function(a){ a.addEventListener("click", closeDrawer); });
    }

    /* ---------- Scroll reveal ---------- */
    var revealEls = document.querySelectorAll(".reveal");
    if("IntersectionObserver" in window && revealEls.length){
      var io = new IntersectionObserver(function(entries){
        entries.forEach(function(entry){
          if(entry.isIntersecting){
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
      revealEls.forEach(function(el){ io.observe(el); });
    } else {
      revealEls.forEach(function(el){ el.classList.add("in"); });
    }

    /* ---------- FAQ accordion ---------- */
    document.querySelectorAll(".faq-item").forEach(function(item){
      var q = item.querySelector(".faq-q");
      var a = item.querySelector(".faq-a");
      if(!q || !a) return;
      q.addEventListener("click", function(){
        var isOpen = item.classList.contains("open");
        item.closest(".faq-list").querySelectorAll(".faq-item.open").forEach(function(openItem){
          if(openItem !== item){
            openItem.classList.remove("open");
            openItem.querySelector(".faq-a").style.maxHeight = null;
          }
        });
        if(isOpen){
          item.classList.remove("open");
          a.style.maxHeight = null;
        } else {
          item.classList.add("open");
          a.style.maxHeight = a.scrollHeight + "px";
        }
      });
    });

    /* ---------- Product filter + search (Products page) ---------- */
    var filterBar = document.querySelector("[data-product-filter]");
    if(filterBar){
      var chips = filterBar.querySelectorAll(".chip");
      var searchInput = filterBar.querySelector("[data-product-search]");
      var cards = document.querySelectorAll("[data-product-card]");
      var emptyState = document.querySelector(".results-empty");
      var activeCat = "all";

      function applyFilter(){
        var term = (searchInput && searchInput.value || "").trim().toLowerCase();
        var visibleCount = 0;
        cards.forEach(function(card){
          var cat = card.getAttribute("data-cat");
          var name = (card.getAttribute("data-name") || "").toLowerCase();
          var matchesCat = activeCat === "all" || cat === activeCat;
          var matchesTerm = !term || name.indexOf(term) !== -1;
          var show = matchesCat && matchesTerm;
          card.style.display = show ? "" : "none";
          if(show) visibleCount++;
        });
        if(emptyState) emptyState.style.display = visibleCount === 0 ? "block" : "none";
      }

      chips.forEach(function(chip){
        chip.addEventListener("click", function(){
          chips.forEach(function(c){ c.classList.remove("active"); });
          chip.classList.add("active");
          activeCat = chip.getAttribute("data-cat");
          applyFilter();
        });
      });
      if(searchInput){ searchInput.addEventListener("input", applyFilter); }
      applyFilter();
    }

    /* ---------- Product gallery thumbnails (Product detail page) ---------- */
    document.querySelectorAll("[data-gallery]").forEach(function(gallery){
      var main = gallery.querySelector(".pd-gallery-main");
      var thumbs = gallery.querySelectorAll(".pd-thumb");
      thumbs.forEach(function(thumb){
        thumb.addEventListener("click", function(){
          thumbs.forEach(function(t){ t.classList.remove("active"); });
          thumb.classList.add("active");
          if(main) main.innerHTML = thumb.innerHTML;
        });
      });
    });

    /* ---------- Quote / enquiry form (client-side demo submit) ---------- */
    document.querySelectorAll("[data-quote-form]").forEach(function(form){
      form.addEventListener("submit", function(e){
        e.preventDefault();
        if(!form.checkValidity()){
          form.reportValidity();
          return;
        }
        var wrapper = form.closest("[data-form-wrapper]");
        var success = wrapper ? wrapper.querySelector(".form-success") : null;
        form.style.display = "none";
        if(success) success.classList.add("show");
        /*
          Production note: wire this submit handler to your backend / form
          endpoint (e.g. an email API or CRM webhook) to actually deliver
          enquiries. Currently this only shows a confirmation state.
        */
      });
    });

  });
})();
