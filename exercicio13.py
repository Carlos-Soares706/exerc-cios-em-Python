"""
Exercício 13: Verificando Sequências de Caracteres
Enunciado: Escreva um programa que, dada uma lista de palavras, verifique se cada palavra contém as letras
 de caracteres 'a','b','c' e exiba as palavras que contêm .
"""

nomes = [
    "Ana", "Beatriz", "Carlos", "Daniela", "Eduardo", 
    "Fernanda", "Gustavo", "Helena", "Igor", "Juliana", 
    "Karina", "Lucas", "Mariana", "Nelson", "Olivia", 
    "Pedro", "Rafael", "Sofia", "Thiago", "Bianca"
]

for nome in nomes:
    if "A" in nome.upper() and "B" in nome.upper() and "C" in nome.upper():

        print(nome)
