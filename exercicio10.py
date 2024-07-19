"""
Exemplo 3: Imprimir palavras com tamanho específico
Escreva um programa que percorra uma string e imprima as palavras que têm exatamente 4 letras.
"""
texto = input('digite um texto: ').split(' ')

for i in texto:
    i = i.replace(".", "")
    i = i.replace(",", "")

    if len(i) == 4:
        break
    print(f'{i}')
    print('****************')



# saldo = 1000
# enviar = 101

# if enviar <= saldo:
#     print('pix enviado')
#     saldo -= enviar
#     print(f'Seu saldo é de R$ {saldo:,.2f}')
    

# else:
#     print(f'Valor não pode ser enviado, seu saldo é de R$ {saldo:,.2f}, e o queres enviar é de R$ {enviar:,.2f}')