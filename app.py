import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "chave-da-atividade"

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "jogos.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# MODEL já implementado: observe como as colunas representam os campos da tabela.
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    genre = db.Column(db.String(80), nullable=False)
    platforms = db.Column(db.String(180), nullable=False)
    release_year = db.Column(db.Integer, nullable=False)
    poster = db.Column(db.String(80), nullable=False)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # ATIVIDADE 1 — CADASTRAR
        # a) Recupere title, genre, platforms, release_year e poster com request.form.
        # b) Converta release_year para inteiro.
        # c) Crie um objeto Game com os valores recebidos.
        # d) Adicione o objeto à sessão e confirme a transação.
        # e) Redirecione para a página inicial.
        pass

    # Esta parte já está pronta: consulta e lista os jogos.
    games = Game.query.order_by(Game.title).all()
    return render_template("home.html", games=games)


@app.route("/editar/<int:game_id>", methods=["GET", "POST"])
def edit(game_id):
    # ATIVIDADE 2 — LOCALIZAR E EDITAR
    # a) Localize o jogo usando o game_id recebido pela URL.
    #    Dica: Game.query.get_or_404(game_id)
    # b) Se o método for POST, atualize os atributos do objeto com request.form.
    # c) Salve as alterações com db.session.commit().
    # d) Redirecione para a página inicial depois de salvar.
    # e) Se for GET, renderize editar.html enviando o objeto game.
    pass


@app.route("/excluir/<int:game_id>", methods=["POST"])
def delete(game_id):
    # ATIVIDADE 3 — EXCLUIR
    # a) Localize o jogo pelo ID.
    # b) Remova o objeto da sessão.
    # c) Confirme a exclusão no banco.
    # d) Redirecione para a página inicial.
    pass


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
