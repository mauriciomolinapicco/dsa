# Ejercicio: Dado un string, encuentra la frecuencia de cada letra en él.
def frecuencia(cadena:str):
    freq = {}
    for c in cadena:
        freq[c] = freq.get(c, 0) + 1
    return freq

f = frecuencia("python hello world")
for i in f:
    if i != " ":
        print(f"Letra: {i} || Cant apariciones: {f[i]}")

    """
Letra: p || Cant apariciones: 1
Letra: y || Cant apariciones: 1
Letra: t || Cant apariciones: 1
Letra: h || Cant apariciones: 2
Letra: o || Cant apariciones: 3
Letra: n || Cant apariciones: 1
Letra: e || Cant apariciones: 1
Letra: l || Cant apariciones: 3
Letra: w || Cant apariciones: 1
Letra: r || Cant apariciones: 1
Letra: d || Cant apariciones: 1
"""