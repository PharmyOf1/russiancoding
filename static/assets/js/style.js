$(window).scroll(function() {
    var distanceFromTop = $(this).scrollTop();
    if (distanceFromTop >= $('.brand-main-top').height()) {
        $('.navbar').addClass('fixed');
        $('.brand-main-top').css('margin-bottom','100px');
    } else {
        $('.navbar').removeClass('fixed');
        $('.brand-main-top').css('margin-bottom','0px');
    }
});
