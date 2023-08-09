#n = int(input('Digite um numero: '))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('Analisando o valor de {}, \no dobro dele é {} \no triplo é {} \ne a raiz quadrada é {:.2f}'.format(n, d, t, r))
# para a raiz quadrada não ficar com muitos valores usei a formatação em 2 casas decimais flutuantes 
#Outra forma de resolver sem usar muitas variaveis:
n = int(input('Digite um numero: '))
print('O dobro de {} vale {}. ' .format(n, (n*2)))
print('O triplo de {} vale {}. \n A raiz quadrada de {} vale {:.2f}' .format(n, (n*3), n, pow(n, (1/2))))