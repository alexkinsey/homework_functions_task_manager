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

def tasks_greater_than_time(task_list, time):
    long_tasks = []
    for task in task_list:
        if task["time_taken"] <= time:
            long_tasks.append(task["description"])
    return long_tasks

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

def add_task(task_list, task_name, task_time):
    task_list.append({ "description": task_name, "completed": False, "time_taken": task_time })

def display_menu():
    print("\nMenu:")
    print("1: Display All Tasks")
    print("2: Display Uncompleted Tasks")
    print("3: Display Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")

running = True
display_menu()

while running:
    user_input = input("\nMake a selection: ")

    if user_input == "1":
        print(all_task_descriptions(tasks))
    elif user_input == "2":
        print(uncompleted_tasks(tasks))
    elif user_input == "3":
        print(completed_tasks(tasks))
    elif user_input == "4":
        mark_complete = input("Which task would you like to mark as complete?: ")
        mark_task_complete(tasks, mark_complete)
    elif user_input == "5":
        task_length = int(input("Type a time: "))
        print(tasks_greater_than_time(tasks, task_length))
    elif user_input == "6":
        task_name = input("Enter a task name for details: ")
        print(task_print_out(tasks, task_name))
    elif user_input == "7":
        task_name = input("Enter task name: ")
        task_time = input("How long with this take?: ")
        add_task(tasks, task_name, task_time)
    elif user_input == "m" or user_input == "M":
        display_menu()
    elif user_input == "q" or user_input == "Q":
        running = False
