n = int(input())

lista = list(map(int, input().split()))

for i in range(n):
    menor = lista[i]
    pos_menor = i
    for j in range(i,n):
        if lista[j] < menor:
            menor = lista[j]
            pos_menor = j
    tmp = lista[i]
    lista[i] = lista[pos_menor]
    lista[pos_menor] = tmp

print(" ".join(map(str, lista)))
