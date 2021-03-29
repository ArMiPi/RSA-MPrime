from random import randrange
import math

# Verificar se um número n é primo ou não
#Entrada: n -> inteiro
#Saída: True  -> Caso n seja um número primo
#       False -> Caso n não seja um número primo
def is_prime(n):
    if n <= 0:
        return False
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

# Gera um número primo aleatório entre 10^min_pot e 10^max_pot
# Entradas: min_pot -> inteiro positivo -> indica o menor valor para a geração de números primos (10**min)
#           max_pot -> inteiro positivo -> indica o maior valor para a geração de números primos (10**max)
#           Condição: min_pot < max_pot
# Saída: rnd_prime -> 10**min_pot <= rnd_prime < 10**max_pot -> número primo
def generate_prime(min_pot, max_pot):
    rnd_prime = randrange(10**min_pot, 10**max_pot)
    # Gera números aleatórios entre 10^min_pot e 10^max_pot até que o número gerado seja um número primo
    while not is_prime(rnd_prime):
        rnd_prime = randrange(10**min_pot, 10**max_pot)
    return rnd_prime

# Gera uma lista com np primos aleatórios
# Entradas: np  -> inteiro positivo -> tamanho da lista
#           min -> inteiro positivo -> indica o menor valor para a geração de números primos (10**min)
#           max -> inteiro positivo -> indica o maior valor para a geração de números primos (10**max)
#           Condição: min < max
# Saída: p -> lista de números primos
def generate_list(np, min, max):
    p = []

    while len(p) < np:
        prime = generate_prime(min, max)
        while prime in p:
            prime = generate_prime(min, max)
        p.append(prime)

    return p
