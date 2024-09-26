# Importar  paquetes necesarios
from flask import Flask, json, jsonify, request
from flask_cors import CORS
import json

# Crear la aplicación Flask
app = Flask(__name__)
CORS(app)

# Variable global para almacenar los productos
productos = []

# Función para cargar los productos desde un archivo JSON
def cargar_productos():
    global productos
    with open('productos.json', 'r') as file:
        productos = json.load(file)

# Función para guardar los productos en un archivo JSON
def guardar_productos():
    with open('productos.json', 'w') as file:
        json.dump(productos, file)

# Ruta de la API para obtener la lista de productos filtrados
@app.route('/productos', methods=['GET'])
def get_productos():
    # Obtener los parámetros de consulta de la URL
    nombre = request.args.get('nombre')
    serie_producto = request.args.get('serie_producto')
    marca = request.args.get('marca')
    codigo = request.args.get('codigo')

    # Crear una copia de la lista de productos para filtrarlos
    productos_filtrados = productos.copy()

    # Aplicar los filtros según los parámetros de consulta
    if nombre:
        productos_filtrados = [producto for producto in productos_filtrados if producto['nombre'] == nombre]
    if serie_producto:
        productos_filtrados = [producto for producto in productos_filtrados if producto['serie_producto'] == serie_producto]
    if marca:
        productos_filtrados = [producto for producto in productos_filtrados if producto['marca'] == marca]
    if codigo:
        productos_filtrados = [producto for producto in productos_filtrados if producto['codigo'] == codigo]

    # Devolver la lista de productos filtrados como respuesta JSON
    return jsonify(productos_filtrados)

# Ruta de la API para agregar un nuevo producto
@app.route('/productos', methods=['POST'])
def agregar_producto():
    # Obtener el nuevo producto desde el cuerpo de la solicitud en formato JSON
    nuevo_producto = request.json
    # Agregar el nuevo producto a la lista de productos
    productos.append(nuevo_producto)
    # Guardar los productos actualizados en el archivo JSON
    guardar_productos()
    # Devolver una respuesta JSON con un mensaje de éxito
    return jsonify({"mensaje": "Producto agregado exitosamente"}), 201

# Ruta de la API para obtener un producto por su ID
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    # Buscar el producto con el ID especificado en la lista de productos
    producto = obtener_producto_por_id(id)
    if producto:
        # Devolver el producto como respuesta JSON
        return jsonify(producto)
    else:
        # Si no se encuentra el producto, devolver un mensaje de error
        return jsonify({"mensaje": "Producto no encontrado"}), 404

# Ruta de la API para eliminar un producto por su ID
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    # Buscar el producto con el ID especificado en la lista de productos
    for producto in productos:
        if producto["id"] == id:
            # Eliminar el producto de la lista
            productos.remove(producto)
            # Guardar los productos actualizados en el archivo JSON
            guardar_productos()
            # Devolver una respuesta JSON con un mensaje de éxito
            return jsonify({"mensaje": "Producto eliminado exitosamente"})
    # Si no se encuentra el producto, devolver un mensaje de error
    return jsonify({"mensaje": "Producto no encontrado"}), 404

# Ruta de la API para actualizar un producto por su ID
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    # Obtener el producto actualizado desde el cuerpo de la solicitud en formato JSON
    nuevo_producto = request.json
    producto_actualizado = False
    
    

# Función para obtener un producto por su ID en la lista de productos
def obtener_producto_por_id(id):
    for producto in productos:
        if producto["id"] == id:
            return producto
    return None

# Cargar los productos al inicio de la aplicación
if __name__ == '__main__':
    cargar_productos()
    app.run(port=3000, debug=True)