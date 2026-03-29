import json
import os
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SYSTEM_INFO = json.load(open(os.path.join(BASE_DIR, "imp", "system.json")))
HOSTNAME = SYSTEM_INFO["HOSTNAME"]


def REBASE_SYSTEM_BIN():
    global SYSTEM_APP_REGISTER
    global SYSTEM_APP_REGISTER_LIST
    global APP_REGISTER
    global APP_REGISTER_LIST

    SYSTEM_APP_REGISTER = json.load(open(os.path.join(BASE_DIR, "sbin", "register.json")))
    SYSTEM_APP_REGISTER_LIST = list(SYSTEM_APP_REGISTER.keys())

    APP_REGISTER = json.load(open(os.path.join(BASE_DIR, "bin", "register.json")))
    APP_REGISTER_LIST = list(APP_REGISTER.keys())

REBASE_SYSTEM_BIN()

print(APP_REGISTER_LIST)

PROMPT = f"system@{HOSTNAME}$ "
PWD = "home"

# DEBUG
# print(PWD)
# print(PROMPT)
# print(SYSTEM_APP_REGISTER_LIST)

open(os.path.join(BASE_DIR, "ENV", ".system.json"), "a")


# SYSTEM STARTUP
def start_system():
    with open(os.path.join(BASE_DIR, "ENV", ".system.json"), "r") as f:
        shell = json.load(f)
    shell["turned_on"] = True
    with open(os.path.join(BASE_DIR, "ENV", ".system.json"), "w") as f:
        json.dump(shell, f, indent=4)


def stop_system():
    with open(os.path.join(BASE_DIR, "ENV", ".system.json"), "r") as f:
        shell = json.load(f)
    shell["turned_on"] = False
    with open(os.path.join(BASE_DIR, "ENV", ".system.json"), "w") as f:
        json.dump(shell, f, indent=4)
    exit(0)


# FILE MANAGEMENT
def make_dir(name):
    os.mkdir(os.path.join(BASE_DIR, PWD, name))


start_system()

while True:
    cmd = input(f"[{PWD}] " + PROMPT)
    cmd = cmd.split(" ")
    if cmd[0] == "killself":
        exit(0)
    elif cmd[0] == "shutdown":
        stop_system()
    elif cmd[0] == "clear":
        subprocess.run("clear", shell=True)

    # BINARY EXECUTION    
    elif cmd[0] in SYSTEM_APP_REGISTER_LIST:
        cmd[0] = os.path.join(BASE_DIR, "sbin", cmd[0], cmd[0] + ".py")
        cmd = " ".join(["python3", *cmd])
        result = subprocess.run(cmd, shell=True)
    elif cmd[0] in APP_REGISTER_LIST:
        cmd[0] = os.path.join(BASE_DIR, "bin", cmd[0], cmd[0] + ".py")
        cmd = " ".join(["python3", *cmd])
        result = subprocess.run(cmd, shell=True)

    # Reinitialise system variables
    elif cmd[0] == "rebase":
        # SYSTEM BIN REGISTERS
        if cmd[1] == "system/bin":
            REBASE_SYSTEM_BIN()

    elif cmd[0] == "mkdir":
        make_dir(cmd[1])
    else:
        cmd = " ".join(cmd)
        print(f"shell: command not found: {cmd}")
