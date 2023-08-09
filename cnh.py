nome = input('Qual seu nome ? ')
print('Seja bem vindo!  ' + nome)
idade = int(input('Qual sua idade?  ' ))
if idade >= 18:
    print('Você ja pode dirigir ' + nome)
else:
     print('Aguarde a idade para dirigir! ')
     exit()   
print('O valor para tirar a CNH é R$1.000 e só aceitamos pagamento à vista! ')
valor = 1000
dinheiro = int(input('Quanto você tem pra pagar pela habilitação? ')) 
if dinheiro >= 1000:
    print('Já podemos marcar as aulas! ')
else:
    print('Poupe mais dinheiro! Para pagar a vista e poder ter descontos :) ')