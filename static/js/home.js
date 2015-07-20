(function ($) {
    var cinemaImage = $(".cinema");
    cinemaImage.on('click', function () {
        window.location.href = "events/cinema/1";
    });

    var sportImage = $(".sport");
    sportImage.on('click', function () {
        window.location.href = "events/sport/1";
    });

    var tourismImage = $(".tourism");
    tourismImage.on('click', function () {
        window.location.href = "events/tourism/1";
    });

    var musicImage = $(".music");
    musicImage.on('click', function () {
        window.location.href = "events/music/1";
    });

})(jQuery);