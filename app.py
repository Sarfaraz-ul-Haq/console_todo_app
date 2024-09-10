from typing import Any, List, Dict, Union

todo_list: List[Dict[str, Union[str, bool]]] = []

while True:
    todo: str = input("Enter a todo or exit: ")

    if todo.lower() == "exit":
        break

    if todo.strip() == "":
        print("Please enter a todo: ")
        continue

    for todo_dict in todo_list:
        if todo_dict["todo"] == todo:
            add = input("Duplicate todo! Do you still want to add it? (yes / no)")
            if add.lower() == "no":
                break
    else:
        todo_list.append({"todo": todo, "completed": False})


print(todo_list)
