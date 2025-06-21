import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(BASE_DIR, "..","Data", "users.json")
current_user = {}

print(os.path.exists('../Data/message.json'))
print(USER_FILE)

if not os.path.exists(USER_FILE):
    with open(USER_FILE, 'w') as file:
        json.dump([], file)

if os.stat(USER_FILE).st_size == 0:
    with open(USER_FILE, 'w') as file:
        json.dump([], file)

with open(USER_FILE, 'r') as file:
    data = json.load(file)

    if not isinstance(data, list):
        with open(USER_FILE, 'w') as file:
            json.dump([], file)
    else:
        print("file dan array kosong sudah dibuat")

def user_login(username:str, password:str):
    global current_user
    with open(USER_FILE, 'r') as file:
        user = ''
        data = json.load(file)

        for u in data:
            if u["username"] == username:
                if u["password"] == password:
                    user = u
                else:
                    print("Password salah")
                    return False
        
        if user == '':
            print("username tidak ditemukan")
            return False
        else :
            for u in data:
                if u['username'] == user['username']:
                    u['is_login'] = True
                    current_user = u.copy()

            with open(USER_FILE, 'w') as file:
                json.dump(data, file)

                return current_user
            
def user_register(username:str, password:str, noHp:int) -> str:
    newUser = {
        "username" : username,
        "password" : password,
        "no_hp" : noHp,
        "is_login" : False
    }
    
    print(newUser)

    if len(newUser['username']) <= 3:
        return "username harus lebih dari 3 karakter"
    
    if len(str(newUser['no_hp'])) <= 5:
        return "nomor hp harus lebih dari 5 digit"

    if len(newUser['password']) <=5:
        return "password harus lebih dari 5 karakter"

    with open(USER_FILE, 'r') as file :
        data = json.load(file)

        for u in data:
            if u["username"] == newUser["username"]:
                return f"username {newUser['username']} sudah di gunakan"
            if u["no_hp"] == newUser["no_hp"] :
                return "nomor hp sudah terdaftar"
    
        with open(USER_FILE, 'w') as file:
            data.append(newUser)
            json.dump(data, file)
            return "akun berhasil dibuat"

def search_user(user:dict, no_hp:int):
    if user['no_hp'] != no_hp:
        with open(USER_FILE, 'r') as file:
            data = json.load(file)

            for u in data:
                if u['no_hp'] == user['no_hp']:
                    continue

                if u['no_hp'] == no_hp:
                    return u
                    
def user_logout():
    global current_user

    if current_user != {}:
        with open(USER_FILE, 'r') as file:
            data = json.load(file)

            for u in data:
                if u['username'] == current_user['username']:
                    u['is_login'] = False
                    current_user = {}
                    with open(USER_FILE, 'w') as file:
                        json.dump(data, file)
                        return "user berhasil logout"
                    
    return "terjadi kesalahan"