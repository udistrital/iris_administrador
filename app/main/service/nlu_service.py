import json
from app.main import db
from app.main.model.nlu import Nlu


def save_new_nlu(data):

    new_nlu = Nlu(
        type=data['type'],
        name=data['name'],
        value=json.dumps(data['value'])
        .replace("[", "{")
        .replace("]", "}")
    )
    save_changes(new_nlu)
    response_object = {
        'status': 'success',
        'message': 'NLU Successfully registered.'
    }
    return response_object, 201


def get_all_nlu():
    return Nlu.query.all()


def get_a_nlu(name):
    return Nlu.query.filter_by(name=name).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
