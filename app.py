from typing import List, Dict, Union

ToDoItem = Dict[str, Union[str, bool]]

todo_list: List[ToDoItem] = [
    {
        "todo": "Learn GenAI",
        "description": "Learn about neural network and transformers",
        "is_completed": False,
    },
    {
        "todo": "Mart Project",
        "description": "Make ai-powered cloud native microsevices mart apis",
        "is_completed": False,
    },
]

def display_todo_list(todo_list: List[ToDoItem]) -> None:
    if not todo_list:
        print("Your Todo list is empty!")
        return
    
    print(f"Here is your todo list:\n")
    for id, todo_item in enumerate(todo_list, start=1):
        if todo_item["is_completed"]:
            status: str = "Done"
        else:
            status: str = "Pending"

        print(f"{id}. Todo: {todo_item["todo"]} - Description: {todo_item["description"]} - [{status}]")

    print("_________________________________________________________________________________________________________\n")



def add_todo_item(to_do_list: List[ToDoItem], todo: str, description: str) -> None:
    todo_list.append({"todo": todo, "description": description, "is_completed": False})
    print(f"\nAdded todo: {todo} | Description: {description}")


def get_task_number(action: str) -> int:
    display_todo_list(todo_list)

    while True:
        try:
            task_number: int = int(input(f"\nEnter the task number to {action}: "))
            return task_number
        except ValueError:
            print("\n Invalid input. Please enter a valid number.")

def delete_todo_item(index: int) -> None:
    index -= 1
    if index >= 0 and index < len(todo_list):
        todo_list.pop(index)
        print("\nTodo deleted successfully")
    else:
        print("\nInvalid  todo number. Please try again.")


    
# add_todo(todo_list, "Learn Transformers")

# display_todos(todo_list)


def main() -> None:
    while True:
        print("\nTodo List Options:")
        print("==================\n")
        print("1. Display todo list")
        print("2. Add a todo")
        print("3. Update todo")
        print("4. Mark todo as done")
        print("5. Delete todo")
        print("6. Exit")

        choice: str = input("\nEnter your choice: ")

        if choice == "1":
            display_todo_list(todo_list)

        elif choice == "2":
            todo: str = input("Enter your todo: ").strip()
            description: str = input("Enter todo description: ").strip()

            if todo != "" and description != "":
                add_todo_item(todo_list, todo, description)
            else:
                print("Todo / description cannot be empty!\n")

        elif choice == "3":
            pass

        elif choice == "4":
            pass

        elif choice == "5":
            try:
                todo_number: int = int(input("Enter the number of the todo to delete: "))
                delete_todo_item(todo_number)
            except ValueError:
                print("\nInvalid input. Please enter a number.")

        elif choice == "6":
            pass


main()
