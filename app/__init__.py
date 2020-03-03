# app/__init__.py

from flask_restplus import Api
from flask import Blueprint

from .main.controller.nlu_controller import api as nlu_ns
from .main.controller.rasa_template_controller import api as rasa_template_ns
from .main.controller.rasa_template_item_controller import api as rasa_template_item_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )


api.add_namespace(nlu_ns, path='/nlu')
api.add_namespace(rasa_template_ns, path='/rasa_template')
api.add_namespace(rasa_template_item_ns, path='/rasa_template_item')