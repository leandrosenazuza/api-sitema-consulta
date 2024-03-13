from flask.globals import request
from models.pacientes import Pacientes
from flask import Flask, render_template
import requests

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods = ["GET", "post"])
def buscar():
    pacientes = Pacientes(request.form["CPF"],"")
    return render_template("index.html",cpf = pacientes.cpf)


if __name__=="__main__":
    app.run(debug=True)