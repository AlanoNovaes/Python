largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m² '.format(largura, altura, area))
#Supondo que um litro de tinta consigo pintar 2 metros de area
tinta = area / 2
print('Para pintar essa parede você precisa de {} litros de tinta. '.format(tinta))