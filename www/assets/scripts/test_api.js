
$(function() {
	$.ajaxSetup({
	  headers : {
	    'Authorization' : 'Digest NTEyZjZjOTA1ZjBhNDYwNjFjNzgwNWViYWE2MmZiNzA='
	  }
	});
	$("#try_api").submit(function(event) {
		submitApiHandler($(this), event);
	});
	$("#location_type").change(function(event) {
		location_type = $(this).find(":selected").val();

		// toggle which items are shown and hidden
		switch(location_type) {
			case "zip":
				$("#zip_container").show();
				$("#city_container").hide();
				$("#state_container").hide();
				$("input#zip").attr("required", true);
				$("input#city").attr("required", false);
				$("input#state").attr("required", false);
			break;
			case "city":
				$("#zip_container").hide();
				$("#city_container").show();
				$("#state_container").show();
				$("#documentation_link_container").show();
				$("input#zip").attr("required", false);
				$("input#city").attr("required", true);
				$("input#state").attr("required", true);
			break;
			case "state":
				$("#zip_container").hide();
				$("#city_container").hide();
				$("#state_container").show();
				$("#documentation_link_container").show();
				$("input#zip").attr("required", false);
				$("input#city").attr("required", true);
				$("input#state").attr("required", true);
			break;
			case "country":
				$("#zip_container").hide();
				$("#city_container").hide();
				$("#state_container").hide();
				$("#documentation_link_container").show();
				$("input#zip").attr("required", false);
				$("input#city").attr("required", false);
				$("input#state").attr("required", false);
			break;
			default:
		}
		$("#documentation_link_container").show();
		$("#submit_button_container").show();
	});
});


function capitalize(s) {
  if (typeof s !== 'string') return '';
  return s.charAt(0).toUpperCase() + s.slice(1);
}


function submitApiHandler(form, event) {
	$("#try_api_submit").prop("disabled", true);
	event.preventDefault();
	function_name = form.find("#function_name").find(":selected").val();
	location_type = form.find("#location_type").find(":selected").val();

	$("#try_it_form_error").hide()

	api_url = "https://api.example.com/v1/"
	api_url += function_name.toLowerCase() + "/" + location_type;
	documentation_url = "https://api.example.com/v1/#operation/"
	documentation_url += "get" + capitalize(location_type) + capitalize(function_name);
	$("a#documentation_link").attr['href'] = documentation_url;

	params = {}
	switch (location_type) {
		case "zip":
			zip = form.find("#zip").val();
			params = {"zip": zip};
		break;
		case "city":
			city = form.find("#city").val();
			state = form.find("#state").val();
			params = {"city": city, "state": state};
		break;
		case "state":
			state = form.find("#state").val();
			params = {"code": state};
		break;
		case "country":
			params = {"code": "US"};
		break;
	}

	$.getJSON(api_url, params )
	.done(function( json ) {
		pretty_json = JSON.stringify(json, null, 4);
		$("#json_output").html(pretty_json);
		$(".output").show();
		console.log(json)
		//console.log( "JSON Data: " + json );
		$("#try_api_submit").prop("disabled", false);
	})
	.fail(function( jqxhr, textStatus, error ) {
		$(".output").hide();
		var err = textStatus + ", " + error;
		console.log( "Request Failed: " + err );
		$("#try_api_submit").prop("disabled", false);
		$("#try_it_form_error").show()
	});
}


