try:
    numero_1 = float(input('Inserir o primeiro número: '))
    numero_2 = float(input('Inserir o segundo número: ')) 
        
    resultado = numero_1 + numero_2
        
    print(f"Resultado: {resultado}")

except ValueError:
    print('Por favor, insira um número')