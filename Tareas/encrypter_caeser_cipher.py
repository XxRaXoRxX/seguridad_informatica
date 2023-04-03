'''Este es un simple ejemplo de como cifrar un mensaje usando la libreria cryptography
basado en el cifrado de Cesar utilizando una clave de la secuencia Fibonacci.'''

def main():
    # Pedir al usuario que ingrese un numero de inicio para la secuencia
    start = int(input("Enter a number to start the sequence: "))

    # Pedir al usuario que ingrese la cantidad de elementos que desea en la secuencia
    length = int(input("Enter the length of the sequence: "))

    # Llamar a la funcion para generar la secuencia Fibonacci
    fibonacci = generate_fibonacci(start, length)

    # Usar el ultimo numero de la secuencia como clave de cifrado para el mensaje
    key = fibonacci[-1]

    # Pedir al usuario que ingrese un mensaje para cifrar
    message = input("Enter a message to encrypt: ")

    # Llamar a la funcion para cifrar el mensaje usando la clave de cifrado generada
    encrypted_message = encrypt_message(message, key)
    # Mostrar el mensaje cifrado y la clave de cifrado generada
    print("Encrypted message:", encrypted_message)
    print("Encryption key:", key)


# Funcion para generar la secuencia Fibonacci
def generate_fibonacci(start, length):
    # Generar la secuencia Fibonacci
    fibonacci = [start]
    a, b = 0, 1
    for i in range(length):
        a, b = b, a + b
        fibonacci.append(b)
    return fibonacci

def encrypt_message(message, key):
    # Cifrar el mensaje usando la clave de cifrado generada
    encrypted_message = ""
    for letter in message:
        if letter.isalpha():
            code = ord(letter) + key % 26
            encrypted_letter = chr(code)
            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter
    return encrypted_message


if __name__ == "__main__":
    # Ejecutar la funcion main() solo si este archivo es ejecutado directamente
    main()