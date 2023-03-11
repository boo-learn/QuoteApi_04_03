from flask import abort
from api import app


@app.errorhandler(404)
def handle_404(error):
    response = {'status': 404, 'error': error.description}
    return response, 404


def get_object_or_404(model, object_id):
    object = model.query.get(object_id)
    if not object:
        abort(404, description=f"Author id={object_id} not found")
    return object
