$(document).ready(function(){
    $('#search_btn').click(search);
});  

function search() {
	search_content = $('#search_content').val();
	console.log(search_content);
	alert(search_content);
}

function render_post(post_data) {

 	insertpost = "<div class='panel panel-default' id=user-post"+ post_data.id +">" +
	          		"<div class='panel-heading'>" +
	          			"<button type='button' class='close' aria-label='Close'" + 
	          			" onclick='delete_post(" + post_data.id + ")'" + ">" +
				            	"<span aria-hidden='true'>&times;</span>" +
				    	"</button>" +
	          		"</div>" +
	    			" <div class='panel-body'>" +
		    			"<div class='media'>" +
						  "<div class='media-left'>" + 
						    "<img src='image/default_user.png' class='media-object' style='width:60px'>" +
						  "</div>" +
						  "<div class='media-body'>" +
						    "<h4 class='media-heading'>" + post_data.author + "</h4>" + 
						    "<p><small><i>Posts on " + post_data.date +"</i></small></p>" +

						  "</div>" +
						  "<div id=post-content" +  post_data.id + ">" +
						  	"<p>" + post_data.content + "</p>" +
						  "</div>" +
						"</div>" +
		    		"</div>" +
			    	"<div class='panel-footer'>" +
			    		"<button class='btn btn-primary' type='button' id='like_btn' onclick='like_post(" + 
			    				post_data.id + ")'>Like</button>" +
			    		"<label class='control-label' for='like_btn' id="+ post_data.id +">"+ post_data.likes +"</label>" +
			    	"</div>" + 
	  			"</div>";

	return insertpost;
 }

