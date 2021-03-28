from randomPrime import GeneratePrime
import keyGen
import cript

p = []  # Lista para armazenar os primos que serão utilizados

# Leitura da quantidade de primos
print("Entre com o número de primos a serem utilizados na criptografia (>= 2): ")
np = int(input())
print("Entre com o valor do menor expoente(x) para a base 10 (!0^x): ")
min = int(input())
print("Entre com o valor do maior expoente(x) para a base 10 (!0^x): ")
max = int(input())

# Preenche a lista com np primos aleatórios e diferentes entre si
while len(p) < np:
    prime = GeneratePrime(min, max).rnd_prime
    while prime in p:
        prime = GeneratePrime(min, max).rnd_prime
    
    p.append(prime)

print(p)
print(set(p))

# Leitura da Mensagem a ser criptografada 
print("Mensagem: ")
M = input()

# GERAÇÃO DE CHAVES

#Chave Pública <N, e> // Chave Partucular <N, d>
N = keyGen.calc_N(p)
phiN = keyGen.calc_phiN(p)
e = keyGen.get_e(phiN)                           # Valor Relativamente Primo a phiN
d = keyGen.calc_d(e, phiN)                       # Inversa de e módulo phiN

# Imprime as chaver pública e privada
CPb = "Pública: <{}, {}>"
CPv = "Privada: <{}, {}>"

print()
print("Chaves: ")
print("="*50)
print(CPb.format(N, e))
print(CPv.format(N, d))
print("="*50)
print()

# CRIPTOGRAFIA
C = cript.cript_msg(M, e, N)

# DESCRIPTOGRAFIA
Mx = cript.descript_msg(p, C, d)

# Passar os inteiros da lista C para valores pertencentes à tabela ASCII
Mct = ""
for el in C:
    Mct += chr(el % 127)

print("Mensagem Original: ", M)
print("Mensagem Criptografada: ", Mct)
print("Mensagem Decriptografada: ", Mx)