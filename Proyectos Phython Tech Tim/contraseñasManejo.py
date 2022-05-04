from cryptography.fernet import Fernet



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("¿whats the master password? ")
key = load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
# pwd es contraseña en ingles
    #la a es el modo en el que se habre el archivo (pluma; permite escribir al final), f es el nombre 
    #la /n sirve apra que el editor de texto baje a la siguiente linea cuando se agregue texto

 #continue nos permite volver al principio del if con un bucle, ideal cuando el usuario pone algo invalido y hay que volver a empezar

 # aunque el programa no funcione nos eseña a que se pueden abrir archivos desde phython y manejarlo
 #estos archivos simepre hay que cerrarlos y tienen fiormas de abrirse que hay que indicar
 #como por ejemplo de solo lectura, leer en bytes, solo agregar texto al final o libre
 #o indicar cuando se cierra con una condicion de un if como por ejemplo cn las contraseñas
