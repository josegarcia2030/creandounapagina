
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from datetime import datetime





app = Flask(__name__)


#conectando la base de datos
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'CORPORACION_NEXUS'
mysql.init_app(app)


@app.route("/")
def home():
    sql = "SELECT * FROM `empleados`"
    conexion = mysql.connect()
    puntero = conexion.cursor()
    puntero.execute(sql)

    empleados = puntero.fetchall()
    #print(empleados)

    conexion.commit()

    return render_template('empleados/index.html', employes = empleados)

@app.route('/create')
def create():
    return render_template('empleados/create.html')


@app.route('/store', methods=["POST"])
def store():

    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']

    now = datetime.now()
    tiempo = now.strftime('%Y%H%M%S')

    if _foto.filename != '':
        nuevoNombreFoto = tiempo + _foto.filename
        _foto.save('uploads/' + nuevoNombreFoto)

    #instruccion sql
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, %s, %s, %s);"
    datos = (_nombre,_correo,nuevoNombreFoto)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()
    return render_template('empleados/index.html')


@app.route('/editar/<int:id>')
def editar(id):

    conexion = mysql.connect()
    puntero = conexion.cursor()
    puntero.execute("SELECT * FROM empleados WHERE id=%s", (id))
    empleados = puntero.fetchall()
    conexion.commit()
    return render_template('empleados/edit.html', employes = empleados)    


@app.route('/destroy/<int:id>')
def destroy(id):
    conexion = mysql.connect()
    puntero =conexion.cursor()
    puntero.execute("DELETE from empleados WHERE id=%s", (id))
    conexion.commit()

    return redirect('/')








if __name__ == '__main__':
    app.run(debug=True, port=5000)