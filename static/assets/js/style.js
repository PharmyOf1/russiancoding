$(window).scroll(function() {
    var distanceFromTop = $(this).scrollTop();
    if (distanceFromTop >= $('.brand-main-top').height()) {
        $('.navbar').addClass('fixed');
        $('.navbar-nav').addClass('fixed');
        $('.logo-nav-small').addClass('fixed');
        $('.brand-main-top').css('margin-bottom','80px');
    } else {
        $('.navbar').removeClass('fixed');
        $('.navbar-nav').removeClass('fixed');
        $('.logo-nav-small').removeClass('fixed');
        $('.brand-main-top').css('margin-bottom','0px');
    }
});
