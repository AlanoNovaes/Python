# Custo da Viagem
distancia = float(input('Digite a distancia da viagem: '))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))          