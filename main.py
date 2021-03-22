from randomPrime import GeneratePrime

p1 = GeneratePrime().rnd_prime
p2 = GeneratePrime().rnd_prime
p3 = GeneratePrime().rnd_prime

print(p1)
print(p2)
print(p3)

# Leitura da Mensagem a ser criptografada 
print("Mensagem: ")
M = input()

# GERAÇÃO DE CHAVES

#Chave Pública <N, e> // Chave Partucular <N, d>
N = p1 * p2 * p3
phiN = (p1 - 1) * (p2 - 1) * (p3 - 1)
e = 65537                           # Valor Relativamente Primo a phiN
d = pow(e, -1, phiN)                # Inversa de e módulo phiN

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
C = (int(M)**e) % N                 # Aplicação da Chave Pública a M
# DECRIPTOGRAFIA

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

print("Mensagem Original: ", M)
print("Mensagem Criptografada: ", C)
print("Mensagem Decriptografada: ", M)