from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações de acesso ao banco de dados
user = 'uutnfujn'
password = 'TJ-budc9lkNSwDgt29vxcSjalpXx2bj7'
host = 'tuffi.db.elephantsql.com'
database = 'uutnfujn'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "chave escondidamente"

# Instanciando objeto da classe SQLAlchemy
db = SQLAlchemy(app)

# Modelar a Classe Filmes -> tabela filmes
class Filmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    imagem_url = db.Column(db.String(255), nullable=False)
    curiosidade = db.Column(db.String(10000), nullable=False)
    
    def __init__(self, nome, imagem_url):
        self.nome = nome
        self.imagem_url = imagem_url
    
    @staticmethod
    
    def read_all():
        # SELECT * FROM filmes ORDER BY id ASC
        return Filmes.query.order_by(Filmes.id.asc()).all()
    db = SQLAlchemy(app)    

    @staticmethod
    def read_single(registro_id):
        #SELECT *FROM filmes WHERE id=x, onde x é o valor do id na coluna id da tabela filmes
        return Filmes.query.get(registro_id) #vai procurar dentro da chave primaria
    db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/read")
def read_all():
    # Chamada do método read_all da classe Filmes, que representa a tabela filmes do banco de dados.
    registros = Filmes.read_all()
    return render_template("read_all.html", registros=registros)


@app.route("/read/<id_registro>")
def read_id(id_registro):
    #chmada do metodo read_single da classe filmes
    registro = Filmes.read_single(id_registro)
    return render_template("read_single.html",registro = registro)


@app.route("/create")
def create():
    return "Em construção,sem avexamento!"


if (__name__ == "__main__"):
    app.run(debug=True)