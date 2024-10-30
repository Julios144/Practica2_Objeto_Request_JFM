from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")

def index():
    
    return render_template('index.html')
    
@app.route("/proceso",methods=['POST'])
def proceso():
    #nombre
    nombre=request.form.get("nombre")
    #apellidos
    apellidos=request.form.get("apellidos")
    #correo electronico
    correo=request.form.get("correo")
    #contraseña
    contraseña=request.form.get("contraseña")
    
    return render_template("salida.html",nom=nombre,ape=apellidos,co=correo,contra=contraseña)

if __name__ == "__main__":
    app.run(debug=True)