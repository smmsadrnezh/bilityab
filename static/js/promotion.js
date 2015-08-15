jQuery(document).ready(function ($) {
    $('#add-promotion').find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: window.location.pathname,
            data: $("#add-promotion-form").serialize(), // serializes the form's elements.
            success: function (data) {
                if (parseInt(data)) {
                    window.location.replace(window.location.pathname);
                } else {
                    $('#add-promotion').find('input[type="number"]').toggleClass('has-error').next('span').toggleClass('is-visible');
                }
            }
        });

    });
});
