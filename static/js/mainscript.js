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
	
	
	
	$(document).on('click', '#completed_filter', function(){
		
		var checkBox = document.getElementById("completed_filter");
		console.log('ds')
		// Get the output text
		var complete_tasks = document.getElementsByClassName("completed");
		console.log('ds')
		// If the checkbox is checked, display the output text
		if (checkBox.checked == true){
			for (let i = 0; i < complete_tasks.length ; i++ ){
				complete_tasks[i].style.display = 'none';
			}
		} 
		else {
			for (let i = 0; i < complete_tasks.length ; i++ ){
				complete_tasks[i].style.display = 'block';
			}
		}
	
	})
	
	$(document).on('click', '#priority_filter', function(){
		var ulTasks = document.getElementById("todo-list")
		var liTasks = ulTasks.getElementsByTagName('li')
		let liEasyTasks = []
		let liMediumTasks = []
		let liHighTasks = []
		let liCompleteTasks = []
		for (let i = 0; i < liTasks.length; i++)
		{
			if($(liTasks[i]).attr('class') == "completed"){
				liCompleteTasks.push(liTasks[i])
			} else
			{
				spanTask = liTasks[i].getElementsByTagName('span')
				if($(spanTask[0]).is('.badge-danger')){
					liHighTasks.push(liTasks[i])
				}
				else if($(spanTask[0]).is('.badge-secondary')){
					liMediumTasks.push($(liTasks[i]))
				}
				else if($(spanTask[0]).is('.badge-success')){
					liEasyTasks.push($(liTasks[i]))
				}
			}
		}
		$(ulTasks).empty()
		$(ulTasks).append(liHighTasks)
		$(ulTasks).append(liMediumTasks)
		$(ulTasks).append(liEasyTasks)
		$(ulTasks).append(liCompleteTasks)
		var checkBox = document.getElementById("priority_filter");
		if (checkBox.checked == false)
		{
			$(ulTasks).children().each(function(i,li){ulTasks.prepend(li)})
		}
	});

});
