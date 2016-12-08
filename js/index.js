/**
 * Created by Fangzhou Liu on 10/20/2016.
 *
 * Javascript for Login page for cookie check
 * 
 */
$(document).ready(function(){
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
        url: '../cgi-bin/main_page.py',  // lecture 8 script to query the pizza database
        type: "POST",                  // GET or POST

        dataType: "json",             // json format

        success: function( data ) {   // function to execute upon a successful request
          console.log("Send Cookie");
          console.log(data);
        	if (data.user_name != "nil") { // return a cookie
            //success_handler(data)
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

    url: "../cgi-bin/sign_in.py",

    type: "POST",

    data: {
            'user_id':user_id,
            'password':pwd,
            'remember_me': remember
          },

    // dataType: "json",

    // when successfully login
    success: function (data) {
        console.log("Success Login");
        login_result = data.result;
        //success_handler(data);
        if (login_result == "success") {
          success_handler(data);
          $("#login_panel").modal('toggle');
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
  var username = $('#signup_username').val();
  var nickname = $('#signup_nickname').val();
  var password = $('#signup_password').val();
  var re_password = $('#re_password').val();
  var email = $('#signup_email').val();
  var team;
  var regular_exp=/\S+@\S+\.\S+/;
  //console.log(team);

  if(document.getElementById('team_mystic').checked){

    team="mystic";
    //console.log(team);
  }else if(document.getElementById('team_valor').checked){
    team="valor";
  }else if(document.getElementById('team_instinct').checked){
    team="instinct";
  }else if(document.getElementById('team_undecide').checked){
    team="undecide";
  }else{
    team="";
  }

  if(username==""||password==""||re_password==""||email==""||team==""){
    $('#error_panel_signup').html("all content must be filled out");
    return;
  }

  console.log(re_password);
  console.log(password);

  if(re_password != password){
    $('#error_panel_signup').html("Your two passwords must be the same");
    return;
  }
  if(re_password==password){
    $('#error_panel_signup').html("");
  }
  if(!regular_exp.test(email)){
    //console.log(regular_exp.test(email));
    $('#error_panel_signup').html("your email style is not valid");
    return;
  }

  $.ajax({

    url: "../cgi-bin/sign_up.py",

    type: "POST",

    data: {
            user_id: username,
            nickname: nickname,
            password: password,
            email: email,
            team: team,
          },

    // dataType: "json",

    // when successfully login
    success: function (data) {
        console.log("Success Login");
        signup_result = data.result;
        //success_handler(data);
        if (signup_result == "success") {
          $("#signup_panel").modal('toggle');
          success_handler(data);
        }
        else {
          $('#error_panel_signup').html(data.result);
          signup_error(signup_result);
          //$('#error_panel_signup').html(data.result);
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

// when the user click the logout button on the screen
// this logout method will be triggeerd
var logout = function() {
  console.log("Logout!");

  // if $.cookie {
  //   console.log($.cookie);
  // }

    $.ajax( {

        url: "../cgi-bin/log_out.py",

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
    // alert("!!!???s");
    console.log("success!");
    console.log(data);
    $('#home').html("<a>Home</a>");
    $('#posts').html("<a href='post.html'>Posts</a>");
    $('#pokemons').html("<a href='http://www.pokemongo.com/en/'>Pokemon</a>");
    $('#profile').html("<a href='change.html'>Profile</a>");
    $('#search').html("<a href='search.html'>Search</a>");
    $('#logout').html("<a>Log Out</a>");
    // $('#login_panel').empty();
    $('#sign_in_btn').hide();
    $('#sign_up_btn').hide();
    $('#name_logo').html('Welcome! ' + data.user_name);
    //$('#login_panel').hide();
    //display post field by Ma Jinjian
    //$('#post-field').css("display","block")
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
    $('#search').empty();
    $('#logout').empty();
     // $('#login').html("<a href='../sign_in.html'>Log In</a>"); 
    $('#sign_in_btn').show();
    $('#sign_up_btn').show();      
    $('#name_logo').html("Welcome! Sommoner");
}

