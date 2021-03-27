from math import gcd
# from random import randrange

def calc_N(p):
    N = 1

    for prime in p:
        N *= prime
    
    return N

def calc_phiN(p):
    phiN = 1

    for prime in p:
        phiN *= (prime - 1)

    return phiN

def get_e(phiN):
    # e = randrange(1, phiN)
    # while gcd(e, phiN) != 1:
    #    e = randrange(1, phiN)
    # return e
    return 65537

def calc_d(e, phiN):
    return pow(e, -1, phiN)