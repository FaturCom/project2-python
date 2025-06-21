import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MESSAGE_FILE = os.path.join(BASE_DIR, "..", "Data", "message.json")

if not os.path.exists(MESSAGE_FILE):
    with open(MESSAGE_FILE, 'w') as file:
        json.dump([], file)

if os.stat(MESSAGE_FILE).st_size == 0:
    with open(MESSAGE_FILE, 'w') as file:
        json.dump([], file)

with open(MESSAGE_FILE, 'r' ) as file:
    data = json.load(file)

    if not isinstance(data, list):
        with open(MESSAGE_FILE, 'w' ) as file:
            json.dump([], file)

def load_message(user1:str, user2:str):
    with open(MESSAGE_FILE, 'r') as file:
        data = json.load(file)

        if len(data) > 0:
            for i in data:
                if user1 in i['user'] and user2 in i['user']:
                    return i['message']
    newChat = {
        "user" : [user1, user2],
        "message" : []
    }

    data.append(newChat)

    with open(MESSAGE_FILE, 'w') as file:
        json.dump(data, file)
    return "belum ada pesan"

def add_message(user1:str, user2:str, message:str):
    with open(MESSAGE_FILE, 'r') as file:
        data = json.load(file)

        if message != "":
            for i in data:
                    if user1 in i['user'] and user2 in i['user']:
                        i['message'].append(f"{user1}: {message}")
                        with open(MESSAGE_FILE, 'w') as file:
                            json.dump(data, file)
