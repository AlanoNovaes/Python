dinheiro = float(input('Quantos reais você tem na carteira? R$ '))
dolar = dinheiro / 4.87
euro = dinheiro / 5.25
print('Com R${:.2f} você pode comprar US${:.2f} em dolar ou se preferir EUR {:.2f}'.format(dinheiro, dolar, euro))