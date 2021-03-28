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

def char_cript(C):
    Mct = ""
    for el in C:
        Mct += chr(el % 127)
    
    return Mct

def descriptografar(p, C, d):
    M1 = (C ** (d % (p[0] - 1))) % p[0]
    M2 = (C ** (d % (p[1] - 1))) % p[1]

    pm = p[0] * p[1]

    M = ((M1 * p[1] * pow(p[1], -1, p[0])) + (M2 * p[0] * pow(p[0], -1, p[1]))) % pm

    dx = 0
    Mx = ""
    for x in range(2, len(p)):
        dx = d % (p[x] - 1)
        Mx = (C ** dx) % p[x]
        M = ((M * p[x] * pow(p[x], -1, pm)) + (Mx * pm * pow(pm, -1, p[x]))) % (pm * p[x])
        pm *= p[x]
    
    return M

def descript_msg(p, C, d):
    dl = []
    for el in C:
        dl.append(descriptografar(p, el, d))

    Dm = int_to_str(dl) # Transforma a lista de inteiros em uma string

    return Dm