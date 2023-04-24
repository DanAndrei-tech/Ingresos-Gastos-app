from flask import Flask

app = Flask(__name__)

from app_ingresos_gastos.routes import *

#inicializar el servidor de Flask
# en mac: export
# en windows: set FLASK_APP=main.py

#flask --app main --debug run