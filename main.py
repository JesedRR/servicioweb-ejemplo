from flask import Flask, jsonify, request, render_template

#Iniciamos Flask, el servidor
app = Flask(__name__)

from products import products

#Creamos rutas

@app.route('/products')
def getProducts():
    return jsonify({"products": products})



@app.route('/products/<string:product_name>')
def detProductByName(product_name):
    return 'El articulo esta registrado'

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.form['name'],
        "price": request.form['price'],
        "quantity": request.form['quantity']
    }
    products.append(new_product)
    return 'Producto agregado correctamente'

@app.route('/')
def index():
    return render_template('index.html', products=products)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)