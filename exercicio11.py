"""
Exercício 11: Filtrando Palavras por Comprimento
Enunciado: Dada uma lista de palavras, escreva um programa que filtre e exiba apenas as palavras que têm mais de 5 caracteres.

palavras = ["banana", "abacate", "uva", "laranja", "ameixa", "ovo", "kiwi"]
"""
palavras = ["banana", "abacate", "uva", "laranja", "ameixa", "ovo", "kiwi"]

for i in palavras:

    if len(i) >= 5:
        print(f'{i}')