#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


import math
raio = float(input("Digite raio do círculo: "))

area = math.pi*(raio**2)
area_str = str(format(area,'.2f'))

print('A área é: '+area_str +'m².')

