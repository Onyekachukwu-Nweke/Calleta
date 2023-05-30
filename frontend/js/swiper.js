$(document).ready(function(){
  $(".owl-carousel").owlCarousel({
    // loop:true,
    // center: true,
    margin:1,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:false
        },
        600:{
            items:3,
            nav:false
        },
        1000:{
            items:4,
            nav:false,
        }
    },
    autoPlay : true,
    autoplayTimeout:1000,
    autoplayHoverPause:true,
    goToFirst : true,
    goToFirstSpeed : 1000
  });
});