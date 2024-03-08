from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

# Instância do Flask
app = Flask(__name__)

# Instância do banco de dados
db = TinyDB("web-app/caminhos.json")

# Rota para salvar o caminho enviado pelo usuário na rota "/novo"
@app.route("/pegar_caminho", methods=["GET", "POST"])
def pegar_caminho(caminhoNovoID=None, caminhoNovoX=None, caminhoNovoY=None, caminhoNovoZ=None, caminhoNovoR=None):
    if request.method == "POST":
        caminhoNovoID = str(request.form.get("caminhoNovoID"))
        caminhoNovoX = request.form.get("caminhoNovoX")
        caminhoNovoY = request.form.get("caminhoNovoY")
        caminhoNovoZ = request.form.get("caminhoNovoZ")
        caminhoNovoR = request.form.get("caminhoNovoR")
        db.insert({"ID": caminhoNovoID, "X": caminhoNovoX, "Y": caminhoNovoY, "Z": caminhoNovoZ, "R": caminhoNovoR})
    caminhos = db.all()
    return listas_caminhos()

# Rota para enviar um novo caminho
@app.route("/novo")
def novo():
    return render_template("novo.html")

# Rota para exibir lista de caminhos
@app.route("/listas_caminhos")
def listas_caminhos():
    render_template("listaCaminhos.html")

# Roda a aplicação web localmente quando este arquivo é executado
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)