from random import randrange
import math

# Verificar se um número n é primo ou não
def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

# Gera um número primo aleatório entre 10^min_pot e 10^max_pot
def generate_prime(min_pot, max_pot):
    rnd_prime = randrange(10**min_pot, 10**max_pot)
    # Gera números aleatórios entre 10^2 e 10^5 até que o número gerado seja um número primo
    while not is_prime(rnd_prime):
        rnd_prime = randrange(10**min_pot, 10**max_pot)
    return rnd_prime

def generate_list(np, min, max):
    p = []

    while len(p) < np:
        prime = generate_prime(min, max)
        while prime in p:
            prime = generate_prime(min, max)
        p.append(prime)

    return p
