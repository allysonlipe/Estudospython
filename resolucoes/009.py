#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

temperaturaFarenheit = int(input('Digite a Temperatura em F°: '))

temperaturaCelsius = round((5*(temperaturaFarenheit-32)/9))

print('A temperatura em Celsius é: '+str (temperaturaCelsius) +'C°')