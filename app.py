# from typing import Any, List, Dict, Union

# todo_list: List[Dict[str, Union[str, bool]]] = []

# while True:
#     todo: str = input("Enter a todo or exit: ")

#     if todo.lower() == "exit":
#         break

#     if todo.strip() == "":
#         print("Please enter a todo: ")
#         continue

#     for todo_dict in todo_list:
#         if todo_dict["todo"] == todo:
#             add = input("Duplicate todo! Do you still want to add it? (yes / no)")
#             if add.lower() == "no":
#                 break
#     else:
#         todo_list.append({"todo": todo, "completed": False})


# print(todo_list)
# _____________________________________________________________

from typing import List, Tuple

ToDoItem = Tuple[str, bool]

todo_list: List[ToDoItem] = [
    ("Learn Generative AI Fundamentals", "Pending"),
    ("Learn LangChain", "Pending"),
]


def display_todos(todo_list: List[ToDoItem]) -> None:
    if not todo_list:
        print("Your To-Do list is empty!")
        return

    print(f"\nHere is your todo list:\n")
    for id, (todo, is_completed) in enumerate(todo_list, start=1):
        if is_completed:
            status: str = "Done"
        else:
            status: str = "Pending"

        print(f"{id}. {todo} - [{status}]")


display_todos(todo_list)
