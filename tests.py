import sys
import time
import msvcrt
import os
from math import sqrt
from randomPrime import generate_list
import keyGen
import cript

# Controle dos testes
num_testes = 1000
success = 0
failures = 0

# Variáveis relacionadas aos testes
np = 3
min_pot = 5
max_pot = 6
msg = "mLçãóê_( 7]"
path = "Tables/Table4/Tabela4-"+str(min_pot)+"-"+str(max_pot)+".txt"  # Onde os dados serão salvos

# Para cálculo do Desvio Padrão
total_time = 0  # Soma total do tempo de execução dos testes
times = []      # Lista para armazenar todos os tempos medidos

arq = open(path, "w")
# arq.write("N\t\t\td\t\t\te\t\t\ttime\n")
i = 0
while i < (num_testes) and not msvcrt.kbhit():
    try:
        ini = time.time()   # Início do teste
        
        # Preenche a lista com np primos aleatórios e diferentes entre si
        p = generate_list(np, min_pot, max_pot)
        # GERAÇÃO DE CHAVES

        #Chave Pública <N, e> // Chave Partucular <N, d>
        N = keyGen.calc_N(p)
        phiN = keyGen.calc_phiN(p)
        e = keyGen.get_e(phiN)                           # Valor Relativamente Primo a phiN
        d = keyGen.calc_d(e, phiN)                       # Inversa de e módulo phiN

        # CRIPTOGRAFIA
        C = cript.cript_msg(msg, e, N)

        # DESCRIPTOGRAFIA
        Mx = cript.descript_msg(p, C, d)

        end = time.time()   # Fim do teste

        # Atualização dos valores para cálculo do Desvio Padrão
        total_time += end - ini
        times.append(end - ini)
        arq.write("e : "+str(e)+"\n")
        # Teste ocorreu sem erros
        # arq.write(str(N)+" \t\t"+str(d)+" \t\t"+str(e)+" \t\t"+str(end - ini)+"\n")
        if msg != Mx:
            arq.write("#################FAIL#################\n")
            arq.write("M: "+msg+"\nMd: "+Mx+"\n")
            for el in p:
                arq.write(str(el)+" ")
            arq.write(str(N)+" "+str(e)+" "+str(d)+"\n")
            failures += 1
        else:
            success += 1
        clear = lambda: os.system("cls")
        clear()
        print("Sucessos: ", success, "\nFracassos: ", failures, "\n")
        i += 1
    except:
        # Algum erro ocorreu na execução desse teste
        failures += 1
        arq.write("ERROR: ")
        for el in p:
            arq.write(str(el)+" ")
        arq.write(str(N)+" "+str(e)+" "+str(d)+"\n")
        clear = lambda: os.system("cls")
        clear()
        print("Sucessos: ", success, "\nFracassos: ", failures, "\n")
        i += 1


# Cálculo do desvio padrão

total_time /= i
dp = 0

arq.write("\nMédia: "+str(total_time))
for tempo in times:
    dp += (tempo - total_time)**2

dp /= i
dp = sqrt(dp)

arq.write("\nDP = "+str(dp)+"\n")
arq.write("\nSuccesses: "+str(success)+"\nFailures: "+str(failures))

arq.close()