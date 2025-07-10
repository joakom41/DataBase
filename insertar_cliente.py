from operations import Operations
from datetime import datetime

def mostrar_ayuda():
    print("\n=== Ayuda del Sistema ===")
    print("1. Insertar cliente: Agrega un nuevo cliente al sistema")
    print("2. Buscar cliente: Encuentra un cliente por su ID")
    print("3. Actualizar cliente: Modifica la información de un cliente existente")
    print("4. Eliminar cliente: Remueve un cliente del sistema")
    print("5. Buscar por ciudad: Lista todos los clientes de una ciudad")
    print("6. Buscar por fecha: Muestra clientes registrados en una fecha específica")
    print("7. Ver todos los clientes: Muestra la lista completa de clientes")
    print("8. Buscar avanzado: Permite buscar por múltiples criterios")
    print("9. Ordenar clientes: Ordena la lista de clientes por diferentes campos")
    print("0. Salir: Cierra el programa")
    print("\nPresione Enter para continuar...")

def main():
    # Crear una instancia de Operations
    ops = Operations()
    
    while True:
        print("\n=== Sistema de Gestión de Clientes ===")
        print("1. Insertar cliente")
        print("2. Buscar cliente")
        print("3. Actualizar cliente")
        print("4. Eliminar cliente")
        print("5. Buscar por ciudad")
        print("6. Buscar por fecha")
        print("7. Ver todos los clientes")
        print("8. Buscar avanzado")
        print("9. Ordenar clientes")
        print("0. Ayuda")
        print("H. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            try:
                # Insertar cliente
                print("\n=== Insertar Cliente ===")
                cliente = {
                    "nombre": input("Nombre: "),
                    "apellidos": input("Apellidos: "),
                    "calle": input("Calle: "),
                    "numero": input("Número: "),
                    "ciudad": input("Ciudad: "),
                    "fecha_registro": datetime.now()
                }
                ops.validar_cliente(cliente)
                resultado = ops.insert_product(cliente)
                print(f"Cliente insertado con ID: {resultado.inserted_id}")
                
            except ValueError as e:
                print(f"\nError: {e}")
                
        elif opcion == "2":
            # Buscar cliente
            id_cliente = input("Ingrese el ID del cliente a buscar: ")
            cliente = ops.find_products({"_id": id_cliente})
            for c in cliente:
                print("\n=== Cliente Encontrado ===")
                print(f"ID: {c['_id']}")
                print(f"Nombre: {c['nombre']} {c['apellidos']}")
                print(f"Dirección: {c['calle']} {c['numero']}, {c['ciudad']}")
                print(f"Fecha de registro: {c['fecha_registro']}")
                
        elif opcion == "3":
            # Actualizar cliente
            id_cliente = input("Ingrese el ID del cliente a actualizar: ")
            try:
                actualizar = {
                    "nombre": input("Nuevo nombre: "),
                    "apellidos": input("Nuevos apellidos: "),
                    "calle": input("Nueva calle: "),
                    "numero": input("Nuevo número: "),
                    "ciudad": input("Nueva ciudad: ")
                }
                ops.validar_cliente(actualizar)
                resultado = ops.update_product({"_id": id_cliente}, {"$set": actualizar})
                print(f"Clientes actualizados: {resultado.modified_count}")
            except ValueError as e:
                print(f"\nError: {e}")
                
        elif opcion == "4":
            # Eliminar cliente
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            confirmacion = input("¿Está seguro? (s/n): ")
            if confirmacion.lower() == 's':
                resultado = ops.delete_product({"_id": id_cliente})
                print(f"Clientes eliminados: {resultado.deleted_count}")
            else:
                print("Operación cancelada")
                
        elif opcion == "5":
            # Buscar por ciudad
            ciudad = input("Ingrese la ciudad a buscar: ")
            clientes = ops.buscar_por_ciudad(ciudad)
            print(f"\n=== Clientes en {ciudad} ===")
            for c in clientes:
                print(f"- {c['nombre']} {c['apellidos']}")
                
        elif opcion == "6":
            # Buscar por fecha
            try:
                fecha = input("Ingrese la fecha de registro (YYYY-MM-DD): ")
                ops.validar_fecha(fecha)
                clientes = ops.buscar_por_fecha_registro(fecha)
                print(f"\n=== Clientes del {fecha} ===")
                for c in clientes:
                    print(f"- {c['nombre']} {c['apellidos']}")
            except ValueError as e:
                print(f"\nError: {e}")
                
        elif opcion == "7":
            # Ver todos los clientes
            clientes = ops.find_products()
            print("\n=== Lista de Clientes ===")
            for c in clientes:
                print(f"- {c['nombre']} {c['apellidos']} ({c['ciudad']})")
                
        elif opcion == "8":
            # Buscar avanzado
            print("\n=== Búsqueda Avanzada ===")
            criterios = {}
            ciudad = input("Ciudad (Enter para saltar): ")
            if ciudad:
                criterios['ciudad'] = ciudad
                
            fecha_inicio = input("Fecha inicio (YYYY-MM-DD, Enter para saltar): ")
            if fecha_inicio:
                try:
                    ops.validar_fecha(fecha_inicio)
                    criterios['fecha_registro'] = {"$gte": datetime.strptime(fecha_inicio, '%Y-%m-%d')}
                except ValueError:
                    print("Fecha inicio inválida, omitiendo...")
                    fecha_inicio = ""
            
            fecha_fin = input("Fecha fin (YYYY-MM-DD, Enter para saltar): ")
            if fecha_fin:
                try:
                    ops.validar_fecha(fecha_fin)
                    if 'fecha_registro' in criterios:
                        criterios['fecha_registro']['$lte'] = datetime.strptime(fecha_fin, '%Y-%m-%d')
                    else:
                        criterios['fecha_registro'] = {"$lte": datetime.strptime(fecha_fin, '%Y-%m-%d')}
                except ValueError:
                    print("Fecha fin inválida, omitiendo...")
                    fecha_fin = ""
            
            if criterios:
                clientes = ops.buscar_multiple_criterios(criterios)
                print("\n=== Resultados de la Búsqueda ===")
                for c in clientes:
                    print(f"- {c['nombre']} {c['apellidos']} ({c['ciudad']})")
            else:
                print("No se especificaron criterios de búsqueda")
                
        elif opcion == "9":
            # Ordenar clientes
            print("\n=== Ordenar Clientes ===")
            print("1. Por nombre")
            print("2. Por ciudad")
            print("3. Por fecha de registro")
            orden_opcion = input("Seleccione una opción: ")
            orden = 1  # ascendente
            campo = ""
            
            if orden_opcion == "1":
                campo = "nombre"
            elif orden_opcion == "2":
                campo = "ciudad"
            elif orden_opcion == "3":
                campo = "fecha_registro"
            else:
                print("Opción no válida")
                continue
                
            ordenar_por = input("Orden ascendente (A) o descendente (D)? ").upper()
            if ordenar_por == 'D':
                orden = -1
                
            clientes = ops.ordenar_clientes(campo, orden)
            print(f"\n=== Clientes Ordenados por {campo} ===")
            for c in clientes:
                print(f"- {c['nombre']} {c['apellidos']} ({c['ciudad']})")
                
        elif opcion == "0":
            # Ayuda
            mostrar_ayuda()
            
        elif opcion == "H":
            # Salir
            print("¡Hasta luego!")
            ops.db.close()
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")
            
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()