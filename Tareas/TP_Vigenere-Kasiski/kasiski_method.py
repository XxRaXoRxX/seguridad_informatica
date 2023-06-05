import re
import math

def kasiski_method(cipher_text):
    # Paso 1: Encontrar las repeticiones de 4 o más caracteres
    pattern = r'(?=(\w{3,})).*?\1'
    repetitions = re.findall(pattern, cipher_text)

    # Paso 2: Calcular las distancias entre las repeticiones
    distances = [repetitions[i+1:].index(repetition) + len(repetition)
                 for i, repetition in enumerate(repetitions[:-1])]
    positions = [m.start() for m in re.finditer(pattern, cipher_text)]
    distances = [positions[i+1] - positions[i] for i in range(len(positions)-1)]

    # Paso 3: Encontrar los factores comunes de las distancias
    factors = []
    for i in range(len(distances)):
        for j in range(i+1, len(distances)):
            factor = math.gcd(distances[i], distances[j])
            if factor > 1:
                factors.append(factor)

    # Paso 4: Generar posibles longitudes de clave
    possible_lengths = []
    for factor in factors:
        for i in range(2, factor):
            if factor % i == 0 and i not in possible_lengths:
                possible_lengths.append(i)

    # Paso 5: Retornar las posibles longitudes de clave
    return possible_lengths

def main():
    print(kasiski_method("HOLA MUNDO"))

if __name__ == "__main__":
    main()