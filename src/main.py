import json

with open("src\data.json", "r") as f:
    data = json.load(f)

def add_todo(field_info):
    todo = {"Name": field_info[0], "ID": field_info[1], "Task": field_info[2]}
    data["todos"].append(todo)

    with open("src\data.json", "w") as f:
        json.dump(data, f, indent=4)

def menu():
    while (user_choice := int(input(f"Select an option:\n1: Add a todo\n2: Remove a todo\n3: List all todos\n> "))) not in (1, 2, 3,):
        print(f"Unrecognized option: {user_choice}")
    
    if user_choice == 1:
        fields, field_info = ("Name", "ID", "Task"), []
        for field in fields:
            info = input(f"Enter the {field} for the task\n> ")
            field_info.append(info)
        
        add_todo(field_info) 
 
    elif user_choice == 2:
        print("coming soon")

    elif user_choice == 3:
        print("coming soon")

menu()