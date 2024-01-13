// Select all slides
const heroSlides = document.querySelectorAll(".hero-slide");

// loop through slides and set each slides translateX property to index * 100%
heroSlides.forEach((slide, index) => {
  slide.style.transform = `translateX(${index * 100}%)`;
});

let heroCurrentSlide = 0;
let heroMaxSlide = heroSlides.length - 1;

const nextHeroSlide = document.querySelector(".hero-btn-next");
const prevHeroSlide = document.querySelector(".hero-btn-prev");

// add event listener and navigation functionality
nextHeroSlide.addEventListener("click", function () {
  if (heroCurrentSlide === heroMaxSlide) {
    heroCurrentSlide = 0;
  } else {
    heroCurrentSlide++;
  }
  heroSlides.forEach((slide, index) => {
    slide.style.transform = `translateX(${100 * (index - heroCurrentSlide)}%)`;
  });
});
prevHeroSlide.addEventListener("click", function () {
  // check if current slide is the first and reset current slide to last
  if (heroCurrentSlide === 0) {
    heroCurrentSlide = heroMaxSlide;
  } else {
    heroCurrentSlide--;
  }

  //   move slide by 100%
  heroSlides.forEach((slide, index) => {
    slide.style.transform = `translateX(${100 * (index - heroCurrentSlide)}%)`;
  });
});

// Set time interval for automatic slide change
const timeInterval = 3000; // 3 seconds
setInterval(() => {
  if (heroCurrentSlide === heroMaxSlide) {
    heroCurrentSlide = 0;
  } else {
    heroCurrentSlide++;
  }
  heroSlides.forEach((slide, index) => {
    slide.style.transform = `translateX(${100 * (index - heroCurrentSlide)}%)`;
  });
}, timeInterval);
