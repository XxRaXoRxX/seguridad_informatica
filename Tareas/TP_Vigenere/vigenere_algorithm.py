import string

def main():
    alphabet = string.ascii_uppercase

    # Pedimos la clave
    key = input("Ingrese la clave: ")

    # Pedimos el texto a cifrar
    text = input("Ingrese texto: ")

    while True:
        # Indicamos si queremos cifrar o descifrar
        option = input("Ingrese 1 para cifrar o 2 para descifrar: ")

        # Ciframos o desciframos el texto
        if option == "1" or option == "2":
            result = operate(text, key, alphabet, option)
            if option == "1":
                print("Texto cifrado: " + result)
            elif option == "2":
                print("Texto descifrado: " + result)
            break
        else:
            print("Opción incorrecta")

def operate(text, key, alphabet, option):
    # Definimos la lista de caracteres
    char_list = []

    # Definimos el indice de la clave
    ind = 0

    # Pasamos la clave a mayusculas
    key = key.upper()

    # Recorremos el texto
    for symbol in text:
        # Obtenemos el indice de la letra
        num = alphabet.find(symbol.upper())

        if num != -1:
            if option == "1":
                # Sumamos el indice de la clave
                num += alphabet.find(key[ind])
            elif option == "2":
                # Restamos el indice de la clave
                num -= alphabet.find(key[ind])

            # Obtenemos el indice de la letra en el alfabeto
            num %= len(alphabet)

            # Agregamos la letra a la lista
            if symbol.isupper():
                char_list.append(alphabet[num])
            elif symbol.islower():
                char_list.append(alphabet[num].lower())

            # Incrementamos el indice de la clave
            ind += 1

            # Si el indice es igual a la longitud de la clave, lo reiniciamos
            if ind == len(key):
                ind = 0
        else:
            char_list.append(symbol)

    # Retornamos un join de la lista para obtener el texto cifrado
    return "".join(char_list)

if __name__ == "__main__":
    main()