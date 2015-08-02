jQuery(document).ready(function ($) {
    $('#add-event').find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();

        $.ajax({
            type: "POST",
            url: "/events/add/",
            data: $("#add-event-form").serialize(), // serializes the form's elements.
            success: function (data) {
                alert("a");
                if (parseInt(data)) {
                    window.location.replace(window.location.pathname);
                } else {
                    $form_login.find('input[type="text"]').toggleClass('has-error').next('span').toggleClass('is-visible');
                    $form_login.find('input[type="password"]').toggleClass('has-error').next('a').next('span').toggleClass('is-visible');
                }
            }

        });

    });
});