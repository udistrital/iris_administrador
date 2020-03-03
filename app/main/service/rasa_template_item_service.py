from app.main import db
from app.main.model.rasa_template_item import RasaTemplateItem


def save_new_rasa_template_item(data):

    new_rasa_template_item = RasaTemplateItem(
        item_type=data['item_type'],
        item_value=data['item_value'],
        tem_id=data['tem_id'],
    )
    save_changes(new_rasa_template_item)
    response_object = {
        'status': 'success',
        'message': 'Rsa Template Item Successfully registered.'
    }
    return response_object, 201


def get_all_rasa_template_item():
    return RasaTemplateItem.query.all()


def get_a_rasa_templatee_item(item_type):
    return RasaTemplateItem.query.filter_by(item_type=item_type).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
