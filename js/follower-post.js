var post_array = new Array();				/* Array store posts of follower */
var path = $(location).attr('href');		/* split url */
var follower_id = path.split("?")[1];		/* retrieve GET parameter */


/* check user login */
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
			retrieve_posts();
		}
	},

	error: function(data) {
		alert("server error");
	}

});


/**
 * retrieve_posts - get post from server
 */
 function retrieve_posts() {
 	$.ajax({
		url: "/cgi-bin/postHandler.py",
			
		type: "POST",

		dataType: "json",

		data: "friend-post=true&id=" + follower_id,

		success: function(data) {
			if(data.result != 'failed') {
				if(JSON.stringify(data) != '{}'){
					posts = JSON.parse(data);
					if(posts.length > 0) {
						posts.forEach(function(element){
							post_array.push(element);
						});
						display_posts();
					}
				}
			}
			else {
				alert("server error")
			}
			
		},

		error: function(data) {
			alert("request failed");
		}
	});
 }


 /**
 * like_post - like a post
 */
 function like_post(post_id) {
 	$.ajax({
		url: "/cgi-bin/postHandler.py",

		type: "POST",

		data: "like=true&id=" + post_id,

		dataType: "json",

		success: function(data) {
			if(data.result == 'succeed') {
				old_likes = parseInt($("#"+post_id).text());

				$("#"+post_id).text(++old_likes);

			}
			else if(data.result != "no change") {
				alert("server error")
			}
		},

		error: function(data) {
			alert("server error");
			console.log(data);
		}

	});
 }


/**
 * display_post - show all the posts
 */
 function display_posts() {
 	post_array.forEach(function(item){
 		insertpost = render_post(item);
		$("#posts").append(insertpost);
		if(item.img) {
			load_img(item);
		}
 	});
 }


/**
 * render_post - form post data into html fashion
 * return: html string
 */
 function render_post(post_data) {

 	insertpost = "<div class='panel panel-default' id=user-post"+ post_data.id +">" +
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

 function load_img(data) {
 	img = $("<img id='post-img' style='max-width: 100%; width: auto; height: auto;'>");
	img.attr("src", data.img);
	img.prependTo("#post-content" + data.id);
 }

