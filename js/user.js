$(document).ready(function(){
  $('#followButton').click(follow);
  get_info();
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


function get_info(){
	$.ajax(
    {
      url: "../cgi-bin/user.py",
      
      type: "POST",

      data: "follow=false&id="+follower_id,

      dataType: "json",

      success: function(data){
        	$("#username").html(follower_id);
        	$("#followButton").html(get_follow_value(data.follow));
        	$("#followButton").val(get_follow_value(data.follow));
        	$("#userImage").attr("src", change_path(data.team));

      },

      error: function(data) {
        //alert("get friend lists fail");
      }
    });
}

function follow(){
	console.log($("#followButton").val());
$.ajax(
    {
      url: "../cgi-bin/user.py",
      
      type: "POST",

      data: "follow=true&id="+follower_id+"&follow_status="+$("#followButton").val(),

      dataType: "json",

      success: function(data){
      	var follow_status = $("#followButton").val();
        	if(data.status != 'error'){
        		if(follow_status == 'Follow')
                  { 
                    $('#followButton').html("Unfollow");
                    //alert('Follow user: '+ follow_id + 'success');
                  }
              else
                  {
                    $('#followButton').html("Follow");
                    //alert('Unollow user: '+ follow_id + 'success');
              }
        	}
        	get_info();

      },

      error: function(data) {
        //alert("get friend lists fail");
      }
    });
}