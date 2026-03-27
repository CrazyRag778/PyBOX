import json
import sys

USER_REGISTER = open("../../users/register.json", "r+")
USER_REGISTER_DATA = USER_REGISTER.read()
USER_REGISTER_JSON = json.loads(USER_REGISTER_DATA)


# print(USER_REGISTER_JSON)


def print_user_register():
    print("USERNAME      PASSWORD")
    i = 0
    for username, data in USER_REGISTER_JSON.items():
        i += 1
        print(f"{i}. {username}          {data['password']}")


def add_user(username, password):
    if username in USER_REGISTER_JSON:
        print("User already exists")
        exit(1)
    USER_REGISTER_JSON[username] = {"password": password}
    with open("../../users/register.json", "w") as f:
        json.dump(USER_REGISTER_JSON, f, indent=4)


def delete_user(username):
    if username not in USER_REGISTER_JSON:
        print("User does not exist")
        exit(1)
    del USER_REGISTER_JSON[username]
    with open("../../users/register.json", "w") as f:
        json.dump(USER_REGISTER_JSON, f, indent=4)


exec_args = sys.argv

if exec_args[1] == "list":
    print_user_register()
elif exec_args[1] == "add":
    add_user(exec_args[2], exec_args[3])
elif exec_args[1] == "delete":
    delete_user(exec_args[2])
else:
    print("Invalid command")
