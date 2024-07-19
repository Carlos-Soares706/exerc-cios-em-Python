palavra = input('digite uma palavra: ')

vogais = ['a', 'e', 'i', 'o', 'u' ]

total_vogais = 0

for letra in palavra:
    if letra in vogais:
        
        total_vogais += 1

print(f'total de vogais no nome {total_vogais}')
        
