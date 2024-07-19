try:
    valor = int(input('Inserir quanto deseja converter para dólar: '))
    
        
    resultado = valor * 5.47
        
    print(f"US$ {resultado:.2f}")

except ValueError:
    print('Por favor, insira um valor válido')