#Crie um programa que envie mensagens personalizadas para uma lista de contatos, o script deve:
#1. pedir ao usuario uma lista de nomes;
#2. criar uma mensagem personalizada;
#3. exibir a mensagem com um pequeno intervalo entre os envios(simulando um chatbot)

import time
import random

listaContatos = []

while True:
    listaContatos.append(input("Digite os Nomes: "))
    maisnomes = input("Deseja continuar: ").lower()
    if maisnomes == "n":
        break
    def msg(lista):
        print(f"Boa Noite {random.choice(lista)}")
        time.sleep(2)
        print("Phython")
    msg(listaContatos)