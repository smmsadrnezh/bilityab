jQuery(document).ready(function ($) {

    $searchbtn = $('#search-btn');

    $searchbtn.on('click', function (event) {

        //fire the submit event on the form
        $('#search-form').trigger('submit');

        //stop the default behavior of the link
        return false;

    });

    $("#help-link").on('click', function () {

        window.location = "/Help";

    });

});