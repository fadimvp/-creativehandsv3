
function showMenuFunction() {
  var x = document.getElementById("toggle-menu");

  if (x.style.display === "block") {
    x.classList.remove("animate__zoomIn");
    x.classList.add("animate__zoomOut");
    setTimeout(() => {
      x.classList.remove("animate__zoomOut");
      x.style.display = "none";
    }, 600);
    
    
  } else {
    
    x.style.display = "block";
    x.classList.remove("animate__zoomOut");
    x.classList.add("animate__zoomIn");
    
  }
}


/* Category carousel start */
$('.owl-carousel').owlCarousel({
    
    margin:10,
    nav:false,
    autoplay:true,
    loop:true,
    navText: ['<i class="fas fa-angle-left"></i>', '<i class="fas fa-angle-right"></i>'],
    dots:false,
    responsive:{
        0:{
            items:2
        },
        768:{
            items:3
        },
        992:{
            items:4
        },
        1000:{
            items:5
        }
    }
}) /* Category carousel end */

/* Show cart start */


/* Show cart end */
 $(function() {
const cartOpen = document.querySelector(".cart-info");
const cartClose = document.querySelector(".close__toggle");
const cartDivOpen = document.querySelector(".cart-info-base");
const cartConteiner = document.querySelector(".cart-info-base");
const bodyBg = document.querySelector(".body-class");

cartOpen.addEventListener("click", () => {
    cartDivOpen.classList.add("open");
    document.body.classList.add("active");
    cartConteiner.style.right = "0";
    cartConteiner.style.width = "350px";
    cartConteiner.style.opacity = "1.0";
    bodyBg.classList.add("bgcolor");
    

});

cartClose.addEventListener("click", () => {
    cartDivOpen.classList.remove("open");
    document.body.classList.remove("active");
    cartConteiner.style.right = "-355px";
    cartConteiner.style.opacity = "0.0";
    bodyBg.classList.remove("bgcolor");
    

});

});

const shipBtn = document.querySelector('.dif-ship-btn');
const shipOpen = document.querySelector('.different-address');
shipBtn.addEventListener('click', () => {
  shipOpen.classList.toggle("active");
  // shipOpen.style.transition = "all 0.3s";
});

/* Show cart end */


// Checkout page js 

const dbtBtn = document.querySelector('.dbt');
const dbtDiv = document.querySelector('.dbt-div');
const codBtn = document.querySelector('.cod');
const codDiv = document.querySelector('.cod-div');
const stcBtn = document.querySelector('.stc');
const stcDiv = document.querySelector('.stc-div');

dbtBtn.addEventListener('click', () => {
 
  dbtDiv.classList.add('active');
  codDiv.classList.remove('active');
  stcDiv.classList.remove('active');
})
codBtn.addEventListener('click', () => {

  dbtDiv.classList.remove('active');
  codDiv.classList.add('active');
  stcDiv.classList.remove('active');
})

stcBtn.addEventListener('click', () => {

  dbtDiv.classList.remove('active');
  codDiv.classList.remove('active');
  stcDiv.classList.add('active');
})

setTimeout(function(){
  $('#message').fadeOut('slow')
},4000)