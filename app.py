from flask import Flask, render_template
from flask_mysqldb import MySQL
from components.registrar import registrar_bp, init_registrar
from components.login import login_bp, init_login



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
app.register_blueprint(registrar_bp, url_prefix='/auth')
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

if __name__ == '__main__':
    app.run(debug=True)
