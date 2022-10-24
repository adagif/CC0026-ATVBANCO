import threading
import time 
import random

# Escreva um programa em Python, que simule a fila de atendimento de um banco. 
# O banco possui 3 caixas. O tempo de atendimento de cada cliente deve ser um 
# tempo aleatório entre 3 a 10 segundos. Suponha que a fila tenha um tamanho 
# fixo com 30 clientes em espera. Utilize um semáforo para fazer o gerenciamento 
# dos recursos compartilhados (caixas) entre os clientes (threads). 

semaforo = threading.Semaphore(3)
print('FILA DE ATENDIMENTO')

def atendimentoBanco(i:str):
    semaforo.acquire()
    print(f'Atendimento {i}')
    time.sleep(random.randint(3,10))
    semaforo.release()

if __name__ == "__main__":
    cli = []
    for i in range(0,30):
        cli.append(threading.Thread(target=atendimentoBanco))
        cli[i].start()
    for i in cli:
        i.join()
