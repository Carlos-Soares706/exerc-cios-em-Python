print("Calculadora com Tratamento de Exceções")

try:
    numero_1 = float(input('Inserir o primeiro número: '))
    numero_2 = float(input('Inserir o segundo número: '))
    operacao = input('Inserir operação (+, -, *, /): ')

    if operacao == '+':
        resultado = numero_1 + numero_2
    elif operacao == '-':
        resultado = numero_1 - numero_2
    elif operacao == '*':
        resultado = numero_1 * numero_2
    elif operacao == '/':
        if numero_2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida")
        resultado = numero_1 / numero_2
    else:
        raise ValueError("Operação inválida. Use +, -, * ou /.")

    print(f"Resultado: {resultado}")

except ValueError as ve:
    print(f"Erro de valor: {ve}")
except ZeroDivisionError as zde:
    print(f"Erro de divisão: {zde}")
except Exception as e:
    print(f"Erro inesperado: {e}")
