# To-Do List in Python

# Initialize an empty to-do list
todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the task to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added!")

def update_task():
    view_tasks()
    if todo_list:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(todo_list):
            updated_task = input("Enter the new task: ")
            todo_list[task_num - 1] = updated_task
            print(f"Task {task_num} updated to '{updated_task}'")
        else:
            print("Invalid task number!")

def delete_task():
    view_tasks()
    if todo_list:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task}' deleted!")
        else:
            print("Invalid task number!")

def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
