"""
Exemplo 2: Contar vogais e consoantes
Escreva um programa que conte o número de vogais e consoantes em uma string.
dica: nesse exercício pode utilizar uma variavel auxiliar para ver se é uma vogal 
vogais = "aeiouAEIOU"
"""

palavra = input('digite uma palavra: ')

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

total_vogais = 0
total_consoantes = 0

for letra in palavra:
    if letra in vogais:
        
        total_vogais += 1
    if not letra in vogais:

        total_consoantes += 1


print(f'total de vogais no nome {total_vogais}\ntotal de consoantes no nome {total_consoantes}')