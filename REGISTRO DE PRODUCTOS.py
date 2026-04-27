print("=====REGISTRO DE PRODUCTOS=====")
nombre_producto = input("Ingrese el nombre del producto: ")
sku = input("Ingrese sku: ")
ano_fabricacion = int(input("Ingrese el año de fabricación: "))
cantidad = int(input("Ingrese cantidad"))

ano_actual = 2026
vida_util = ano_fabricacion - ano_actual

print("=====ENTREGA DE INFORMACION=====")
print(f"El nombre del producto es: {nombre_producto}")
print(f"El sku es: {sku}")
print(f"El año de fabricación es: {ano_fabricacion}")
print(f"La cantidad es: {cantidad}")
