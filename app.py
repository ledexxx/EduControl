from flask import Flask, render_template
from flask_mysqldb import MySQL
from components.registrar import registrar_bp, init_registrar
from components.login import login_bp, init_login
from components.dashboard import dashboard_bp, init_dashboard
from components.dashboard_apoderados import dashboard_apoderados_bp, init_dashboard_apoderados


app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'educontrol'

# Inicializar MySQL
mysql = MySQL(app)

# Blueprints
init_registrar(mysql)
init_login(mysql)
init_dashboard(mysql)
init_dashboard_apoderados(mysql)
app.register_blueprint(registrar_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp)
app.register_blueprint(dashboard_apoderados_bp)
app.register_blueprint(login_bp, url_prefix='/auth')
# Rutas
@app.route('/')
def index():
    return render_template('Inicio.html')

@app.route('/auth')
def login():
    return render_template('portal.html')

@app.route('/qr')
def qr():
    return render_template('qr.html')

@app.route('/crear_cuenta')
def crear_cuenta():
    return render_template('registro.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard/apoderado')
def dashboard_apoderado():
    return render_template('dashboard_apoderado.html')

@app.route('/admin/panel')
def admin_panel():
    return render_template('panel.html')


if __name__ == '__main__':
    app.run(debug=True)
