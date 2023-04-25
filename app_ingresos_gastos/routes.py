from app_ingresos_gastos import app
from flask import render_template

@app.route("/")
def index():
    datos = [
        {
        'fecha':"24/04/2023",
        'concepto':'Ropa',
        'monto':'150',
    },
         {
        'fecha':"24/04/2023",
        'concepto':'Salario',
        'monto':'1500',
    },
         {
        'fecha':"24/04/2023",
        'concepto':'Ocio',
        'monto':'12€',
    }
    ]
    return render_template("index.html",data = datos,title = 'Lista')

@app.route("/new")
def create():
    return render_template("new.html",title="Registro",tipoAccion = 'Registro',tipoBoton='Guardar')

@app.route("/update")
def edit():
   return render_template("update.html",title = 'Actualizar',tipoAccion='Actualizar',tipoBoton='Editar')

@app.route("/delete")
def remove():
   return render_template("delete.html",title = 'Eliminar')