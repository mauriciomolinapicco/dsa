def eliminar_duplicados(arr):
    vistos = set()
    res = []
    for item in arr:
        if item not in vistos:
            vistos.add(item)
            res.append(item)
    return res

lista = eliminar_duplicados([1,1,1,1,2,2,2,2,3,3,66,55,44,55,5])
print(lista)    #[1, 2, 3, 66, 55, 44, 5]