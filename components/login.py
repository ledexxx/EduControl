from flask import Blueprint, request, jsonify
import bcrypt

login_bp = Blueprint('login', __name__)

# Variable global para MySQL
mysql = None

def init_login(mysql_instance):
    global mysql
    mysql = mysql_instance

@login_bp.route('/login', methods=['POST'])
def login():
    try:
        # Obtener los datos de la solicitud
        data = request.json
        email = data.get('email')
        contraseña = data.get('contraseña')

        # Validar que los campos no estén vacíos
        if not email or not contraseña:
            return jsonify({"mensaje": "Por favor, completa todos los campos"}), 400

        # Consultar en la base de datos
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id, nombre, contraseña FROM usuarios WHERE email = %s", (email,))
        usuario = cursor.fetchone()
        cursor.close()

        # Validar credenciales
        if usuario and bcrypt.checkpw(contraseña.encode('utf-8'), usuario[2].encode('utf-8')):
            return jsonify({"mensaje": "Inicio de sesión exitoso", "usuario": usuario[1]})
        else:
            return jsonify({"mensaje": "Credenciales inválidas"}), 401

    except Exception as e:
        return jsonify({"mensaje": f"Error en el servidor: {str(e)}"}), 500