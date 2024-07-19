"""
Exercício 16: Substituição de Palavras
Dada uma lista de frases e uma palavra específica, substitua essa palavra por outra em todas as frases da lista.
variáveis utilizaveis
frases = ['Eu gosto de maçã', 'A maçã é saudável', 'Prefiro maçã a pera']

substituir 'maça' por 'laranja'
"""

frases = ['Eu gosto de maçã', 'A maçã é saudável', 'Prefiro maçã a pera']
  
for i in frases:
    
    i = i.replace("maçã", "laranja")
    print(i)
