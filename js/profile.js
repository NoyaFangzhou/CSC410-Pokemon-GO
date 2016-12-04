

$(document).ready(function(){
     load_profile();
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
      alert("fail");
      // alert(stringify(data));
    }
  });
}


function update()
    {
     
      $.ajax({
        url: "../cgi-bin/profile.py",

        type: "POST",

        data: "modify = True&email_address=" +$("#profile_email_address").val()+ "&nickname="+$("#profile_nickname").val(),

        dataType: "json",

        success:function(data){
          alert("modify success!");
        },

        error:function(data){
          alert("modify fail");
        }

  });
    }


function prom() {  
  var name = prompt("Please type your new password", "");   
  if(name != null) {
    $.ajax({
      url: "../cgi-bin/profile.py",

      type: "POST",

      data: "change_password="+name,

      dataType: "json",

      success:function(data){
        alert("Password modified successfully!");
      },

      error:function(data){
        alert("Password modified fail");
      }
    });
  }
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