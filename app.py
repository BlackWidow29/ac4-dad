from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ac4.db"
db = SQLAlchemy(app)

class Follow(db.Model):
    __tablename__ = "follow"

        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
        user = db.relationship('user',lazy='subquery',
        backref=db.backref('follow', lazy=True))

# esta classe irá criar a minha tabela
class Post(db.Model):
    # nome da tabela
    __tablename__ = "post"
    # campos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(100), unique=True)
    id_user = db.Column(db.Integer, db.ForeignKey('post_user.id'), nullable=False)

    post_user = db.relationship("User")

    # construtor da classe Post
    def __init__(self, user, password, name, email):
        self.user = user
        self.password = password
        self.name = name
        self.email = email

@app.route("/")
def index():
    # select * from
    usuarios = User.query.all()
    return render_template("index.html", usuarios=usuarios)


if __name__ == "__main__":
    # crio a tabela
    db.create_all()
    app.run(debug=True)