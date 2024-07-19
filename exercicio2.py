try:
    temperatura = float(input('Inserir a temperatura em Celsius: '))
    
    fahrenheit = (9/5)*temperatura + 32

    print('em fahrenheit a temperatura é',fahrenheit )

except ValueError:
    print('Por favor, insira um número')