try:
    valor = int(input('Inserir uma quantidade de horas: '))
    
        
    resultado = valor * 60
        
    print(f" {resultado} minutos")

except ValueError:
    print('Por favor, insira um valor válido')