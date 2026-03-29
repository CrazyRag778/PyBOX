import json
import os

BASE_DIR = os.getcwd()
SYSTEM_JSON_PATH = os.path.join(BASE_DIR, "imp", "system.json")

with open(SYSTEM_JSON_PATH, "r+") as SYSTEM_INFO:
    SYSTEM_INFO_JSON = json.loads(SYSTEM_INFO.read())

HOSTNAME = SYSTEM_INFO_JSON['HOSTNAME']

PYOS_ASCII_ART = f'''
██████╗ ██╗   ██╗ ██████╗ ███████╗  HOSTNAME: {HOSTNAME}
██╔══██╗╚██╗ ██╔╝██╔═══██╗██╔════╝  
██████╔╝ ╚████╔╝ ██║   ██║███████╗
██╔═══╝   ╚██╔╝  ██║   ██║╚════██║
██║        ██║   ╚██████╔╝███████║
╚═╝        ╚═╝    ╚═════╝ ╚══════╝
(Power . Your . OS)
'''

print(PYOS_ASCII_ART)