from typing import Any, List, Dict, Union

# List[Dict[str, Union[str, bool]]]

todo_list = []

while True:
    todo = input("Enter a todo or exit: ")

    if todo.lower() == "exit":
        break
    else:
        todo_list.append({"todo": todo, "completed": False})

print(todo_list)
