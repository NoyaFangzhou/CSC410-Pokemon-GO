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


$('#new_post').focus(function() {
	console.log("focus");
	show_posts();
});
/**
 * retrieve posts when load page
 */
function retrieve_posts() {
	$.ajax({
		url: "/cgi-bin/postHandler.py",
			
		type: "POST",

		dataType: "json",

		success: function(data) {
			posts = JSON.parse(data);
			if(posts.length > 0) {
				posts.forEach(function(element){
					post_array.push(element);
				});
				display_posts();
			}
		},

		error: function(data) {
			alert(data);
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
			insertpost = render_post(data);
			$("#posts").prepend(insertpost);
			post_array.push(data);
		},

		error: function(data) {
			alert("failed");
			console.log(data);
		}
	});
});

/**
 * delete_post - delete a post
 */
function delete_post() {
	$.ajax({
		url: "/cgi-bin/"

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
 	insertpost = "<div id='user-post' class='row'>" +
 						"<table border='0' style='word-break:break-all; word-wrap:break-all;'>" +
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
										"<button class='btn btn-primary'>" +
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
	return insertpost;
 }
