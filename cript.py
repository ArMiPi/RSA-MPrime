# Retorna uma lista, sendo cada elemento da lista o correspondente em ASCII de cada char da string
# Entrada: txt -> string
# Saída: l -> lista de inteiros
def str_to_int(txt):
    l = []                                  # Inicia uma lista vazia

    for c in txt:                           # Percorre a string elemento a elemento
        l.append(ord(c))                    # Preenche a lista
    
    return l                                # Retorna a lista criada

# Recebe uma lista com valores em ASCII e retorna a string correspondente a esses valores
# Entrada: l -> lista de inteiros correspondentes aos códigos da tabela ASCII
# Saída: text -> string
def int_to_str(l):
    text = ""                               # Inicia uma string vazia

    for asc in l:                           # Percorre todos os elementos da lista
        text += chr(asc)

    return text                             # Retorna a string criada

# Realiza a criptografia da mensagem
#Entradas: x -> inteiro
#          e -> inteiro
#          N -> inteiro
# Saída: (x**e) % N -> inteiro
def criptografar(x, e, N):
    return (x**e) % N

# Retorna uma lista contendo a mensagem criptografada
# Entradas: M -> string
#           e -> inteiro
#           N -> inteiro
# Saída: c -> lista
def cript_msg(M, e, N):
    lM = str_to_int(M)                      # Representação ASCII de M
    
    c = []
    for el in lM:
        c.append(criptografar(el, e, N))    # Criptografar cada elemento de lM

    return c

# Imprime a mensagem criptografada utilizando a tabela ASCII
# Entrada: C -> lista de inteiros
# Saída: Mct -> string
def char_cript(C):
    Mct = ""
    for el in C:
        Mct += chr(el % 128)
    
    return Mct

# Realiza a descriptografia da mensagem
# Entradas: p -> lista de primos
#           C -> lista de inteiros
#           d -> inteiro
# Saída: M -> inteiro
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

# Retorna a string contendo a mensagem descriptografada
# Entradas: p -> lista de primos
#           C -> lista de inteiros
#           d -> inteiro
# Saída: Dm -> string
def descript_msg(p, C, d):
    dl = []
    for el in C:
        dl.append(descriptografar(p, el, d))

    Dm = int_to_str(dl) # Transforma a lista de inteiros em uma string

    return Dm