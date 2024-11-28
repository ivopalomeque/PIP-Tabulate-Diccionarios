from tabulate import tabulate

# Lista de Diccionarios
personas = [
  {"nombre": "Fabio", "edad": 36, "ciudad": "jujuy"},
  {"nombre": "Luis", "edad": 25, "ciudad": "Cordoba"},
  {"nombre": "Ana", "edad": 52, "ciudad": "San Juan"},
  {"nombre": "Pedro", "edad": 45, "ciudad": "Rosario"},
]

for persona in personas:
  print(persona)

for persona in personas:
  print(f"Name: {persona["nombre"]}, Age: {persona['edad']}, City: {persona['ciudad']}")

for persona in personas:
  if persona["edad"] > 40:
    print(persona["nombre"], "esta viejito")
  else:
    print(persona["nombre"], "esta jovencito")

mayores_de_40 = [persona["nombre"] for persona in personas if persona["edad"] > 40]
    
print(mayores_de_40)

tabla_personas = [list(persona.values()) for persona in personas]
tabla_encabezados = personas[0].keys()
encabezados=["nombre", "edad", "ciudad"]
print(tabulate(tabla_personas, headers=encabezados, tablefmt="pipe"))