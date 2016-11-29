var post_array = new Array();

$('#new_posts').focus(function() {
	$('#postModal').modal();
});

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
			retrieve_posts();
		}
	},

	error: function(data) {
		alert("server error");
	}
});

/**
 * retrieve posts when load page
 */
function retrieve_posts() {
	$.ajax({
		url: "/cgi-bin/postHandler.py",
			
		type: "POST",

		dataType: "json",

		data: "retrieve=true",

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
 * send one post to server
 */
$("#post-send").click(function() {
	$.ajax({
		url: "/cgi-bin/postHandler.py",
		
		type: "POST",
		
		data: "post-content=" + $('#post-text').val() +
			   "&new=true",

		dataType: "json",
		success: function(data) {
			if(data.result == 'succeed') {
				insertpost = render_post(data);
				$("#posts").prepend(insertpost);
				post_array.push(data);
			}
			else {
				alert("server error");
			}
		},

		error: function(data) {
			alert("request failed");
			console.log(data);
		}
	});
});

/**
 * delete_post - delete a post
 */
function delete_post(post_id) {
	$.ajax({
		url: "/cgi-bin/postHandler.py",

		type: "POST",

		data: "delete=true&id=" + post_id,

		dataType: "json",

		success: function(data) {
			if(data.result == 'succeed') {
				$("#user-post"+post_id.toString()).remove();
			}
			else {
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
			else {
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
 	});
 }


/**
 * render_post - form post data into html fashion
 * return: html string
 */
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
						  "</div>"+
						  "<p>" + post_data.content + "</p>" +
						"</div>" +
		    		"</div><!-- panel-body -->" +
			    		"<div class='panel-footer'>" +
			    			"<button class='btn btn-primary' type='button' id='like_btn' onclick='like_post(" + 
			    					post_data.id + ")'>Like</button>" +
			    			"<label class='control-label' for='like_btn' id="+ post_data.id +">"+ post_data.likes +"</label>" +
			    		"</div>" + 
	  				"</div><!-- panel-default -->";

 	/*insertpost = "<div id='user-post" + post_data.id + "' class='row'>" +
 						"<table border='0' style='word-break:break-all; word-wrap:break-all;'>" +
 							"<a onclick='delete_post(" + post_data.id + ")'>" + "x" + "</a>" + 
 							"<tr>" +
 								"<td rowspan='2'>" +
 									"image" +
								"</td>" +
								"<td><b>" + post_data.author + "</b></td>" +
							"</tr>" +
							"<tr>" +
								"<td>"+ post_data.date +"</td>" +
							"</tr>" +
							"<tr>" + 
								"<td colspan='2'>" +
									"<p>" +
										post_data.content + 
									"</p>" +
								"</td>" +
							"</tr>" +
							"<tr>" +
								"<td>" +
									"<div class = 'col-md-6'>" +
										"<button class='btn btn-primary' onclick='like_post(" + post_data.id + ")'>" +
											"Like" +
										"</button>" +
									"</div>" +
								"</td>" +
								"<td>" +
									"<div class='col-md-6'>" +
										"<button class='btn btn-primary'>" +
											"Comment" +
										"</button>" +
									"</div>" +
								"</td>" +
							"</tr>" +
							"<tr>" +
								"<td colspan='2'>" +
									"Comment Detail" +
								"</td>" +
							"</tr>" +
						"</table>" +
					"</div>";
		*/
	return insertpost;
 }