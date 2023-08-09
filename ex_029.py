# Radar eletrônico
velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade >= 80:
    print('Você excedeu o limite de velocidade da via e será multado em R${:.2f}'.format(multa)) 
else:
    print('Tenha um bom dia e dirija com segurança!')
          