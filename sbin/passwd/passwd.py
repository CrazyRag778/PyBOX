import sys
import os
import json

s_args = sys.argv
if len(s_args) < 2:
    print("usage: passwd <new_password>")
    sys.exit(1)

new_password = s_args[1]

# Base project root — cwd is always PYOS/ when called from shell.py
BASE_DIR = os.getcwd()

# Absolute path to system config
SYSTEM_JSON_PATH = os.path.join(BASE_DIR, "imp", "system.json")

# Read current system info
with open(SYSTEM_JSON_PATH, "r") as SYSTEM_INFO:
    SYSTEM_INFO_JSON = json.load(SYSTEM_INFO)

# If password is still default, change without verification
if SYSTEM_INFO_JSON["password"] == "root":
    SYSTEM_INFO_JSON["password"] = new_password
else:
    # Ask for current password to verify identity
    current_password = input("Current password: ")
    if current_password != SYSTEM_INFO_JSON["password"]:
        print("passwd: incorrect password")
        sys.exit(1)
    SYSTEM_INFO_JSON["password"] = new_password

# Overwrite file with updated data
with open(SYSTEM_JSON_PATH, "w") as SYSTEM_INFO:
    json.dump(SYSTEM_INFO_JSON, SYSTEM_INFO, indent=4)

print("passwd: password updated successfully")