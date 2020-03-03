from app.main import db
from app.main.model.rasa_template import RasaTemplate


def save_new_rasa_template(data):

    new_rasa_template = RasaTemplate(
        tem_name=data['tem_name']
    )
    save_changes(new_rasa_template)
    response_object = {
        'status': 'success',
        'message': 'Rsa Template Successfully registered.'
    }
    return response_object, 201


def get_all_rasa_template():
    return RasaTemplate.query.all()


def get_a_rasa_template(tem_name):
    return RasaTemplate.query.filter_by(tem_name=tem_name).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
