# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
#     o produto do dobro do primeiro com metade do segundo.
#     a soma do triplo do primeiro com o terceiro.
#     o terceiro elevado ao cubo.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

calc1 = 2*n1*n2/2
print('O produto do dobro do primeiro com metade do segundo: '+ str(calc1))
calc2 = (3*n1)+n3
print('a soma do triplo do primeiro com o terceiro: '+ str(calc2))
calc3 = n3**3
print('o terceiro elevado ao cubo: '+str(calc3))