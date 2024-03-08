from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB

app = Flask(__name__)

db = TinyDB()

@app.route("/pegar_caminho", methods=["GET", "POST"])
def pegar_caminho(caminhoNovo = None):
    if request.method == "GET":
        caminhoNovo = request.form.get("caminhoNovo")
        db.insert({"caminho": caminhoNovo})
    caminhos = db.all()
    return render_template("listaCaminhos.html", caminhoNovo = caminhoNovo, caminhos = caminhos)

@app.route("/novo")
def novo():
    return True


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)