# Importar los  paquetes necesarios
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import datetime
import requests

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)

# Definir la clase Tarjeta para representar una cuenta bancaria
class Tarjeta:
    def __init__(self, cliente, num_tarjeta, monto, clave):
        self.cliente = cliente
        self.num_tarjeta = num_tarjeta
        self.monto = monto
        self.clave = clave

# Definir la clase BankDB para simular una base de datos bancaria
class BankDB:
    def __init__(self):
        self.cuentas = [
            Tarjeta("Juan Pérez", "1111-1111-1111", 10000000, "1234"),
            Tarjeta("María López", "2222-2222-2222", 50000000, "5678"),
            Tarjeta("Rosa Marquez", "3333-3333-3333", 50000000, "6789"),
            Tarjeta("Elver Gruñon", "4444-4444-4444", 5, "2222")
        ]

    def obtener_cuenta(self, num_tarjeta, clave):
        for cuenta in self.cuentas:
            if cuenta.num_tarjeta == num_tarjeta and cuenta.clave == clave:
                return cuenta
        return None

# Crear una instancia de BankDB para simular la base de datos
bank_db = BankDB()

# Ruta de la API para obtener la lista de cuentas bancarias
@app.route('/cuentas', methods=['GET'])
def obtener_cuentas():
    cuentas = [cuenta.__dict__ for cuenta in bank_db.cuentas]
    return jsonify(cuentas)

# Ruta de la API para realizar una compra con una cuenta bancaria
@app.route('/compra', methods=['POST'])
def realizar_compra():
    datos_compra = request.json
    cuenta = bank_db.obtener_cuenta(datos_compra.get('num_tarjeta'), datos_compra.get('clave'))
    if cuenta:
        producto_id = datos_compra.get('producto_id')
        producto = obtener_producto_por_id(producto_id)
        if producto:
            precio_producto = producto.get('precio')
            if cuenta.monto >= precio_producto:
                cuenta.monto -= precio_producto
                eliminar_producto(producto)  # Eliminar producto automáticamente
                
                # Actualizar el saldo y hora de la compra
                nuevo_saldo = cuenta.monto
                hora_compra = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Crear la respuesta con los nuevos datos
                respuesta = {
                    "mensaje": "Compra realizada exitosamente",
                    "producto": producto,
                    "nuevo_saldo": nuevo_saldo,
                    "hora_compra": hora_compra
                }
                
                return jsonify(respuesta)
            else:
                return jsonify({"mensaje": "Saldo insuficiente en la cuenta"}), 400
        else:
            return jsonify({"mensaje": "Producto no encontrado"}), 404
    else:
        return jsonify({"mensaje": "Cuenta no válida o clave incorrecta"}), 401

# Función para obtener un producto por su ID desde la API de productos
def obtener_producto_por_id(id):
    response = requests.get('http://localhost:3000/productos')
    if response.status_code == 200:
        productos = response.json()
        for producto in productos:
            if producto["id"] == id:
                return producto
    return None

# Función para eliminar un producto de la API de productos
def eliminar_producto(producto):
    url = 'http://localhost:3000/productos/{}'.format(producto["id"])
    response = requests.delete(url)
    if response.status_code != 200:
        print("Error al eliminar el producto")

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(port=4000, debug=True)