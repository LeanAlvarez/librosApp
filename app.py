from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_mysqldb import MySQL #importo la bbdd


#inicializacion de la app
app = Flask(__name__)

#settings
app.secret_key = 'miclavesecreta'


#conexion bbdd
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'app1'
mysql = MySQL(app)


#Creacion de Rutas
@app.route('/')
def Index():
    return render_template('index.html')



@app.route('/ingresa', methods=["POST"])
def Home():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasenia = request.form['contrasenia']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE nombre = %s and dni = %s', (usuario, contrasenia))
        data = cur.fetchall()
        if len(data) < 1:
            flash('El usuario o la contraseña no coinciden, intenta de nuevo!')   
            return redirect(url_for('Index'))
        elif data[0][1] and data [0][3]:
            return render_template('home.html', data = data)

            
        

        
        
        




if __name__ == '__main__':
    app.run(port=3000, debug=True)