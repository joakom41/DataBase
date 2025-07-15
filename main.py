from insertar_cliente import menu_cliente
from producto import menu_producto
from pedido import menu_pedido

def main():
    while True:
        print("\n=== Menú General ComercioTech ===")
        print("1. Gestionar Clientes")
        print("2. Gestionar Productos")
        print("3. Gestionar Pedidos")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_cliente()
        elif opcion == "2":
            menu_producto()
        elif opcion == "3":
            menu_pedido()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
