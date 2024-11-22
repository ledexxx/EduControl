from flask import Blueprint, request, jsonify
from components.notificacion import enviar_correo_apoderado

asistencia_bp = Blueprint('asistencia', __name__)

def init_asistencia(mysql_instance):
    global mysql
    mysql = mysql_instance

@asistencia_bp.route('/registrar_asistencia', methods=['POST'])
def registrar_asistencia():
    data = request.json
    id_estudiante = data['id_estudiante']
    estado = data['estado']

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT nombre, email FROM usuarios WHERE id = %s", (id_estudiante,))
    estudiante = cursor.fetchone()

    if not estudiante:
        return jsonify({"mensaje": "Estudiante no encontrado"}), 404

    if estado == 'ausente':
        enviar_correo_apoderado(estudiante[1], estudiante[0], "HOY")

    cursor.execute("INSERT INTO asistencia (id_estudiante, fecha, estado) VALUES (%s, NOW(), %s)", 
                   (id_estudiante, estado))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensaje": "Asistencia registrada con éxito"})
