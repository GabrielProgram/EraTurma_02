# Curso de Python
# 2020/05/09

"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas, e informe
ao final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.
"""
print('Departamento Estadual de Meteorologia: \n'
      'Digite as temperaturas para o cálculo:\n'
      "Digite 'end' para realizar o cálculo:")

N = 1
Temperaturas = 1
TemperaturasTemp = 0
Soma = 0
Média = 0
Mínimo = 0
Máximo = 0
Sair = 'string'

while Sair != 'end':
    TemperaturasTemp = input('Temperatura {}:\n'.format(N))
    if TemperaturasTemp == 'end':
        Sair = 'end'
    while TemperaturasTemp != 'end':
        try:
            Temperaturas = float(TemperaturasTemp)
            N = N + 1
        except ValueError:
            print('Please insert a valid real number and try again.')
            break
        else:
            break
    Soma = Soma + Temperaturas
    Média = Soma / 2
    if Mínimo == 0:
        Mínimo = Soma + 1
    if Mínimo >= Temperaturas:
        Mínimo = Temperaturas
    if Máximo <= Temperaturas:
        Máximo = Temperaturas

print('\nSoma:\n{}'.format(Soma))
print('Média:\n{}'.format(Média))
print('Máximo:\n{}'.format(Máximo))
print('Mínimo:\n{}'.format(Mínimo))