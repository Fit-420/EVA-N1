# Precios de los sándwiches
precios_sandwiches = {
    "Churrasco": 1500,
    "Completo": 1000,
    "Vegetariano": 1200,
    "Barros Luco": 3000
}

# Ingreso de la cantidad de sándwiches por teclado
sandwiches_cliente = {}
print("¡Bienvenido a Sanguchitos!")
print("Por favor, ingrese la cantidad de cada sándwich que desea pedir:")

for tipo in precios_sandwiches:
    cantidad = int(input(f"{tipo}: "))
    sandwiches_cliente[tipo] = cantidad

# Cálculo del total
total = sum(precios_sandwiches[tipo] * cantidad for tipo, cantidad in sandwiches_cliente.items())

# Pregunta si desea entrega a domicilio
print("\n¿Desea entrega a domicilio? (Sí/No): ", end="")
entrega_domicilio = input().strip().lower()

if entrega_domicilio == "si" or entrega_domicilio == "sí":
    total += 1500
    comuna = input("Ingrese la comuna de entrega: ")
    calle = input("Ingrese la calle de entrega: ")
    numero_casa = input("Ingrese el número de casa de entrega: ")
    direccion_entrega = f"{comuna}, {calle} #{numero_casa}"
else:
    direccion_entrega = "No aplica"

# Descuento (si aplica)
codigo_descuento = input("\nIngrese el código de descuento (o deje en blanco si no tiene): ")
if codigo_descuento == "CEBOLLA":
    descuento = 0.10 * total
    total -= descuento
    descuento_texto = f"Descuento del 10%: -${descuento:.2f}"
else:
    descuento_texto = "No aplica"

# Imprimir recibo
print("\n*** Recibo de Compra ***")
print("-" * 30)
for tipo, cantidad in sandwiches_cliente.items():
    subtotal = precios_sandwiches[tipo] * cantidad
    print(f"{tipo:<15} x{cantidad:<5} ${subtotal:.2f}")
print("-" * 30)
print(f"Entrega a domicilio: {direccion_entrega}")
print(f"{descuento_texto:<20} Total: ${total:.2f}")
print("-" * 30)
