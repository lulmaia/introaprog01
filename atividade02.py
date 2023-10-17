entrada = input("Digite uma lista de números: ")

numeros_str = entrada.split()

numeros = [int(numero) for numero in numeros_str]

soma_pares = 0

for numero in numeros:
    if numero % 2 == 0:
        soma_pares += numero

print("A soma dos números pares na lista:", soma_pares)
