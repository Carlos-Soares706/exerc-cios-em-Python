numeros = input("lista de números: ").split()


numeros = [int(num) for num in numeros]


numeros_positivos = [num for num in numeros if num >= 0]


print("lista dos numeros positivos:", numeros_positivos)