jQuery(document).ready(function ($) {
    var $form_modal = $('.cd-user-modal'),
        $form_login = $form_modal.find('#cd-login'),
        $form_signup = $form_modal.find('#cd-signup'),
        $form_forgot_password = $form_modal.find('#cd-reset-password'),
        $form_modal_tab = $('.cd-switcher'),
        $tab_login = $form_modal_tab.children('li').eq(0).children('a'),
        $tab_signup = $form_modal_tab.children('li').eq(1).children('a'),
        $forgot_password_link = $form_login.find('.cd-form-bottom-message a'),
        $back_to_login_link = $form_forgot_password.find('.cd-form-bottom-message a'),
        $main_nav = $('#login-register');

    if(parseInt($('#body-container').attr('going_recovery')))
    {
        $main_nav.children('ul').removeClass('is-visible');
        $form_modal.addClass('is-visible');
        login_selected();
        setTimeout(function () {
            $('#recovery-message').slideUp(function () {
                $(this).css('display', 'none');
            });
        }, 3000);
    }

    //open modal
    $main_nav.on('click', function (event) {

        if ($(event.target).is($main_nav)) {
            // on mobile open the submenu
            $(this).children('ul').toggleClass('is-visible');
        } else {
            // on mobile close submenu
            $main_nav.children('ul').removeClass('is-visible');
            //show modal layer
            $form_modal.addClass('is-visible');
            //show the selected form
            ( $(event.target).is('#for-register') ) ? signup_selected() : login_selected();
        }

    });

    //close modal
    $('.cd-user-modal').on('click', function (event) {
        if ($(event.target).is($form_modal) || $(event.target).is('.cd-close-form')) {
            $form_modal.removeClass('is-visible');
        }
    });
    //close modal when clicking the esc keyboard button
    $(document).keyup(function (event) {
        if (event.which == '27') {
            $form_modal.removeClass('is-visible');
        }
    });

    //switch from a tab to another
    $form_modal_tab.on('click', function (event) {
        event.preventDefault();
        ( $(event.target).is($tab_login) ) ? login_selected() : signup_selected();
    });

    //hide or show password
    $('.hide-password').on('click', function () {
        var $this = $(this),
            $password_field = $this.prev('input');

        ( 'password' == $password_field.attr('type') ) ? $password_field.attr('type', 'text') : $password_field.attr('type', 'password');
        ( 'مخفی کردن' == $this.text() ) ? $this.text('نمایش') : $this.text('مخفی کردن');
        //focus and move cursor to the end of input field
        $password_field.putCursorAtEnd();
    });

    //show forgot-password form
    $forgot_password_link.on('click', function (event) {
        event.preventDefault();
        forgot_password_selected();
    });

    //back to login from the forgot-password form
    $back_to_login_link.on('click', function (event) {
        event.preventDefault();
        login_selected();
    });

    function login_selected() {
        is_registering = false;
        $form_login.addClass('is-selected');
        $form_signup.removeClass('is-selected');
        $form_forgot_password.removeClass('is-selected');
        $tab_login.addClass('selected');
        $tab_signup.removeClass('selected');
    }

    function signup_selected() {
        is_registering = true;
        $form_login.removeClass('is-selected');
        $form_signup.addClass('is-selected');
        $form_forgot_password.removeClass('is-selected');
        $tab_login.removeClass('selected');
        $tab_signup.addClass('selected');
    }

    function forgot_password_selected() {
        is_registering = false;
        $form_login.removeClass('is-selected');
        $form_signup.removeClass('is-selected');
        $form_forgot_password.addClass('is-selected');
    }

    var is_registering = false;

    $form_forgot_password.find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();
        if (!isEmail($('#reset-email').val())) {
            $('#reset-email').toggleClass('has-error').next('span').text('پست الکترونیکی نامعتبر!').toggleClass('is-visible');
            setTimeout(function () {
                hide_error($('#reset-email'));
            }, 3000);
        }
        else {
            $.ajax({
                type: "POST",
                url: "/recover/",
                data: $("#recover-form").serialize(),
                success: function (data) {
                    if (parseInt(data)) {
                        var message = $form_forgot_password.find('.cd-form-message');
                        var old_message = message.text();
                        message.fadeOut(function () {
                            message.css('color', '#147D0E').text('لینک دریافت رمز عبور جدید به ایمیل شما ارسال شد.').fadeIn();
                        });
                        setTimeout(function () {
                            message.css('color', '#000').text(old_message);
                            if (!is_registering)
                                $back_to_login_link.click();
                        }, 4000);
                    }
                }
            });
        }
    });

    function isEmail(email) {
        var emailReg = /^([a-zA-Z0-9_.+-])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        return emailReg.test(email);
    }

    $form_login.find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "/login/",
            data: $("#signin-form").serialize(),
            success: function (data) {
                if (parseInt(data)) {
                    window.location.replace(window.location.pathname);
                } else {
                    $form_login.find('input[type="text"]').toggleClass('has-error').next('span').toggleClass('is-visible');
                    $form_login.find('input[type="password"]').toggleClass('has-error').next('a').next('span').toggleClass('is-visible');
                    setTimeout(function () {
                        hide_error($form_login.find('input[type="text"]'));
                        hide_error($form_login.find('input[type="password"]'));
                    }, 3000);
                }
            }
        });

    });

    function hide_error($elem) {
        $elem.toggleClass('has-error').parent().find('span').toggleClass('is-visible');
    }

    $form_signup.find('input[type="submit"]').on('click', function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "/register/",
            data: $("#signup-form").serialize(), // serializes the form's elements.
            success: function (data) {
                if (data == 'success') {
                    window.location.replace(window.location.pathname);
                } else {
                    data = data.trim();
                    var errors = data.split(' ');
                    for (var error in errors) {
                        switch (errors[error]) {
                            case 'invalid_first_name':
                                $('#signup-first-name').toggleClass('has-error').next('span').text('نام نامعتبر').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-first-name'));
                                }, 3000);
                                break;
                            case 'empty_first_name':
                                $('#signup-first-name').toggleClass('has-error').next('span').text('نامتان را وارد کنید').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-first-name'));
                                }, 3000);
                                break;
                            case 'invalid_last_name':
                                $('#signup-last-name').toggleClass('has-error').next('span').text('نام خانوادگی نامعتبر').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-last-name'));
                                }, 3000);
                                break;
                            case 'empty_last_name':
                                $('#signup-last-name').toggleClass('has-error').next('span').text('نام خانوادگی تان را وارد کنید').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-last-name'));
                                }, 3000);
                                break;
                            case 'date':
                                $('#signup-birth-date').toggleClass('has-error').next('span').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-birth-date'));
                                }, 3000);
                                break;
                            case 'password':
                                $('#signup-password').toggleClass('has-error').next('a').next('span').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-password'));
                                }, 3000);
                                break;
                            case 'invalid_email':
                                $('#signup-email').toggleClass('has-error').next('span').text('پست الکترونیکی نامعتبر').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-email'));
                                }, 3000);
                                break;
                            case 'registered_email':
                                $('#signup-email').toggleClass('has-error').next('span').text('این پست الکترونیکی قبلا وارد شده است').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-email'));
                                }, 3000);
                                break;
                            case 'taken_username':
                                $('#signup-username').toggleClass('has-error').next('span').toggleClass('is-visible');
                                setTimeout(function () {
                                    hide_error($('#signup-username'));
                                }, 3000);
                                break;
                        }
                    }
                }
            }
        });

    });

});


//credits http://css-tricks.com/snippets/jquery/move-cursor-to-end-of-textarea-or-input/
jQuery.fn.putCursorAtEnd = function () {
    return this.each(function () {
        // If this function exists...
        if (this.setSelectionRange) {
            // ... then use it (Doesn't work in IE)
            // Double the length because Opera is inconsistent about whether a carriage return is one character or two. Sigh.
            var len = $(this).val().length * 2;
            this.setSelectionRange(len, len);
        } else {
            // ... otherwise replace the contents with itself
            // (Doesn't work in Google Chrome)
            $(this).val($(this).val());
        }
    });
};