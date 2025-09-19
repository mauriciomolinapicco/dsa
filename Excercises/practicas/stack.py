"""
Ejercicio: Validación de paréntesis
Descripción:

Dada una cadena que contiene solo los caracteres '(', ')', '{', '}', '[', y ']', determina si la secuencia de paréntesis es válida.

Una secuencia de paréntesis es válida si:

Los paréntesis se cierran en el orden correcto.

Cada tipo de paréntesis debe cerrarse con su par correspondiente.

Ejemplo 1:

Entrada: s = "()"

Salida: True

Ejemplo 2:

Entrada: s = "()[]{}"

Salida: True

Ejemplo 3:

Entrada: s = "(]"

Salida: False

Ejemplo 4:

Entrada: s = "([)]"

Salida: False

Ejemplo 5:

Entrada: s = "{[]}"

Salida: True

"""
def is_valid(cadena):
    stack = []
    valid = {")":"(", "]":"[", "}":"{"}
    for c in cadena:
        if c in valid.values():
            stack.append(c)
        elif c in valid:
            if stack:
                par = stack.pop()
            else: 
                return False
            if par != valid[c]:
                return False
    
    return True

# valid = {"(":")", "[":"]", "{":"}"}

print(is_valid("hola me llamo ((hello)) [world{python}]"))

