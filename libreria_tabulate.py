from tabulate import tabulate

data = [
  ["Nombre", "Edad", "Ciudad"],
  ["Ana", 18, "Bs As"],
  ["Pedro", 15, "Cordoba"],
  ["Luis", 17, "Rosario"],
]

print(tabulate(data[1:], headers=data[0], tablefmt="github"))
print(tabulate(data[1:], headers=data[0], tablefmt="keys"))
print(tabulate(data[1:], headers=data[0], tablefmt="html"))
print(tabulate(data[1:], headers=data[0], tablefmt="text"))

""" # Calcular el ancho máximo de cada columna
column_widths = [max(len(str(row[col])) for row in data) for col in range(len(data[0]))]

# Crear una fila formateada
def format_row(row):
    return " | ".join(str(cell).ljust(width) for cell, width in zip(row, column_widths))

# Imprimir la tabla
print(format_row(data[0]))  # Encabezados
print("-" * sum(column_widths) + "-" * (len(column_widths) - 1))  # Separador
for row in data[1:]:
    print(format_row(row))  # Filas """
