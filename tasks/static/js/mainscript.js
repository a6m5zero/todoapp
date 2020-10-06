$(document).ready(function() {
	$(document).on('click', '.remove', function(){
		console.log('ds')
		$(this).parent().remove();
	})

	$(document).on('click', '.checkbox', function(){
		$(this).parent().addClass('completed');
		$(this).attr('disabled', true);

		uid = $(this).attr('data-uid');
		$.get("/tasks/complete/" + uid);
	})
	$("#filter").click(function($) {
		$("#filter_d").append("<input class='checkbox' id ='completed_fl' type='checkbox' />")
	});
})