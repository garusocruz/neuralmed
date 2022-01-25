import base64
import codecs
import json
import os


from flask import make_response, render_template, request
from flask.views import MethodView

from pandora_box.services.pandora_box_service import PandoraBoxService
from PIL import Image


class ApiNeuralmedView(MethodView):
    service = PandoraBoxService

    def get(self):
        service = self.service()
        
        return make_response(
            render_template("dirtree.html", tree=service.make_tree("images")), 200
        )

    def post(self):
        raw_event = request.get_json()

        service = self.service(raw_event=raw_event)
        service.save_original_file()
        service.save_resized_file()
        return make_response("", 200)
