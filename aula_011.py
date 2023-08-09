# Cores no Terminal utilizando ANSI
nome = 'Alano'
cores = {'vermelho': '\033[33m',
         'branco': '\033[30m',
         'pretoebranco': '\033[7m',
                       }
print('Olá! Muito prazer em te conhecer {}{}'.format(nome, cores['pretoebranco']))