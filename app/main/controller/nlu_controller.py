from flask import request
from flask_restplus import Resource

from app.main.service.nlu_service import get_all_nlu, save_new_nlu, get_a_nlu
from ..util.dto import NluDto


api = NluDto.api
_nlu = NluDto.nlu


@api.route('/')
class NluList(Resource):
    @api.doc('list_of_registered_nlu')
    @api.marshal_list_with(_nlu, envelope='data')
    def get(self):
        """List all registered nlu"""
        return get_all_nlu()

    @api.response(201, 'Nlu successfully created.')
    @api.doc('create a new nlu')
    @api.expect(_nlu, validate=True)
    def post(self):
        """Creates a new _nlu """
        data = request.json
        return save_new_nlu(data=data)


@api.route('/<name>')
@api.param('name', 'The NLU name')
@api.response(404, 'NLU not found.')
class Nlu(Resource):
    @api.doc('get a nlu')
    @api.marshal_with(_nlu)
    def get(self, name):
        nlu = get_a_nlu(name)
        if not nlu:
            api.abort(404)
        else:
            return nlu
