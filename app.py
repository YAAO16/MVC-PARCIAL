from flask import Flask, render_template, request, redirect, session, url_for,  flash

from controllers import ctlEmpresas
from controllers import ctlProducto

app = Flask(__name__)



@app.route('/')
def inicio():
    return render_template("views/inicio.html")

@app.route('/entrar',methods=["GET","POST"])
def entrar():
    if request.method == 'GET':
        return render_template("views/entrada.html")
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        #print(email,password)
        #print(email,password)
        consulta = ctlEmpresas.ctlEntrarEmp(email,password)
        flash( consulta[1] )
        
        if consulta[0]:
            return render_template('views/producto/index_producto.html')
        else:
            return render_template("views/entrada.html") 
            
@app.route('/nu_contra', methods=["GET", "POST"])
def nu_contra():
    return render_template("nu_contra.html") 

@app.route('/recuperarp', methods=["GET", "POST"])
def rec_contra():
        if request.method =='GET':
            return render_template('views/rec_contra.html')
        else:
            email = request.form.get('email_form')
    
           
@app.route('/volver', methods=["GET", "POST"])
def volver():
    return render_template("views/inicio.html")

@app.route('/cerrar', methods=["GET", "POST"])
def cerrar():
    session.clear()
    return render_template("views/inicio.html")       

@app.route('/registrar', methods=["GET", "POST"])
def registrar():
    if request.method == 'GET':
        return render_template("views/registros.html")
    else:

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        imagen = request.form['imagen']
        celular = request.form['celular']
        direccion = request.form['direccion']
        descripcion = request.form['descripcion']
        
        consulta = ctlEmpresas.ctlRegistroEmp(name,email,password,imagen,celular,direccion,descripcion)
        flash(consulta[1])
        
        if(consulta[0]):
            return render_template("views/producto/index_producto.html")
        else:
            return render_template("views/registros.html")
            
        


@app.route('/crea_prod', methods=['GET','POST'])
def crea_prod():
    if request.method == 'GET':
        print("mostrando el formulario")
        return render_template("views/producto/crea_prod.html")     
    else:
        print("no pasa el producto")
        name = request.form.get('name_pro')
        descripcion = request.form.get('des_producto')
        precio = request.form.get('pre_productos')
        imagen = request.form.get('img_producto')
        consulta = ctlProducto.ctlRegProduct(name, descripcion, precio, imagen)
        flash(consulta[1])
        if(consulta[0]):
            return render_template("views/producto/crea_prod.html")     
            
 
if __name__ == '__main__':
    app.secret_key = "kamata16angulo"
    app.run(debug=True)