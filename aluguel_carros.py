#Calculando aluguel de carros sabendo que a diaria é R$60,00 e a cada km rodado R$0,15
dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de {:.2f}'.format(pago))
