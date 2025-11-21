def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
    Parametros:
        inventario (list): lista de diccionarios.
        nombre (str): nombre del producto.
        precio (float): precio del producto.
        cantidad (int): cantidad disponible.
    Retorno:
        None
    """
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    Parametros:
        inventario (list)
    Retorno:
        None
    """
    if not inventario:
        print("Inventario vacío.")
        return

    print("\nInventario actual:")
    for p in inventario:
        print(f"- {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre.
    Parametros:
        inventario (list)
        nombre (str)
    Retorno:
        dict si existe, None si no existe
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto existente.
    Parametros:
        inventario (list)
        nombre (str)
        nuevo_precio (float o None)
        nueva_cantidad (int o None)
    Retorno:
        bool indicando si se actualizó
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        return False

    if nuevo_precio is not None:
        producto["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        producto["cantidad"] = nueva_cantidad

    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto del inventario.
    Parametros:
        inventario (list)
        nombre (str)
    Retorno:
        bool indicando si se eliminó
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        return False

    inventario.remove(producto)
    return True


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario.
    Parametros:
        inventario (list)
    Retorno:
        dict con unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock
    """
    if not inventario:
        return None

    unidades_totales = sum(p["cantidad"] for p in inventario)

    subtotal = lambda p: p["precio"] * p["cantidad"]
    valor_total = sum(subtotal(p) for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": producto_mas_caro,
        "producto_mayor_stock": producto_mayor_stock
    }

    
    