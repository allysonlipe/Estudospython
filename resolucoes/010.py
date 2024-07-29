#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temperaturaCelsius = int(input('Digite a Temperatura em C°: '))

temperaturaFarenheit = round((1.8*temperaturaCelsius)+32)

print('A temperatura em Farenheit é: '+str (temperaturaFarenheit) +'F°')