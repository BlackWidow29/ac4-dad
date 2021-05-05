from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ac4.db"
db = SQLAlchemy(app)

class User(db.Model):
    # nome da tabela
    __tablename__ = "user"
    # campos da tabela
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    # post_user = db.relationship('Post', backref ='User', lazy=True)
    # construtor da classe User
    def __init__(self, user, password, name, email):
        self.user = user
        self.password = password
        self.name = name
        self.email = email

class Follow(db.Model):
    # nome da tabela
    tablename="follow"
    # campos da tabela
    id =db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer(100), db.ForeignKey('follow_user.id'), nullable=False)
    id_follower = db.Column(db.Integer(100), db.ForeignKey('follow_user.id'), nullable=False)

    follow_user = db.relationship("User")

    # construtor da classe Follow
    def __init__(self, id_user, id_folllower):
        self.id_user = id_user
        self.id_folllower = id_folllower

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
    def __init__(self, content, id_user):
        self.content = content
        self.id_user = id_user

@app.route("/")
def index():
    # select * from
    usuarios = User.query.all()
    return render_template("index.html", usuarios=usuarios)


if __name__ == "__main__":
    # crio a tabela
    db.create_all()
    app.run(debug=True)