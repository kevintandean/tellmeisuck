/**
 * Created by kevin on 7/31/2014.
 */

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
var me;


function get_post(id) {
    $.ajax({
        url: '/get_post/' + id,
        type: 'GET',
        dataType: 'html',
        success: function (response) {
            console.log(response);
            $('#posts').html(response);
            $('.post').fadeIn('fast');
            var latest = $('#posts').children().first().data('id');
            console.log(latest);
            (function check_new_post(id, latest) {
                $.ajax({
                    url: '/check_new_post/' + id + '/' + latest,
                    type: 'GET',
                    dataType: 'html',
                    success: function (response) {
                        console.log(response);
                        $('#posts').prepend(response);
                        $('.post').fadeIn('fast');
                    },
                    complete: function () {
                        var updated = $('#posts').children().first().data('id');
                        setTimeout(function () {
                            check_new_post(id, updated)
                        }, 5000);
                    }})
            })(id, latest)
        }
    })
}

function create_post(id) {
    var data = {'author': me, 'recipient': id};
    var jsondata = JSON.stringify(data);
    $.ajax({
            url: '/post/',
            type: 'GET',
            dataType: 'html',
            success: function (response) {
                console.log(response);
                $('#post').html(response);
                $('#id_recipient').val(id);
                $('#id_author').val(me);
                $('#postForm').modal();

            }
        }
    )
}

function submit_post(data) {
    console.log(data);
    var jsondata = JSON.stringify(data);
    $.ajax({
        url: '/post/',
        type: 'POST',
        dataType: 'json',
        data: jsondata
    })
}

function create_user(data) {
    var jsondata = JSON.stringify(data);
    $.ajax({
        url: '/create_user/',
        type: 'POST',
        data: jsondata,
        dataType: 'json',
    })
}

function Status() {
    FB.getLoginStatus(function (response) {
            if ('connected' == response.status) {
                FB.api("/me", function (response) {
                    console.log(response);
                    me = response['id'];
                    var user_id = response['id'];
                    var first_name = response['first_name'];
                    var last_name = response['last_name'];
                    var email = response['email'];
                    var user_data = {'user_id': user_id, 'first_name': first_name, 'last_name': last_name, 'email': email};
                    create_user(user_data);
                    $('#username').html(first_name + last_name);
                    getFriends();
                    get_post(me);
                });
                $('#myModal').modal('hide');
            } else {
                $('#myModal').modal(
                )
            };

//            console.log(response)
        }
    )
}
// This function is called when someone finishes with the Login using button
function checkLoginState() {
    Status()
}

function getFriends() {
    var data;
    FB.api("/me/friends", function (response) {
        data = JSON.stringify(response);
        console.log(data);
        $.ajax({
            url: '/display_friends/',
            type: 'POST',
            dataType: 'html',
            data: data,
            success: function (response) {
                console.log(response);
                $('#friends').append(response);
            },
            error: function (response) {
                console.log(response);
            }
        })
    });
}

// Load the SDK asynchronously
(function (d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s);
    js.id = id;
    js.src = "//connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

var user_id, first_name, last_name;
$(document).ready(function () {
    var id = '268058963391642';
    window.fbAsyncInit = function () {
        FB.init({
            appId: id,
            cookie: true,  // enable cookies to allow the server to access
            // the session
            xfbml: true,  // parse social plugins on this page
            version: 'v2.0' // use version 2.0
        });
        Status();

        $('#getfriends').on('click', function () {
            getFriends();
        });
        $(document).on('click', '#postToFriend', function () {
            create_post($(this).data('id'));
        });
        $(document).on('click', '#submitPost', function () {
            var author = ($(this).siblings('#id_author').val());
            var recipient = ($(this).siblings('#id_recipient').val());
            var good = ($(this).siblings('#id_good').val());
            var bad = ($(this).siblings('#id_bad').val());
            var data = {author: author, recipient: recipient, good: good, bad: bad};
            submit_post(data);
        });
        $(document).on('click', '#getposts', function () {
            get_post(me)

        });
        $(document).on('click', '#logout', function () {
            FB.logout()
        })
    }
})

