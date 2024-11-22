import qrcode
import io
@app.route('/generar_qr/<int:id_estudiante>', methods=['GET'])
def generar_qr(id_estudiante):
    qr_data = f"educontrol-{id_estudiante}"
    img = qrcode.make(qr_data)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')
