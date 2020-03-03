from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })


class NluDto:
    api = Namespace('nlu', description='nlu related operations')
    nlu = api.model('nlu', {
        'id': fields.String(description='nlu id'),
        'type': fields.String(required=True, description='nlu type'),
        'name': fields.String(required=True, description='nlu name'),
        'value': fields.List(fields.String(), description='nlu value')
    })


class RasaTemplateDto:
    api = Namespace('rasa_template', description='rasa_template related operations')
    rasa_template = api.model('rasa_template', {
        'id': fields.String(description='rasa_template id'),
        'tem_name': fields.String(required=True, description='rasa_template name')
    })


class RasaTemplateItemDto:
    api = Namespace('rasa_template_item', description='rasa_template_item related operations')
    rasa_template_item = api.model('rasa_template_item', {
        'id': fields.String(description='rasa_template_item id'),
        'item_type': fields.String(required=True, description='rasa_template_item name'),
        'item_value': fields.String(required=True, description='rasa_template_item name'),
        'tem_id': fields.String(required=True, description='rasa_template_item name')
    })


