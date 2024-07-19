from time import sleep

numero = input('Inserir um numro pra contagem regressiva: ')
numero = int(numero)

while numero > 0:

    try:
        numero -= 1
        print(f'{numero}')
        sleep(1)

    except ValueError:
        print('Por favor, insira um número valido')

