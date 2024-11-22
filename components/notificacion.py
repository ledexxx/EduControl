import smtplib
from email.mime.text import MIMEText

def enviar_correo_apoderado(email, nombre, fecha):
    cuerpo = f"Estimado apoderado,\n\nEl estudiante {nombre} no asistió el día {fecha}. Por favor, comuníquese con la institución si necesita más información.\n\nSaludos,\nEduControl"
    mensaje = MIMEText(cuerpo)
    mensaje['Subject'] = "Notificación de Inasistencia"
    mensaje['From'] = "tu_correo@institucion.com"
    mensaje['To'] = email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login("tu_correo@institucion.com", "tu_contraseña")
        server.send_message(mensaje)
