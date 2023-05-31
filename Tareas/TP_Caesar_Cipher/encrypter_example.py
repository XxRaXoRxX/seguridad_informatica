from cryptography.fernet import Fernet

'''Este es un simple ejemplo de como cifrar un mensaje usando la libreria cryptography'''

def main():
    # Pedir al usuario que ingrese un mensaje para cifrar
    msg = input("Enter a message to encrypt: ")

    # Generar una key de cifrado
    key = Fernet.generate_key()
    encrypted_msg = encrypt_message(msg, key)
    
    # Mostrar el mensaje cifrado y la clave de cifrado generada
    print("Encrypted message:", encrypted_msg)
    print("Encryption key:", key)

def encrypt_message(msg, key):
    # Crear un objeto Fernet usando la clave de cifrado
    f = Fernet(key)

    # Convertir el mensaje a bytes
    msg_bytes = msg.encode()

    # Cifrar el mensaje usando la clave de cifrado generada
    encrypted_msg = f.encrypt(msg_bytes)

    return encrypted_msg

if __name__ == "__main__":
    # Ejecutar la funcion main() solo si este archivo es ejecutado directamente
    main()