from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ejemplo'

mysql = MySQL(app)

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios")
    data = cur.fetchall()
    cur.close()
    return jsonify(list(data))
    

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    nuevo_usuario = request.get_json()
    nombre = nuevo_usuario['nombre']
    edad = nuevo_usuario['edad']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", (nombre, edad))
    mysql.connection.commit()
    cur.close()

    return jsonify({'mensaje': 'Usuario agregado correctamente'})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
