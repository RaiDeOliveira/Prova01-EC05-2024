from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB()

@app.route("/pegar_caminho", methods=["GET", "POST"])
def pegar_caminho(caminhoNovoID, caminhoNovoX, caminhoNovoY, caminhoNovoZ, caminhoNovoR):
    if request.method == "POST":
        caminhoNovoID = str(request.form.get("caminhoNovoID"))
        caminhoNovoX = request.form.get("caminhoNovoX")
        caminhoNovoY = request.form.get("caminhoNovoY")
        caminhoNovoZ = request.form.get("caminhoNovoZ")
        caminhoNovoR = request.form.get("caminhoNovoR")
        db.insert({caminhoNovoID: {caminhoNovoX, caminhoNovoY, caminhoNovoZ, caminhoNovoR}})
    caminhos = db.all()
    return listas_caminhos(ID=caminhoNovoID, caminhos=caminhos)

@app.route("/novo")
def novo():
    return render_template("novo.html")

@app.route("/listas_caminhos")
def listas_caminhos(ID, caminhos):
    render_template("listaCaminhos.html", ID, caminhos)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)