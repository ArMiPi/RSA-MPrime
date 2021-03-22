from randomPrime import GeneratePrime
import keyGen
import cript

p1 = GeneratePrime().rnd_prime
p2 = GeneratePrime().rnd_prime
p3 = GeneratePrime().rnd_prime

#print(p1)
#print(p2)
#print(p3)

# Leitura da Mensagem a ser criptografada 
print("Mensagem: ")
M = input()

# GERAÇÃO DE CHAVES

#Chave Pública <N, e> // Chave Partucular <N, d>
N = keyGen.calc_N(p1, p2, p3)
phiN = keyGen.calc_phiN(p1, p2, p3)
e = keyGen.get_e()                           # Valor Relativamente Primo a phiN
d = keyGen.calc_d(e, phiN)                   # Inversa de e módulo phiN

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
Mx = cript.descript_msg(p1, p2, p3, C, d)

# Passar os inteiros da lista C para valores pertencentes à tabela ASCII
Mct = ""
for el in C:
    Mct += chr(el % 127)

print("Mensagem Original: ", M)
print("Mensagem Criptografada: ", Mct)
print("Mensagem Decriptografada: ", Mx)