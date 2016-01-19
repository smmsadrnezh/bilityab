(function ($) {

    $('#filter').on('click', function () {

        window.location.href = "http://127.0.0.1:8000/SalesChart/" + "?start-date=" + $('#start-date').val() + "&end-date=" + $('#end-date').val();

    });

})(jQuery);