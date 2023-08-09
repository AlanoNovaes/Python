# Jogo da Adivinhação v.1.0
from random import randint
from time import sleep
computador = randint(0,5) #Faz o computador sortear o número entre 0 e 5
jogador = int(input('Digite um número entre 0 e 5: ')) #Jogador tenta adivinhar o número
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('Você errou! Eu pensei no número {} e não no {}! tente novamente!'.format(computador,jogador))

