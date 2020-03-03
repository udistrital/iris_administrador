from flask import request
from flask_restplus import Resource

from app.main.service.rasa_template_service import get_all_rasa_template, save_new_rasa_template, get_a_rasa_template
from ..util.dto import RasaTemplateDto


api = RasaTemplateDto.api
_rasa_template = RasaTemplateDto.rasa_template


@api.route('/')
class RasaTemplateList(Resource):
    @api.doc('list_of_registered_rasa_template')
    @api.marshal_list_with(_rasa_template, envelope='data')
    def get(self):
        """List all registered rasa templates"""
        return get_all_rasa_template()

    @api.response(201, 'Rasa Template successfully created.')
    @api.doc('create a new rasa template')
    @api.expect(_rasa_template, validate=True)
    def post(self):
        """Creates a new rasa template """
        data = request.json
        return save_new_rasa_template(data=data)


@api.route('/<tem_name>')
@api.param('tem_name', 'The Rasa Template name')
@api.response(404, 'Rasa Template not found.')
class RasaTemplate(Resource):
    @api.doc('get a RasaTemplate')
    @api.marshal_with(_rasa_template)
    def get(self, tem_name):
        rasa_template = get_a_rasa_template(tem_name)
        if not rasa_template:
            api.abort(404)
        else:
            return rasa_template
