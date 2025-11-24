def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    Parametros:
        inventario (list)
        ruta (str)
        incluir_header (bool)
    Retorno:
        None
    """
    if not inventario:
        print("No se puede guardar: inventario vacío.")
        return

    try:
        with open(ruta, "w", encoding="utf-8") as f:
            if incluir_header:
                f.write("nombre,precio,cantidad\n")

            for p in inventario:
                linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
                f.write(linea)

        print(f"Inventario guardado en: {ruta}")

    except PermissionError:
        print("Error: no se pudo escribir en el archivo (permiso denegado).")
    except Exception as e:
        print(f"Error inesperado al guardar: {e}")


def cargar_csv(ruta):
    """
    Carga un archivo CSV y retorna una lista de productos.
    Parametros:
        ruta (str)
    Retorno:
        lista de diccionarios con productos
    """
    inventario_cargado = []
    errores = 0

    try:
        with open(ruta, "r", encoding="utf-8") as f:
            lineas = f.readlines()

        if not lineas:
            print("El archivo está vacío.")
            return [], 0

        header = lineas[0].strip().split(",")

        if header != ["nombre", "precio", "cantidad"]:
            print("Encabezado inválido. Se esperaba: nombre,precio,cantidad")
            return [], 0

        for linea in lineas[1:]:
            partes = linea.strip().split(",")

            if len(partes) != 3:
                errores += 1
                continue

            nombre, precio, cantidad = partes

            try:
                precio = float(precio)
                cantidad = int(cantidad)

                if precio < 0 or cantidad < 0:
                    raise ValueError()

                inventario_cargado.append({
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                })

            except ValueError:
                errores += 1

        return inventario_cargado, errores

    except FileNotFoundError:
        print("Archivo no encontrado.")
        return [], 0
    except UnicodeDecodeError:
        print("Error de codificación del archivo.")
        return [], 0
    except Exception as e:
        print(f"Error inesperado al cargar: {e}")
        return [], 0
