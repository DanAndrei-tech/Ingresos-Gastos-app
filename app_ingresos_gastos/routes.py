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
    return render_template("index.html",data = datos)

@app.route("/new")
def create():
    return render_template("new.html")