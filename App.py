
from Servicios import (
    agregar_producto,
    mostrar_inventario,
    buscar_producto,
    actualizar_producto,
    eliminar_producto,
    calcular_estadisticas,
)

from Archivo import guardar_csv, cargar_csv


def pedir_float(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor < 0:
                print("El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número válido.")


def pedir_int(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor < 0:
                print("No puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Debe ingresar un número entero.")


def main():
    inventario = []

    while True:
        print("\nMENU PRINCIPAL")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = pedir_float("Precio: ")
            cantidad = pedir_int("Cantidad: ")
            agregar_producto(inventario, nombre, precio, cantidad)
            print("Producto agregado.")

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            producto = buscar_producto(inventario, nombre)
            if producto:
                print(producto)
            else:
                print("No encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")
            if not buscar_producto(inventario, nombre):
                print("Producto no encontrado.")
                continue

            nuevo_precio = pedir_float("Nuevo precio: ")
            nueva_cantidad = pedir_int("Nueva cantidad: ")

            actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad)
            print("Producto actualizado.")

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            if eliminar_producto(inventario, nombre):
                print("Producto eliminado.")
            else:
                print("No encontrado.")

        elif opcion == "6":
            est = calcular_estadisticas(inventario)
            if not est:
                print("Inventario vacío.")
            else:
                print("Unidades totales:", est["unidades_totales"])
                print("Valor total:", est["valor_total"])
                print("Producto más caro:", est["producto_mas_caro"])
                print("Producto con mayor stock:", est["producto_mayor_stock"])

        elif opcion == "7":
            ruta = input("Ruta del archivo CSV a guardar: ")
            guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Ruta del archivo CSV a cargar: ")

            nuevos, errores = cargar_csv(ruta)
            if not nuevos:
                continue

            print(f"Se cargaron {len(nuevos)} productos.")
            print(f"Filas inválidas omitidas: {errores}")

            decision = input("¿Sobrescribir inventario actual? (S/N): ").upper()

            if decision == "S":
                inventario = nuevos
                print("Inventario reemplazado.")
            else:
                for p in nuevos:
                    existente = buscar_producto(inventario, p["nombre"])
                    if existente:
                        existente["cantidad"] += p["cantidad"]
                        existente["precio"] = p["precio"]
                    else:
                        inventario.append(p)
                print("Inventario fusionado.")

        elif opcion == "9":
            print("Fin del programa.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
