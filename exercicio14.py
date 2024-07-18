"""
Exercício 14: Comparando Comprimento de Palavras
Enunciado: Dada uma lista de pares de palavras, escreva um programa que compare o comprimento de cada par
 de palavras e exiba qual palavra de cada par é a mais longa.

pares_palavras = [("casa", "laranja"), ("banana", "uva"), ("python", "java"), ("amor", "amizade")]
"""
pares_palavras = [("casa", "laranja"), ("banana", "uva"), ("python", "java"), ("amor", "amizade")]

for duplas in pares_palavras:
     
    if len(duplas[0]) > len(duplas[1]):
        print(f'{duplas[0]}')
    if len(duplas[0]) < len(duplas[1]):
        print(f'{duplas[1]}')