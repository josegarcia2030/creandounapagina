from distutils.log import debug
from flask import Flask, render_template, request
from flaskext.mysql import MySQL






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

    #instruccion sql
    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'rasek2030', 'rasek2030@gmail.com', 'foto1Null.jpg');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

    return render_template('empleados/index.html')




if __name__ == '__main__':
    app.run(debug=True, port=5000)