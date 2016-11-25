/**
 * Created by Fangzhou Liu on 10/20/2016.
 *
 * Javascript for Login page for cookie check
 * 
 */
$(document).ready(function(){  
     alert("Hello World");  
     send_cookie();
     $('#login_btn').click(login);
     $('#logout').click(logout);
     $('#signup_btn').click(signup);
});  



// send the cookie to the server before the page was loaded
// 
var send_cookie = function () {
    // .ajax is the core Ajax function supported by jQuery and requires the following parameters:
    //  url: the URL of the resource to send the request to
    //  data: the data to send along with the request; encoded as a query string for GET
    //  dataType: the expected format of the data coming back in the response
    //  success: a function to execute if the request is successful
    //  error: a function to execute if the request fails for any reason
    $.ajax({
        url: '../cgi-bin/main_page_test.py',  // lecture 8 script to query the pizza database

        type: "POST",                  // GET or POST

        dataType: "json",             // json format

        success: function( data ) {   // function to execute upon a successful request
          console.log("Send Cookie");
          console.log(data);
        	if (data.user_name != "nil") { // return a cookie
            login_result = data.result;
            if (login_result == "success") {
              success_handler(data);
            }
            else {
              login_error(login_result);
            }
        	}
        	else { // no cookie or error
	           error_handler();
          }
        },

        error: function(request) {   // function to call when the request fails, other errors
            console.log("Error!");
            console.log(request);
            error_handler();
        }
    });
}

// when the user click the login button on the screen
// this login method will be triggeerd
var login = function () {

  var user_id = $('#username').val();
  var pwd = $('#password').val();
  var remember = $('#remember_me').prop("checked");
  console.log(user_id);
  console.log(pwd);
  console.log(remember);
  if (user_id == "" || pwd == "") {
    $('#error_panel_signin').html("Your Username or Password cannot be left empty!!!")
  }

  $.ajax({

    url: "../cgi-bin/sign_in_test.py",

    type: "POST",

    data: {
      user_id: user_id,
      password: pwd,
      remember_me: remember
    },

    // dataType: "json",

    // when successfully login
    success: function (data) {
        console.log("Success Login");
        login_result = data.result;
        // success_handler(data);
        if (login_result == "success") {
          success_handler(data);
        }
        else {
          login_error(login_result);
        }
    },

    error: function (request,status, error) {
        console.log("Error Login");
        console.log(request);
        console.log(error);
        error_handler()
    }
  });
}

// call when signup button clicked
var signup = function() {

}

// when the user click the logout button on the screen
// this logout method will be triggeerd
var logout = function() {
  console.log("Logout!");

  // if $.cookie {
  //   console.log($.cookie);
  // }

    $.ajax( {

        url: "../cgi-bin/log_out_test.py",

        type: "POST",

        success: function (data) {
            console.log("Success Logout");
            error_handler();
        },

        error: function (request) {
            console.log("Error Logout");
            console.log(request);
        }

    });

}

var success_handler = function(data) {

    console.log("success!");
    console.log(data);
    $('#home').html("<a>Home</a>");
    $('#posts').html("<a href='#posts'>Posts</a>");
    $('#pokemons').html("<a href='#pokemons'>Pokemon</a>");
    $('#profile').html("<a href='#profile'>Profile</a>");
    $('#logout').html("<a>Log Out</a>");
    // $('#login_panel').empty();
    $('#sign_in_btn').hide();
    $('#sign_up_btn').hide();
    $('#name_logo').html('Welcome! ' + data.user_name);

    // console.log(data.password)

}

var login_error = function(err_msg) {
    error_handler();
    $('#error_panel_signin').html(err_msg);
}

var signup_error = function(err_msg) {
  error_handler();
    $('#error_panel_signup').html(err_msg);
}


var error_handler = function() {
    $('#home').empty();
    $('#posts').empty();
    $('#pokemons').empty();
    $('#profile').empty();
    $('#logout').empty();
     // $('#login').html("<a href='../sign_in.html'>Log In</a>"); 
    $('#sign_in_btn').show();
    $('#sign_up_btn').show();      
    $('#name_logo').html("Welcome! Sommoner");
}