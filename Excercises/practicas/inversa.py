def inversa(cadena: str):
    return cadena[::-1]

def inversa_v2(cadena: str):
    res = ""
    for i in range(1, len(cadena)+1):
        res += cadena[-i]
    return res

print(inversa_v2("hola"))