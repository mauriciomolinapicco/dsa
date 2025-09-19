import json

# Diccionario con datos
data = {
    "clientes": [
        {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"},
        {"nombre": "Ana", "edad": 25, "ciudad": "Barcelona"},
        {"nombre": "Luis", "edad": 35, "ciudad": "Valencia"}
    ],
    "empresa": {
        "nombre": "Tech Solutions",
        "sector": "Tecnología"
    }
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)


"""
Uses json.dump(data,file) because it translates from python dict to json automatically
"""