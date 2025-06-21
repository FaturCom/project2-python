import os
import sys
from Operations import user_handler as userHandler
from Operations import message_handler as messageHandler

if __name__ == "__main__":
    user = {}

    while True:
        os.system('clear')
        options = int(input( "="*10 + "Autentikasi" + 10*"=" +"\n1.Login\n2.Register\n3.Keluar\nmasukan opsi: "))
        
        match options:
            case 1 :
                print(  "\n" + 10*"=" + "LOGIN" + 10 * "=" + "\n")
                username = input("masukan username: ").strip()
                password = input("masukan password: ").strip()
                user = userHandler.user_login(username, password)
                
                if not user:
                    input("tekan enter untuk kembali ke menu...")
                else:
                    input('tekan enter untuk login ke akun...')
                    break

            case 2 :
                print( "\n" + 10*"=" + "REGISTER" + 10 * "=" + "\n")
                username = input("masukan username: ").strip()
                noHp = int(input("masukan nomor hp: "))
                password = input("masukan password: ").strip()
                confirm_password = input("konfirmasi password: ")

                if password == confirm_password:
                    print(userHandler.user_register(username, password, noHp))
                else:
                    print("password dan konfirmasi password harus sama")
                
                input('tekan enter untuk kembali ke menu...')
            case 3 : 
                print(userHandler.user_logout())
                print("program di hentikan")
                sys.exit(0)

            case _:
                print("opsi tidak ditemukan")
                input("tekan enter untuk kembali ke menu...")
        
    while user != {}:
        os.system('clear')
        print(f"NAMA : {user['username']}")
        print(f"NOMOR HP : {user['no_hp']}")

        print( 5*'\n' + '/exit untuk keluar, /contact untuk mencari nomor kontak')
        command = input('masukan commnad: ')

        match command:
            case '/exit':
                print(userHandler.user_logout())
                print('program dihentikan')
                sys.exit(0)

            case '/contact':
                os.system('clear')
                print(f"NAMA : {user['username']}")
                print(f"NOMOR HP : {user['no_hp']}")
                noHpTarget = int(input( 5 * "\n" + "masukan nomor hp yang ingin anda hubungi: "))

                result = userHandler.search_user(user, noHpTarget)
                
                if result:
                    message = messageHandler.load_message(user['username'], result['username'])

                elif result == None:
                    message = False
                    print("nomor hp tidak ditemukan")
                    input("tekan enter untuk kembali ke menu...")

                if message  or message == []:
                    while message or message == []:
                        os.system('clear')
                        print (15 * "=" + f" chat {user['username']} dan {result['username']} " + "=" * 15 + "\n")
                        message = messageHandler.load_message(user['username'], result['username'])
                        for msg in message:
                            print(f"{msg}\n")

                        input_message = input("\n\n(tekan enter untuk melihat/back untuk kembali ke menu)\nmasukan pesan: ")

                        if input_message == "/back" or message == "/exit":
                            break

                        messageHandler.add_message(user['username'], result['username'], input_message)

            case _ :
                print("command tidak ditemukan")
                input("tekan enter untuk kembali ke menu...")