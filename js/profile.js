
$(document).ready(function(){
    /**
     * check user login
     */
    $.ajax({
      url: "/cgi-bin/accessManager.py",

      type: "POST",

      dataType: "json",

      success: function(data) {
        if(data.access == "deny") {
          alert("Please Login");
          window.location.pathname = "index.html";
        }
        else {
          load_profile();

         $('#modify_btn').click(update);
         $('#password_submit').click(modify_pwd);
        }
      },

      error: function(data) {
        alert("server error");
      }
    });
     // $('#home').html("<a href='main_page.html'></a>");
});  
/**
 * retrieve posts
 */
function load_profile() {
  $.ajax({
    url: "../cgi-bin/profile.py",
      
    type: "POST",

    data: "modify=False",

    dataType: "json",

    success: function(data) {
      // alert(data);
      // console.log("ajax");
      // console.log(data);
      var t = JSON.parse(data);
      // console.log("t");
      // console.log(t[0]);
      // alert(t);
      // alert(t.nickname);
      // alert(data.nickname);
      $("#profile_email_address").val(t[0].email_address);
      $("#profile_username").val(t[0].user_ID);
      $("#profile_nickname").val(t[0].nickname);
      // console.log("!!!!!!!!!1");
      // console.log(document.getElementById("profile_username").value);
    },

    error: function(data) {
      alert("load data error");
      // alert(stringify(data));
    }
  });
}


function update()
    {
     
      $.ajax({
        url: "../cgi-bin/profile.py",

        type: "POST",

        data: "modify=True&email_address=" +$("#profile_email_address").val()+ "&nickname="+$("#profile_nickname").val(),

        dataType: "json",

        success:function(data){
          alert("modify success!");
        },

        error:function(data){
          console.log(data)
          alert("modify fail");
        }

  });
    }


// function prom() {  

//   var name = prompt("Please type your new password", "");   
//   if(name != null) {
//     $.ajax({
//       url: "../cgi-bin/profile.py",

//       type: "POST",

//       data: "change_password="+name,

//       dataType: "json",

//       success:function(data){
//         alert("Password modified successfully!");
//       },

//       error:function(data){
//         alert("Password modified fail");
//       }
//     });

// }  

function modify_pwd() {  

    var old_pwd = $('#old_password').val();
    var new_pwd = $('#new_password').val();
    var re_new_pwd = $('#re_new_password').val();

    console.log(old_pwd);
    console.log(new_pwd);
    console.log(re_new_pwd);
    if (old_pwd == "" || new_pwd == "" || re_new_pwd == "") {
      $('#error_panel_modify').html("Should fill all table");
      return;
    }
    if (new_pwd != re_new_pwd) {
      $('#error_panel_modify').html("New Password not match");
      return;
    }
    if (new_pwd == old_pwd) {
      $('#error_panel_modify').html("No difference between new and old Password");
      return;
    }
    
    $.ajax({
      url: "../cgi-bin/profile.py",

      type: "POST",

      data: {
        change_password: 'True',
        old_password: old_pwd,
        new_password: new_pwd,
      },

      dataType: "json",

      success:function(data){

        if(data.status == "false"){
              $('#error_panel_modify').html("password error");
          }
        else{
            alert("Password modified successfully!");
            $("#change_pwd_modal").hide();
        }
      },

      error:function(data){
        alert("Password modified failed!");
      }
    });

}



// /**
//  * display_post - show all the posts
//  */
 // function display_profile() {
 //    insertpost = "<div id='user-post'>" +
 //              "<a id='post-user'>" + item.author + "</a>" +
 //              "<a id= 'delete'> x </a>" +
 //              "<div id='content'>" + item.content + "</div>" +
 //              "<div id= 'date'>" + item.date + "</div>" +
 //             "</div>"
 //    $("#posts").append(insertpost);
 //  );
 // }