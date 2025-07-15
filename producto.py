from operations import Operations

def menu_producto():
    ops = Operations()
    while True:
        print("\n=== Sistema de Gestión de Productos ===")
        print("1. Insertar producto")
        print("2. Buscar producto por código")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Ver todos los productos")
        print("H. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            try:
                print("\n=== Insertar Producto ===")
                producto = {
                    "codigo_producto": input("Código Producto: "),
                    "nombre": input("Nombre: "),
                    "precio": float(input("Precio: ")),
                    "stock": int(input("Stock: ")),
                    "estado": input("Estado: ")
                }
                # Aquí podrías agregar validaciones para producto
                resultado = ops.insert_product(producto, "productos")
                print(f"Producto insertado con ID: {resultado.inserted_id}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "2":
            codigo = input("Ingrese código del producto: ")
            productos = ops.buscar_por_codigo_producto(codigo, "productos")
            productos_lista = list(productos)
            if len(productos_lista) > 0:
                print("\n=== Producto Encontrado ===")
                for p in productos_lista:
                    print(f"ID: {p['_id']}")
                    print(f"Código: {p['codigo_producto']}")
                    print(f"Nombre: {p['nombre']}")
                    print(f"Precio: {p['precio']}")
                    print(f"Stock: {p['stock']}")
                    print(f"Estado: {p['estado']}")
            else:
                print("No se encontró producto con ese código.")

        elif opcion == "3":
            codigo = input("Ingrese código del producto a actualizar: ")
            productos = ops.buscar_por_codigo_producto(codigo, "productos")
            productos_lista = list(productos)
            if len(productos_lista) > 0:
                try:
                    actualizar = {
                        "nombre": input("Nuevo nombre: "),
                        "precio": float(input("Nuevo precio: ")),
                        "stock": int(input("Nuevo stock: ")),
                        "estado": input("Nuevo estado: ")
                    }
                    resultado = ops.update_product({"codigo_producto": codigo}, {"$set": actualizar}, "productos")
                    print(f"Productos actualizados: {resultado.modified_count}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("No se encontró producto con ese código.")

        elif opcion == "4":
            codigo = input("Ingrese código del producto a eliminar: ")
            resultado = ops.delete_product({"codigo_producto": codigo}, "productos")
            print(f"Productos eliminados: {resultado.deleted_count}")

        elif opcion == "5":
            productos = ops.find_products(None, "productos")
            print("\n=== Lista de Productos ===")
            for p in productos:
                print(f"- {p['codigo_producto']} | {p['nombre']} | Precio: {p['precio']} | Stock: {p['stock']} | Estado: {p['estado']}")

        elif opcion.upper() == "H":
            print("Saliendo del sistema de productos...")
            ops.db.close()
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_producto()
