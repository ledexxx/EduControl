from flask import Blueprint, render_template, jsonify
from flask_mysqldb import MySQL

# Crear el Blueprint
dashboard_apoderados_bp = Blueprint('dashboard_apoderados', __name__)

# Variable global para MySQL
mysql = None

# Función de inicialización
def init_dashboard_apoderados(mysql_instance):
    global mysql
    mysql = mysql_instance

# Ruta para el Dashboard de Apoderados
@dashboard_apoderados_bp.route('/dashboard/apoderado')
def dashboard_apoderado():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT 
            u.nombre, 
            COUNT(a.estado) AS total_asistencias,
            SUM(a.estado = 'justificada') AS justificadas
        FROM usuarios u
        LEFT JOIN asistencia a ON u.id = a.id_estudiante
        WHERE u.rol = 'estudiante'
        GROUP BY u.id
    """)
    estudiantes = cursor.fetchall()
    cursor.close()

    return render_template('dashboard_apoderado.html', estudiantes=estudiantes)
