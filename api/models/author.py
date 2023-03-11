from api import db


class AuthorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    surname = db.Column(db.String(32), nullable=False, server_default="Иванов")
    quotes = db.relationship('QuoteModel', backref='author', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()

    # def __init__(self, name):
    #     self.name = name


    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name
    #     }
