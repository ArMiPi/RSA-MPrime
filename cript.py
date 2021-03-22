# Retorna uma lista, sendo cada elemento da lista o correspondente em ASCII de cada char da string
def str_to_int(txt):
    l = []                                  # Inicia uma lista vazia

    for c in txt:                           # Percorre a string elemento a elemento
        l.append(ord(c))                    # Preenche a lista
    
    return l                                # Retorna a lista criada

# Recebe uma lista com valores em ASCII e retorna a string correspondente a esses valores
def int_to_str(l):
    text = ""                               # Inicia uma string vazia

    for asc in l:                           # Percorre todos os elementos da lista
        text += chr(asc)

    return text                             # Retorna a string criada

def criptografar(x, e, N):
    return (x**e) % N

def cript_msg(M, e, N):
    lM = str_to_int(M)                      # Representação ASCII de M
    
    c = []
    for el in lM:
        c.append(criptografar(el, e, N))    # Criptografar cada elemento de lM

    return c

def descriptografar(p1, p2, p3, C, d):
    #Redução modular de d
    d1 = d % (p1 - 1)
    d2 = d % (p2 - 1)
    d3 = d % (p3 - 1)

    # Calcular os Mi
    M1 = (C**d1) % p1
    M2 = (C**d2) % p2
    M3 = (C**d3) % p3

    Ml = (M1 * p2 * pow(p2, -1, p1) + M2 * p1 * pow(p1, -1, p2)) % (p1 * p2)

    M = ( Ml * p3 * pow(p3, -1, p1*p2) + M3 * (p1 * p2) * pow(p1 * p2, -1, p3) ) % (p1 * p2 * p3)

    return M

def descript_msg(p1, p2, p3, C, d):
    dl = []
    for el in C:
        dl.append(descriptografar(p1, p2, p3, el, d))

    Dm = int_to_str(dl)

    return Dm