# Precios de los sándwiches
precios_sandwiches = {
    "Churrasco": 1500,
    "Completo": 1000,
    "Vegetariano": 1200,
    "Barros Luco": 3000
}

# Ingreso de la cantidad de sándwiches por teclado
sandwiches_cliente = {}
for tipo in precios_sandwiches:
    cantidad = int(input(f"Ingrese la cantidad de sándwiches {tipo}: "))
    sandwiches_cliente[tipo] = cantidad

# Cálculo del total
total = sum(precios_sandwiches[tipo] * cantidad for tipo, cantidad in sandwiches_cliente.items())

# Pregunta si desea entrega a domicilio
entrega_domicilio = input("¿Desea entrega a domicilio? (Sí/No): ").strip().lower()

if entrega_domicilio == "si" or entrega_domicilio == "sí":
    total += 1500
    direccion_entrega = input("Por favor, ingrese la dirección de entrega: ")
else:
    direccion_entrega = "No aplica"

# Descuento (si aplica)
codigo_descuento = input("Ingrese el código de descuento (o deje en blanco si no tiene): ")
if codigo_descuento == "CEBOLLA":
    descuento = 0.10 * total
    total -= descuento
    print(f"Se aplicó un descuento del 10%: -${descuento:.2f}")

# Mostrar el total a pagar y la información de entrega
print(f"Total a pagar: ${total:.2f}")
print(f"Dirección de entrega: {direccion_entrega}")
