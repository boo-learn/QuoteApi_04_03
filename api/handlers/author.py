from api import app, db, request
from api.models.quote import QuoteModel
from api.models.author import AuthorModel
from api.schemas.author import author_schema, authors_schema


# Сериализация:
#      MA       FLASK
# obj ---> dict ----> json
@app.route('/authors', methods=["GET"])
def get_authors():
    authors = AuthorModel.query.all()
    return authors_schema.dump(authors)


@app.route('/authors/<int:author_id>', methods=["GET"])
def get_author_by_id(author_id):
    author = AuthorModel.query.get(author_id)
    if not author:
        return f"Author id={author_id} not found", 404

    return author_schema.dump(author)


@app.route('/authors', methods=["POST"])
def create_author():
    author_data = request.json
    author = AuthorModel(author_data["name"])
    db.session.add(author)
    db.session.commit()
    return author_schema.dump(author), 201


@app.route('/authors/<int:author_id>', methods=["PUT"])
def edit_author(author_id):
    author_data = request.json
    author = AuthorModel.query.get(author_id)
    if author is None:
        return {"Error": f"Author id={author_id} not found"}, 404
    author.name = author_data["name"]
    db.session.commit()
    return author_schema.dump(author)


@app.route('/authors/<int:author_id>', methods=["PUT"])
def delete_author(quote_id):
    raise NotImplemented("Метод не реализован")
