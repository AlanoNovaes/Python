a = input('Digite algo: ')
# TODA VARIAVEL PODE SER TESTADA CONFORME EXEMPLOS ABAIXO 
# VERIFICAR O TIPO DA VARIAVEL A QUE NO CASO POR PADRÃO É STRING
print('O tipo primitivo desse valor é: ', type(a))
# VERIFICAR SE O USUARIO DIGITOU SOMENTE ESPAÇOS.
print('Só tem espaços? ' ,a.isspace())
# VERIFICAR SE O USUARIO DIGITOU SOMENTE NUMEROS.
print('É um número? ' ,a.isnumeric())
# VERIFICAR SE É ALFABÉTICO.
print('Tem letras? ' ,a.isalpha())
#VERIFICAR SE O USUARIO DIGITOU LETRAS E NUMEROS.
print('É alfanúmerico? ' ,a.isalnum())
#VERIFICAR SE O USUARIO DIGITOU LETRAS MAIUSCULAS.
print('É maiusculo? ' ,a.isupper())
#VERIFICAR SE O USUARIO DIGITOU LETRAS MINUSCULAS.
print('É minusculas? ' ,a.islower())
#VERIFICAR SE O USUARIO DIGITOU LETRAS CAPITALIZADAS (MAIUSCULAS E MINUSCULAS)
print('Está capitalizada?', a.istitle())