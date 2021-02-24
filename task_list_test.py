# the following lines were used previously for testing

print("\n")
print(f"Today's tasks are: {all_task_descriptions(tasks)}")
print(f"Uncompleted tasks: {uncompleted_tasks(tasks)}")
print(f"Completed tasks: {completed_tasks(tasks)}")
print("\n")

# adjust task time to fetch different tasks from list
task_time = 10
print(f"ALL short tasks ({task_time} minutes or less): {tasks_less_than_time(tasks, task_time)}")
print("\n")

# set a task name to see full details
task = "Make Dinner"
print(f"{task} detail: {task_print_out(tasks, task)}")
print("\n")

# mark task as complete
task_complete = "Feed Cat"
mark_task_complete(tasks, task_complete)
print(f"Marked {task_complete} as complete.")
print(f"Uncompleted tasks: {uncompleted_tasks(tasks)}")
print("\n")

# add extra task
print("Adding 'Have Bath' to task list")
add_task(tasks, "Have Bath", False, 45)
print(f"Today's tasks are: {all_task_descriptions(tasks)}")
