@asistencia_bp.route('/reporte/por_fecha', methods=['POST'])
def reporte_por_fecha():
    data = request.json
    fecha = data['fecha']  # Debe estar en formato 'YYYY-MM-DD'

    cursor = mysql.connection.cursor()
    cursor.execute("""
        SELECT u.nombre, a.fecha, a.estado
        FROM asistencia a
        JOIN usuarios u ON a.id_estudiante = u.id
        WHERE DATE(a.fecha) = %s
        ORDER BY a.fecha DESC
    """, (fecha,))
    reportes = cursor.fetchall()
    cursor.close()

    return jsonify([
        {"nombre": r[0], "fecha": r[1].strftime("%Y-%m-%d"), "estado": r[2]}
        for r in reportes
    ])
