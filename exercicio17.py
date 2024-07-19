"""
Exercício 17: Verificação de Sufixo
Dada uma lista de strings e um sufixo, verifique quais strings 
terminam com esse sufixo e imprima o índice dessas strings.

palavras = ['banana', 'manga', 'uva', 'limão', 'melão']

sufixo = 'ão'

esse exericio, imprimir os indices e palavras que contenham o sufixo
"""

palavras = ['banana', 'manga', 'uva', 'limão', 'melão']
sufixo = 'ão'

for index, palavra in enumerate(palavras, start=1):
    if palavra[-2:] == sufixo:
        print(f'{index}. {palavra}')