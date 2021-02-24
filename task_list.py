tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

def uncompleted_tasks(tasks_list):
    uncompleted_tasks = []
    for task in tasks_list:
        if not task["completed"]:
            uncompleted_tasks.append(task["description"])
    return uncompleted_tasks

def completed_tasks(tasks_list):
    completed_tasks = []
    for task in tasks_list:
        if task["completed"]:
            completed_tasks.append(task["description"])
    return completed_tasks

def all_task_descriptions(tasks_list):
    task_descriptions = []
    for task in tasks_list:
        task_descriptions.append(task["description"])
    return task_descriptions

def tasks_less_than_time(task_list, time):
    short_tasks = []
    for task in task_list:
        if task["time_taken"] <= time:
            short_tasks.append(task["description"])
    return short_tasks

def task_print_out(task_list, task_name):
    full_task = "Task not found."
    for task in task_list:
        if task["description"] == task_name:
            full_task = task
            break
    return full_task

def mark_task_complete(task_list, task_name):
    count = 0
    for task in task_list:
        if task["description"] == task_name:
            task_list[count]["completed"] = True
        count += 1
    return 

def add_task(task_list, task_name, task_complete, task_time):
    task_list.append({ "description": task_name, "completed": task_complete, "time_taken": task_time })
    return

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
