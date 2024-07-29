#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input('Digite quanto vale sua hora: '))
horasTrabalhadas = int(input('Digite quantas horas você trabalhou esse mês: '))

salario = format(valorHora * horasTrabalhadas, '.2f')

print('Seu salário esse mês foi de: R$ '+str(salario))