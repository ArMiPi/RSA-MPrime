from random import randrange
import math

class GeneratePrime:
    def __init__(self, min_pot, max_pot):
        self.rnd_prime = self.generate_prime(min_pot, max_pot)
        self.min_pot = min_pot
        self.max_pot = max_pot
    
    # Verificar se um número n é primo ou não
    def is_prime(self, n):
        if n == 1:
            return False
        if n % 2 == 0:
            return False
        for x in range(3, int(math.sqrt(n)) + 1, 2):
            if n % x == 0:
                return False
        return True

    # Gera um número primo aleatório entre 10^2 e 10^5
    def generate_prime(self, min_pot, max_pot):
        self.rnd_prime = randrange(10**min_pot, 10**max_pot)
        # Gera números aleatórios entre 10^2 e 10^5 até que o número gerado seja um número primo
        while not self.is_prime(self.rnd_prime):
            self.rnd_prime = randrange(10**min_pot, 10**max_pot)
        return self.rnd_prime
