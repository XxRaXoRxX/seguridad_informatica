import re
from collections import Counter

def kasiski_method(cipher_text):
    # Paso 1: Encontrar las repeticiones de 3 o más caracteres
    pattern = r'(?=(\w{3,})).*?\1'
    repetitions = re.findall(pattern, cipher_text)

    # Paso 2: Calcular las distancias entre las repeticiones
    distances = [repetitions[i+1:].index(repetitions[i]) + len(repetitions[i])
                 for i, repetition in enumerate(repetitions[:-1])]
    
    # Paso 3: Encontrar los factores comunes de las distancias

        # Logica para el paso 3

    # Paso 4: Generar posibles longitudes de clave

        # Logica para el paso 4

    # Paso 5: Retornar las posibles longitudes de clave

        # Logica para el paso 5