"""
Exercício 15: Classificar Números em Duas Listas
Dada uma lista de números, classifique-os em duas listas: 
uma contendo os números positivos e outra contendo os números negativos.
"""
numeros = [12, -7, 5, -3, 9, -14, 8, -1, 4, -10]

positivos = []
negativos = []

for numero in numeros:
    if numero >= 0:
        positivos.append(numero)
        
    else:
        negativos.append(numero)
        

print(f'positivos {positivos}')
print(f'negativos {negativos}')