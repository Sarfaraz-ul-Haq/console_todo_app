from typing import List
from typing_extensions import TypedDict

class ToDoItem(TypedDict):
    todo: str
    description: str
    is_completed: bool

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

def add_todo_item(todo_list: List[ToDoItem], todo: str, description: str) -> None:
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
        raise IndexError("Invalid todo index.")
        
def update_todo_item(index: int, todo_list: List[ToDoItem], todo: str, description: str) -> None:
    index -= 1

    if index >= 0 and index < len(todo_list):
        todo_list[index]["todo"] = todo
        todo_list[index]["description"] = description
    else:
        raise IndexError("Invalid index")
    
def mark_todo_as_done(index: int, todo_list: List[ToDoItem]) -> None:
    index -= 1

    if index >= 0 and index < len(todo_list):
            todo_list[index]["is_completed"] = True
            print("Todo marked as done")
    else:
        print("\nInvalid index")


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
            index: int = int(input("Enter todo number to update: "))
            new_todo: str = input("Update todo: ").strip()
            new_description: str = input("Update todo description: ").strip()
            update_todo_item(index, todo_list, new_todo, new_description)

        elif choice == "4":
            index: int = int(input("Enter index: "))
            mark_todo_as_done(index, todo_list)

        elif choice == "5":
            try:
                todo_number: int = int(input("Enter the number of the todo to delete: "))
                delete_todo_item(todo_number)
            except ValueError:
                print("\nInvalid input. Please enter a number.")

        elif choice == "6":
            print("Todo app closed")
            break

main()

