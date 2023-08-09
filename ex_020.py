#Sorteando uma ordem na lista
#Como vou utilizar somente um módulo do random importei somente o shuffle
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação dos trabalhos sera: ')
print(lista)
