(function ($) {

    //var eventImage = $("#event_id");
    //eventImage.on('click', function () {
    //    window.location.href = "events/cinema/";
    //});

    var cinema_events = $('.cinema').closest('.event');
    cinema_events.on('click', function () {
        window.location.href = "events/cinema/"+cinema_events.attr('event_id');
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