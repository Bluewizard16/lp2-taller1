from flask import Flask, render_template
from datos import productos

# Creamos el objeto de la clase Flask
app = Flask(__name__)

# Definimos las rutas
@app.route("/")
def index():
    return render_template("index.html", productos=productos)

@app.route("/producto/<string:nombre>")
def producto(nombre):
    producto = [p for p in productos if p['nombre'] == nombre]
    return render_template("producto.html", producto=producto[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)