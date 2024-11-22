@asistencia_bp.route('/reporte', methods=['GET'])
def obtener_reporte():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT u.nombre, a.fecha, a.estado
        FROM asistencia a
        JOIN usuarios u ON a.id_estudiante = u.id
        WHERE u.rol = 'estudiante'
        ORDER BY a.fecha DESC
    """)
    reportes = cursor.fetchall()
    cursor.close()

    return jsonify([
        {"nombre": r[0], "fecha": r[1].strftime("%Y-%m-%d"), "estado": r[2]}
        for r in reportes
    ])
