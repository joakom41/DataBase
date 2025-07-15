from operations import Operations
from datetime import datetime

def menu_pedido():
    ops = Operations()
    while True:
        print("\n=== Sistema de Gestión de Pedidos ===")
        print("1. Insertar pedido")
        print("2. Buscar pedidos por código cliente")
        print("3. Actualizar pedido")
        print("4. Eliminar pedido")
        print("5. Ver todos los pedidos")
        print("H. Salir")
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            try:
                print("\n=== Insertar Pedido ===")
                pedido = {
                    "codigo_pedido": input("Código Pedido: "),
                    "codigo_cliente": input("Código Cliente: "),
                    "fecha_pedido": datetime.strptime(input("Fecha Pedido (YYYY-MM-DD): "), '%Y-%m-%d'),
                    "productos": [],  # Aquí puedes mejorar para agregar productos uno a uno
                    "total_compra": float(input("Total Compra: ")),
                    "metodo_pago": input("Método de Pago: ")
                }
                # Para agregar productos (opcional)
                agregar_productos = input("¿Desea agregar productos? (s/n): ")
                while agregar_productos.lower() == "s":
                    codigo_producto = input("Código producto: ")
                    nombre_producto = input("Nombre producto: ")
                    cantidad = int(input("Cantidad: "))
                    precio_unitario = float(input("Precio unitario: "))
                    total_producto = cantidad * precio_unitario
                    pedido["productos"].append({
                        "codigo_producto": codigo_producto,
                        "nombre": nombre_producto,
                        "cantidad": cantidad,
                        "precio_unitario": precio_unitario,
                        "total_comprado": total_producto
                    })
                    agregar_productos = input("Agregar otro producto? (s/n): ")

                resultado = ops.insert_product(pedido, "pedidos")
                print(f"Pedido insertado con ID: {resultado.inserted_id}")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "2":
            codigo_cliente = input("Ingrese código del cliente para buscar pedidos: ")
            pedidos = ops.buscar_por_codigo_cliente(codigo_cliente, "pedidos")
            pedidos_lista = list(pedidos)
            if len(pedidos_lista) > 0:
                print("\n=== Pedidos Encontrados ===")
                for p in pedidos_lista:
                    print(f"ID: {p['_id']}")
                    print(f"Código Pedido: {p['codigo_pedido']}")
                    print(f"Código Cliente: {p['codigo_cliente']}")
                    print(f"Fecha Pedido: {p['fecha_pedido']}")
                    print(f"Productos:")
                    for prod in p['productos']:
                        print(f" - {prod['nombre']} x{prod['cantidad']} = {prod['total_comprado']}")
                    print(f"Total Compra: {p['total_compra']}")
                    print(f"Método Pago: {p['metodo_pago']}")
            else:
                print("No se encontraron pedidos para ese cliente.")

        elif opcion == "3":
            codigo_pedido = input("Ingrese código del pedido a actualizar: ")
            pedidos = ops.buscar_por_codigo_pedido(codigo_pedido, "pedidos")
            pedidos_lista = list(pedidos)
            if len(pedidos_lista) > 0:
                try:
                    actualizar = {
                        "codigo_cliente": input("Nuevo código cliente: "),
                        "fecha_pedido": datetime.strptime(input("Nueva fecha pedido (YYYY-MM-DD): "), '%Y-%m-%d'),
                        "total_compra": float(input("Nuevo total compra: ")),
                        "metodo_pago": input("Nuevo método pago: ")
                    }
                    resultado = ops.update_product({"codigo_pedido": codigo_pedido}, {"$set": actualizar}, "pedidos")
                    print(f"Pedidos actualizados: {resultado.modified_count}")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("No se encontró pedido con ese código.")

        elif opcion == "4":
            codigo_pedido = input("Ingrese código del pedido a eliminar: ")
            resultado = ops.delete_product({"codigo_pedido": codigo_pedido}, "pedidos")
            print(f"Pedidos eliminados: {resultado.deleted_count}")

        elif opcion == "5":
            pedidos = ops.find_products(None, "pedidos")
            print("\n=== Lista de Pedidos ===")
            for p in pedidos:
                print(f"- Pedido {p['codigo_pedido']} Cliente: {p['codigo_cliente']} Fecha: {p['fecha_pedido']} Total: {p['total_compra']}")

        elif opcion.upper() == "H":
            print("Saliendo del sistema de pedidos...")
            ops.db.close()
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    menu_pedido()
