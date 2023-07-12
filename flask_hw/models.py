from app import db
from sqlalchemy import func


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    author = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Integer, nullable=False)


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey(Users.id), primary_key=True)
    book_id = db.Column(db.ForeignKey(Books.id), primary_key=True)
    # date = db.Column(db.Text, default=func.now())
