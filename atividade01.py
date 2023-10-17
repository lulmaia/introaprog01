q = []

for i in range(20):
    while True:
        num = float(input('Digite um número positivo: '))
        if num > 0:
            q.append(num)
            break
        else:
            print('Erro!')


maior_elemento = q[0]
menor_elemento = q[0]

posicao_maior_elemento = 1
posicao_menor_elemento = 1


for i in range(1, len(q)):
    if q[i] > maior_elemento:
        maior_elemento = q[i]
        posicao_maior_elemento = i + 1
    if q[i] < menor_elemento:
        menor_elemento = q[i]
        posicao_menor_elemento = i + 1

print(f"O maior elemento de Q é {maior_elemento} e ocupa a posição {posicao_maior_elemento} no vetor.")
print(f"O menor elemento de Q é {menor_elemento} e ocupa a posição {posicao_menor_elemento} no vetor.")
