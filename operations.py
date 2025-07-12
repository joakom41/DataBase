from database import Database
from datetime import datetime

class Operations:
    def __init__(self):
        self.db = Database()
    
    def insert_product(self, product_data):
        collection = self.db.get_collection('clientes')
        return collection.insert_one(product_data)
    
    def find_products(self, filter=None):
        collection = self.db.get_collection('clientes')
        return collection.find(filter or {})
    
    def update_product(self, filter, update):
        collection = self.db.get_collection('clientes')
        return collection.update_one(filter, update)
    
    def delete_product(self, filter):
        collection = self.db.get_collection('clientes')
        return collection.delete_one(filter)
    
    def buscar_por_ciudad(self, ciudad):
        collection = self.db.get_collection('clientes')
        return collection.find({"ciudad": ciudad})
    
    def buscar_por_fecha_registro(self, fecha):
        collection = self.db.get_collection('clientes')
        return collection.find({"fecha_registro": fecha})
    
    def buscar_por_codigo_producto(self, codigo):
        collection = self.db.get_collection('clientes')
        return collection.find({"codigo": codigo})
    
    def buscar_por_rango_fechas(self, fecha_inicio, fecha_fin):
        collection = self.db.get_collection('clientes')
        return collection.find({
            "fecha_registro": {
                "$gte": fecha_inicio,
                "$lte": fecha_fin
            }
        })
    
    def buscar_multiple_criterios(self, criterios):
        collection = self.db.get_collection('clientes')
        return collection.find(criterios)
    
    def ordenar_clientes(self, campo, orden=1):
        collection = self.db.get_collection('clientes')
        return collection.find().sort(campo, orden)
    
    def buscar_por_nombre(self, nombre):
        collection = self.db.get_collection('clientes')
        return collection.find({"nombre": {"$regex": f".*{nombre}.*", "$options": "i"}})
    
    def validar_cliente(self, cliente_data):
        required_fields = ['nombre', 'apellidos', 'calle', 'numero', 'ciudad']
        if not all(field in cliente_data for field in required_fields):
            raise ValueError("Faltan campos obligatorios")
        if not isinstance(cliente_data['nombre'], str) or not isinstance(cliente_data['apellidos'], str):
            raise ValueError("Nombre y apellidos deben ser texto")
        if not cliente_data['numero'].isdigit():
            raise ValueError("El número debe ser numérico")
        if len(cliente_data['nombre']) > 50 or len(cliente_data['apellidos']) > 50:
            raise ValueError("Nombre o apellidos demasiado largos")
        if not cliente_data['ciudad'].isalpha():
            raise ValueError("La ciudad debe contener solo letras")
        return True
    
    def validar_fecha(self, fecha_str):
        try:
            datetime.strptime(fecha_str, '%Y-%m-%d')
            return True
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD")
        
    def delete_product(self, filter):
        collection = self.db.get_collection('clientes')
        return collection.delete_one(filter)