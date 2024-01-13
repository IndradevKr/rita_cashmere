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

nextHeroSlide.addEventListener("click", function () {
    if(heroCurrentSlide === heroMaxSlide){
        heroCurrentSlide = 0;
    } else {
    heroCurrentSlide++;
    }
 heroSlides.forEach((slide, index) => {
   slide.style.transform = `translateX(${100 * (index - heroCurrentSlide)}%)`;
 });
});
// add event listener and navigation functionality
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

const categorySlides = document.querySelectorAll(".category-slide");

categorySlides.forEach((slide, index) => {
  slide.style.transform = `translateX(${index * 100}%)`;
});

let categoryCurrentSlide = 0;
let categoryMaxSlide = categorySlides.length - 1;

const nextCategorySlide= document.querySelector(".category-btn-next");
const prevCategorySlide = document.querySelector(".category-btn-prev");

nextCategorySlide.addEventListener("click", function () {
    if(categoryCurrentSlide === categoryMaxSlide){
        categoryCurrentSlide = 0;
    } else {
    categoryCurrentSlide++;
    }
 categorySlides.forEach((slide, index) => {
   slide.style.transform = `translateX(${100 * (index - categoryCurrentSlide)}%)`;
 });
});
// add event listener and navigation functionality
prevCategorySlide.addEventListener("click", function () {
    // check if current slide is the first and reset current slide to last
    if (categoryCurrentSlide === 0) {
      categoryCurrentSlide = categoryMaxSlide;
    } else {
      categoryCurrentSlide--;
    }
  
    //   move slide by 100%
    categorySlides.forEach((slide, index) => {
      slide.style.transform = `translateX(${100 * (index - categoryCurrentSlide)}%)`;
    });
  });