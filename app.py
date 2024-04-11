from flask import Flask, render_template, request
import pandas as pd
from Model import *

app = Flask(__name__)

@app.route("/", methods=['GET'])
def Homepage():
    return render_template("LandingPage.html")

@app.route("/login", methods=['GET'])
def Login():
    nav = 0
    return render_template("Login.html", nav = nav)

@app.route("/cadastro", methods=['GET'])
def Cadastro():
    nav = 0
    return render_template("Cadastro.html", nav = nav)

@app.route("/sobre", methods=['GET'])
def SobreNos():
    nav = 3
    return render_template("SobreNos.html", nav = nav)

######################## MAQUIAGENS ###############################
@app.route("/maqart", methods=['GET'])
def MaqArt():
    nav = 4
    return render_template("MaqArt.html", nav = nav)

@app.route("/maqsocial", methods=['GET'])
def MaqSocial():
    nav = 4
    return render_template("MaqSocial.html", nav = nav)

@app.route("/maqnoiva", methods=['GET'])
def MaqNoiva():
    nav = 4
    return render_template("MaqNoiva.html", nav = nav)

@app.route("/maqprofi", methods=['GET'])
def MaqProfi():
    nav = 4
    return render_template("MaqProfi.html", nav = nav)

##################CABELO######################

@app.route("/cabcorte", methods=['GET'])
def CabCorte():
    nav = 4
    return render_template("CabCorte.html", nav = nav)

@app.route("/cabcor", methods=['GET'])
def CabCor():
    nav = 4
    return render_template("CabCor.html", nav = nav)

@app.route("/cabtrat", methods=['GET'])
def CabTrat():
    nav = 4
    return render_template("CabTratamento.html", nav = nav)
############################UNHAS#################################################

@app.route("/unhagel", methods=['GET'])
def UnhaGel():
    nav = 4
    return render_template("UnhaGel.html", nav = nav)

@app.route("/unhamani", methods=['GET'])
def UnhaMani():
    nav = 4
    return render_template("UnhaMani.html", nav = nav)

@app.route("/unhapedi", methods=['GET'])
def UnhaPedi():
    nav = 4
    return render_template("UnhaPed.html", nav = nav)

@app.route("/unhaacrili", methods=['GET'])
def UnhaAcrilico():
    nav = 4
    return render_template("UnhaAcrilico.html", nav = nav)


###################################################################################

@app.route("/contato", methods=['GET'])
def Contato():
    nav = 2
    foot = 1
    return render_template("Contato.html", nav = nav, foot = foot)

###############################SERVIÇOS############################################

@app.route("/ServMaq", methods=['GET'])
def smaq():
    nav = 4
    return render_template("ServiçoMaquiagem.html", nav = nav)

@app.route("/ServCab", methods=['GET'])
def scab():
    nav = 4
    return render_template("ServiçoCabelo.html", nav = nav)

#######################################################################################

@app.route("/categorias", methods=['GET'])
def Categorias():
    nav = 4
    return render_template("Categorias.html", nav = nav)

@app.route("/faq", methods=['GET'])
def FAQ():
    nav = 1
    return render_template("Faq.html", nav = nav)

@app.route("/post", methods=['POST'])
def Adicionar():
    return

@app.route("/put", methods=['PUT'])
def Atualizar():
    return

@app.route("/deletar", methods=['DELETE'])
def Deletar():
    return

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")