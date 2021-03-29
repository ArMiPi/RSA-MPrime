import sys
import args
from randomPrime import generate_list
import keyGen
import cript

if len(sys.argv) < 5:
    print("Parâmetros insuficientes!")
    print("Uso: python RSA-MPrime.py <número de primos> <potência mínima> <potência máxima> <mensagem>")
    exit()

params = args.Args(sys.argv)

# Preenche a lista com np primos aleatórios e diferentes entre si
p = generate_list(params.np, params.min_pot, params.max_pot)

print(p)
print(set(p))

# GERAÇÃO DE CHAVES

#Chave Pública <N, e> // Chave Partucular <N, d>
N = keyGen.calc_N(p)
phiN = keyGen.calc_phiN(p)
e = keyGen.get_e(phiN)                           # Valor Relativamente Primo a phiN
d = keyGen.calc_d(e, phiN)                       # Inversa de e módulo phiN

# Imprime as chaves pública e privada
keyGen.print_keys(N, e, d)

# CRIPTOGRAFIA
C = cript.cript_msg(params.msg, e, N)

# DESCRIPTOGRAFIA
Mx = cript.descript_msg(p, C, d)

# Passar os inteiros da lista C para valores pertencentes à tabela ASCII
Mct = cript.char_cript(C)

print("Mensagem Original: ", params.msg)
print("Mensagem Criptografada: ", Mct)
print("Mensagem Decriptografada: ", Mx)