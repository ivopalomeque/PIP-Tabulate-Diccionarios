mi_diccionario = {}

persona = {
  "nombre": "Fabio",
  "edad": 36,
  "ciudad": "jujuy"
}

# Acceso a datos
print(persona)
print(persona["nombre"])
print(persona["ciudad"])
print(persona["edad"])
# KeyError: print(persona["altura"])

print(persona.get("altura")) # Devuelve None
print(persona.get("profesion", "Desconocida")) # Devuelve Desconocida

# Modificación o Creación
persona["edad"] = 31
print(persona["edad"])
persona["profesion"] = "Profesor"
print(persona.get("profesion", "Desconocida")) # Devuelve Profesor

# Borrar
del persona["profesion"]
print(persona.get("profesion", "Desconocida")) # Devuelve Desconocida nuevamente

# Iterar claves
for key in persona:
  print(key)

# Iterar valores
for value in persona.values():
  print(value)

# Iterar claves y valores
for key, value in persona.items():
  print(f"{key}: {value}")

print(persona.keys())
print(persona.values())
print(persona.items())

# tamaño
print(len(persona)) #3

# Buscar una clave
if "edad" in persona:
  print("Tiene la clave")

pares = [x**2 for x in range(10) if x % 2 == 0]
print(pares)

cuadrados = {x: x**2 for x in range(10)}
print(cuadrados)