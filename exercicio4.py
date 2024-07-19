print("Calculadora com Tratamento de Exceções")

try:
    numero_1 = float(input('Inserir o primeiro número: '))
    numero_2 = float(input('Inserir o segundo número: '))
    operacao = input('Inserir operação (+, -, *, /): ')
    resultado = False

    if operacao == '+':
        resultado = numero_1 + numero_2
    elif operacao == '-':
        resultado = numero_1 - numero_2
    elif operacao == '*':
        resultado = numero_1 * numero_2
    elif operacao == '/':
        resultado = numero_1 / numero_2
    if resultado == False:
        print("operação incorreta")
    else:
        print(f"Resultado: {resultado}")

except :
    print('Por favor, insira uma conta valida')

finally:
    print('Finalizado')
        
