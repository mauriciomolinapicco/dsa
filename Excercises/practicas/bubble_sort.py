def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(i+1):
            if lista[j] > lista[i]:
                lista[i],lista[j] = lista[j], lista[i]
    return lista

ordenada = bubble_sort([5,4,3,2,1])
print(ordenada)