# Aumentos múltiplos
salario = float(input('Qual é o seu salário? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Você ganhava R${:.2f} e passou a ganhar R${:.2f}'.format(salario, novo))
          