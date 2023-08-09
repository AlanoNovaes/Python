#Seno, Cosseno e Tangente
from math import radians, sin, cos, tan
angulo = float(input('Digi te o Angulo que você deseja: '))
seno = sin(radians(angulo))
print('O Angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('O angulo de {} tem o Tangente de {:.2f}'.format(angulo, tangente))
