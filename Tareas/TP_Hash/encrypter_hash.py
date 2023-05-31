import hashlib

def hash_string(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

mensaje_original = "mensaje secreto"
mensaje_recibido = input("Introduce el mensaje recibido: ")
hash_recibido = hash_string(mensaje_recibido)
hash_original = hash_string(mensaje_original)

if hash_recibido == hash_original:
    print("El mensaje NO ha sido modificado.")
else:
    print("El mensaje SI ha sido modificado.")

print(hash_recibido)
print(hash_original)