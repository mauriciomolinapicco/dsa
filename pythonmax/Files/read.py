print("Reading lines")
with open('archivo.txt', 'r') as file:
    lines = file.readlines()  # Read all lines as a list
    for i,linea in enumerate(lines):
        print(f"Linea {i}: {linea.strip()}")  # Strip elimina el \n al final


print("------------------")
print("Reading the whole file at once...")
with open('archivo.txt', 'r') as file:
    content = file.read()
    print(content)


print("------------------")
print("Reading the first x characters...")
with open("archivo.txt", "r") as file:
    content = file.read(30)
    print(content)
