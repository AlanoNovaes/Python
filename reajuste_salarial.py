#Calculando reajuste salarial de 15%
salario = float(input('Qual o salario do funcionário? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com o reajuste de 15% passou a ganhar R${:.2f}'.format(salario,novo))