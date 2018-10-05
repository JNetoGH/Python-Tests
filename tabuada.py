txt = {'ln': '-=' * 20,
       'c': '\033[m',
       'b': '\033[1m'}

print(txt['ln'])
print('{}               TABUADA{}'.format(txt['b'], txt['c']))
print(txt['ln'])
num = int(input('Insira o número a ser multiplicado: '))
range1 = int(input('Isira o início da tabuada: '))
range2 = int(input('Insira o fim da tabuada: '))
print(txt['ln'])

for c in range(range1, range2+1):
    result = c * num
    print('{}{} x {} = {}{}'.format(txt['b'], num, c, result, txt['c']))
print(txt['ln'])
