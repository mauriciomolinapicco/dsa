def es_palindromo(cadena):
    stack = []
    for c in cadena:
        stack.append(c)

    for c in cadena:
        if c != stack.pop():
            return False
    
    return True


def es_palindromo_optimizada(cadena):
    stack = []
    n = len(cadena)

    for i in range(n//2):
        stack.append(cadena[i])

    for i in range((n+1) // 2, n):
        if cadena[i] != stack.pop():
            return False
    
    return True



def es_palindromo_v2(cadena):
    return cadena == cadena[::-1]