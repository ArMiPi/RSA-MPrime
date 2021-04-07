from math import gcd
from random import randrange

# Calcula o valor de N
# Entrada: p -> lista contendo números primos
#Saída: N -> inteiro -> produto de todos os primos em p
def calc_N(p):
    N = 1

    for prime in p:
        N *= prime
    
    return N

# Calcula o valor de φ(N)
# Entrada: p -> lista contendo números primos
# Saída: phiN -> inteiro -> produto de todos os primos da lista, sendo que de cada elemento é decrementado de 1
def calc_phiN(p):
    phiN = 1

    for prime in p:
        phiN *= (prime - 1)

    return phiN

# Retorna o valor de e
# Entrada: φ(N) -> inteiro
# Saída: e -> inteiro -> inteiro coprimo de φ(N)
def get_e(phiN):
    #e = randrange(2, 10**5)
    #while gcd(e, phiN) != 1:
    #    e = randrange(2, 10**5)
    #return e
    for e in range(2, phiN):
        if gcd(e, phiN) == 1:
            return e
    #return 65537

def calc_d(e, phiN):
    return pow(e, -1, phiN)

def print_keys(N, e, d):
    CPb = "Pública: <{}, {}>"
    CPv = "Privada: <{}, {}>"

    print()
    print("Chaves: ")
    print("="*50)
    print(CPb.format(N, e))
    print(CPv.format(N, d))
    print("="*50)
    print()