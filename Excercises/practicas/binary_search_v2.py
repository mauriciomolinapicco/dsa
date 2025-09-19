def binary_search(lista, obj):
    l, r = 0, len(lista) - 1
    while l <= r:
        m = (l+r) // 2
        if lista[m] > obj:
            r = m - 1
        elif lista[m] < obj:
            l = m + 1
        else:
            return m
    return -1


lista = [1,2,3,4,5,6,7,8,9,10]
print(f"Esta en la posicion: {binary_search(lista, 10)}")