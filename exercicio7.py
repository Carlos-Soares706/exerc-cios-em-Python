
numero = (input('Inserir o CPF: '))
numero_2 = numero.replace(".", "")
numero_3 = numero_2.replace("-", "")
tam_numero = len(str(numero_3))
print(f'tamanho numero{tam_numero}')

if tam_numero == 11:
    print("numero válido.")
else:
    print('Numero invalido.')

