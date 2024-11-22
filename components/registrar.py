from flask import Blueprint, render_template, request, jsonify 
import bcrypt

# Definir Blueprint
registrar_bp = Blueprint('registrar', __name__)

# Variable global para MySQL
mysql = None

# Función de inicialización
def init_registrar(mysql_instance):
    global mysql
    mysql = mysql_instance

# Valores válidos para el campo "rol"
ROLES_VALIDOS = ['profesor', 'estudiante', 'apoderado']

# Ruta para registrar usuarios
@registrar_bp.route('/crear_cuenta', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'GET':
        # Renderizar el formulario de registro
        return render_template('crear_cuenta.html')

    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombre = request.form.get('nombre')
            email = request.form.get('email')
            password = request.form.get('password')
            confirm_password = request.form.get('confirm_password')
            t_usuario = request.form.get('t_usuario')

            # Validar contraseñas
            if password != confirm_password:
                return jsonify({"mensaje": "Las contraseñas no coinciden"}), 400

            # Validar tipo de usuario
            if t_usuario not in ROLES_VALIDOS:
                return jsonify({"mensaje": "El tipo de usuario no es válido"}), 400

            # Encriptar la contraseña
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            # Insertar datos en la base de datos
            cursor = mysql.connection.cursor()
            cursor.execute("""
                INSERT INTO usuarios (nombre, email, contraseña, rol, creado_en)
                VALUES (%s, %s, %s, %s, NOW())
            """, (nombre, email, hashed_password, t_usuario))
            mysql.connection.commit()
            cursor.close()

            return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

        except Exception as e:
            return jsonify({"mensaje": f"Error al registrar usuario: {str(e)}"}), 500
