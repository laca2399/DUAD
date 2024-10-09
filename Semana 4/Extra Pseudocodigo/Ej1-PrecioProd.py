precio_producto = float(input("Ingrese el precio del producto "))
if (precio_producto < 100):
    descuento = precio_producto * 0.02
else:
    descuento = precio_producto * 0.1
precio_final = precio_producto - descuento
print(f"El precio final es {precio_final}")