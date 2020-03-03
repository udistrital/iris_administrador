from flask import request
from flask_restplus import Resource

from app.main.service.rasa_template_item_service import get_all_rasa_template_item, save_new_rasa_template_item, get_a_rasa_templatee_item
from ..util.dto import RasaTemplateItemDto


api = RasaTemplateItemDto.api
_rasa_template_item = RasaTemplateItemDto.rasa_template_item


@api.route('/')
class RasaTemplateItemList(Resource):
    @api.doc('list_of_registered_rasa_template_item')
    @api.marshal_list_with(_rasa_template_item, envelope='data')
    def get(self):
        """List all registered rasa template items"""
        return get_all_rasa_template_item()

    @api.response(201, 'Rasa Template Item successfully created.')
    @api.doc('create a new rasa template Item')
    @api.expect(_rasa_template_item, validate=True)
    def post(self):
        """Creates a new rasa template Item """
        data = request.json
        return save_new_rasa_template_item(data=data)


@api.route('/<item_type>')
@api.param('item_type', 'The Rasa Template type')
@api.response(404, 'Rasa Template Item not found.')
class RasaTemplateItem(Resource):
    @api.doc('get a RasaTemplateItem')
    @api.marshal_with(_rasa_template_item)
    def get(self, item_type):
        rasa_template_item = get_a_rasa_templatee_item(item_type)
        if not rasa_template_item:
            api.abort(404)
        else:
            return rasa_template_item
