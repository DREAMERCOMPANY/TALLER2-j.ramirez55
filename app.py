from flask import Flask, jsonify, render_template

app = Flask(__name__)

class Perro:
    def __init__(self):
        self.sonido = "Guau"
   
    def hace(self):
        return self.sonido

class Huron:
    def __init__(self):
        self.sonido = "Chirrido"
   
    def hace(self):
        return self.sonido

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perro', methods=['GET'])
def perro():
    perro = Perro()
    return jsonify({"animal": "Perro", "hace": perro.hace()})

@app.route('/huron', methods=['GET'])
def huron():
    huron = Huron()
    return jsonify({"animal": "Hurón", "hace": huron.hace()})

if __name__ == '__main__':
    app.run(debug=True)
