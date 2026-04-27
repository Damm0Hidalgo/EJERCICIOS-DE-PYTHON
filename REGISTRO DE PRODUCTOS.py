print("=====REGISTRO DE PRODUCTOS=====")

nombre_producto = input("Ingrese el nombre del producto: ")
sku = input("Ingrese sku: ")
ano_fabricacion = int(input("Ingrese el año de fabricación: "))
cantidad = int(input("Ingrese cantidad: "))
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingresa tu edad: "))
correo = input("Ingresa tu correo: ")
ano_actual = 2026
vida_util = ano_actual - ano_fabricacion

print("=====ENTREGA DE INFORMACION=====")
print(f"El nombre del producto es: {nombre_producto}")
print(f"El sku es: {sku}")
print(f"El año de fabricación es: {ano_fabricacion}")
print(f"La cantidad es: {cantidad}")
print(f"La vida util del producto es: {vida_util}")
print(f"El nombre del cliente es: {nombre}")
print(f"La edad de {nombre} es: {edad}")
print(f"Su correo es: {correo}")