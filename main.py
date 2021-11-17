

import time
import random
import threading
from cores import *


print('\nBem vindo, você terá 1 minuto para digitar o máximo de palavras possíveis!\nIniciando em ', end= ' ')
time.sleep(10)
for i in range(3, 0, -1):
    print(f'{color_green()}{i}', '...', end=' ')
    time.sleep(1)

lista_palavras = []

with open('palavras.txt', 'r') as arquivo_palavras:
    for palavras in arquivo_palavras:
        palavras = palavras.rstrip()
        lista_palavras.append(palavras)

rodadas = 0
pontos = 0
erros = 0
tempo = True

def cronometro():
    # tempo = True
    global tempo
    minuto = segundo = 0
    while tempo == True:
        time.sleep(1)
        segundo += 1
        if segundo == 60:
            segundo = 0
            minuto += 1
        if minuto == 1:
            print('Tempo acabou!')
            tempo = False
            return tempo

threading.Thread(target=cronometro).start()

while True:


    palavras_na_tela = random.choice(lista_palavras)
    print(f'\n\n{color_white()}Digte a palavra: {palavras_na_tela}')
    teste_digitacao = input()
    rodadas += 1

    if tempo == False and rodadas >= 1:
        print(f'\n{color_white()}Sua pontuação foi de {pontos} pontos\nVocê errou {erros} palavras\nTotal de tentativas foi de {rodadas-1}')
        break

    elif teste_digitacao == palavras_na_tela:
        print(f'{color_green()}Correto!')
        pontos += 1

    else:
        print(f'{color_red()}Errado!')
        erros += 1

    if tempo == False and rodadas >= 1:
        print(f'\n{color_white()}Sua pontuação foi de {pontos} pontos\nVocê errou {erros} palavras\nTotal de tentativas foi de {rodadas-1}')
        break

