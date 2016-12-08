$(document).ready(function(){
  $('#search_btn').click(search);
  get_friend();
});




function change_path(team){
	if(team == "mystic"){
		return "../image/mystic.jpg";
	}else if(team == "valor"){
		return "../image/valor.jpg";
	}else if(team == "instinct"){
		return "../image/instinct.jpg";
	}else{
		return "../image/undecide.jpg"
	}
}

function get_follow_value(value){
  if(value == 'yes'){
        return "Unfollow";
  }else{
        return "Follow";
  }
}



function get_friend() {
  $.ajax(
    {
      url: "../cgi-bin/friend.py",
      
      type: "POST",

      data: "show=True",

      dataType: "json",

      success: function(data){
        console.log(data);
        friends = JSON.parse(data);
        if(friends.length > 0){
          friends.forEach(function(element){
              show_friend(element.name, change_path(element.team));
          });
        }
      },

      error: function(data) {
        //alert("get friend lists fail");
      }
    });
}

// gyp 12.3
function show_friend(name , team){
  // alert(name);
  insert_friends = "<ol class=\"list-unstyled\">" + 
              "<li>" +
                "<div class=\"media\">" +
          "<div class=\"media-left\">" +
            "<img src=\"" + team + "\" class=\"media-object\" style=\"width:30px\">" +
          "</div>" +
          "<div class=\"media-body\">" +
            "<label><a href='follower.html?" + name + "'>" + name + "</a></label>" +
          "</div>" + 
        "</div>" +
              "</li>" +
            "</ol>";
    $('#contactlist').append(insert_friends);
}


// 12.6

function change_follow(follow_status, follow_id){
  $.ajax({
      url: "../cgi-bin/friend.py",
      
      type: "POST",

      data: "show=False&search=False&follow_status="+follow_status+"&follow_id="+follow_id,

      dataType: "json",

      success:function(data){
        // alert(data.status);
          if (data.status != 'error'){
              if(follow_status == 'Follow')
                  { 
                    $('#button_' + follow_id).html("Unfollow");
                    //alert('Follow user: '+ follow_id + 'success');
                  }
              else
                  {
                    $('#button_' + follow_id).html("Follow");
                    //alert('Unollow user: '+ follow_id + 'success');
              }
      
          }else{
              alert("operation failed");
          }
          search();
      },

      error:function(data){
        // alert(data);
          alert("operation failed");
      }

  });
}


function show_follow(name,team , follow, follow_id){
  users=  
    "<div class='col-xs-12 col-sm-4 col-md-3 col-lg-3'>" +
    "<div class='tile'>" + 
      "<img src= '" + team + "' alt='Infinity-Loop' class='tile-image'>" +
      "<h3 class='tile-title'>" + name + "</h3>" +
      "<p></p>" +
      "<button type='button' id = 'button_"+ follow_id +"' onclick = \"change_follow('" + follow + "','" + follow_id + "')\" class='btn btn-primary btn-large btn-block' href='http://designmodo.com/flat'>" + follow +"</button>" + 
    "</div>" + 
  "</div>";
  // alert(users);
  // alert(name);
  $('#friend-list').append(users);
}


function search(){
  $.ajax({
      url: "../cgi-bin/friend.py",
      
      type: "POST",

      data: "show=False&search=True&name=" + $('#search_content').val(),

      dataType: "json",

      success:function(data){
        $('#friend-list').html(""); 
          var t = JSON.parse(data);
          // window.location.href ='../pokemon.html';
          if(t.length > 0){
            t.forEach(function(element){
                show_follow(element.user_ID, change_path(element.team) ,get_follow_value(element.follow) , element.user_ID);
            });
            }
      },

      error:function(data){
          data = JSON.parse(data);
          //alert(data);
          alert("error");
      }
  });
}

