#DICT COMPREHENSION
potencias = {i: i*i for i in range(5)}

print(potencias)
#{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#LOOP THROUGH MAPS
for key in potencias:
    print(key, potencias[key])

for value in potencias.values():
    print(value)

for key, val in potencias.items():
    print(f"potencia de {key} es {val}")


# se pueden usar tuplas como keys para hashmaps
