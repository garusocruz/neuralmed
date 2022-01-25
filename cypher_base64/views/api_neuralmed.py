import codecs
import uuid

from flask import make_response, request
from flask.views import MethodView

from cypher_base64.services.cypher_service import CypherService


class ApiNeuralmedView(MethodView):
    service = CypherService()

    def get(self):
        f = codecs.open("cypher_base64/templates/index.html", "r", "utf-8")
        document = f.read()
        return make_response(document, 200)

    def post(self):
        if not (request.files and request.files.get("file", None)) and not (
            request.get_json() and request.get_json().get("file_base64", None)
        ):
            f = codecs.open("cypher_base64/templates/error.html", "r", "utf-8")
            document = f.read()
            error_message = "Por favor voce precisa enviar na request algum destes campos, 'file' para os inputs de formulário ou 'file_base64' caso envie um json via body da requisição"
            document = document.replace("{error_message}", error_message)
            return make_response(document, 400)

        data = request.get_json()

        if data:
            file_base64 = data["file_base64"]
            extension_file = data.get("extension_file", None)

            if not extension_file:
                error_message = "Você precisa informar a extensão do arquivo, com o campo 'extension_file'"
                return make_response(error_message, 400)

            response = ""

        else:
            file = request.files["file"]
            extension_file = self.service.get_file_format(file=file)

            file_base64 = (self.service.encode_base64(file=file)).decode()

            f = codecs.open("cypher_base64/templates/success.html", "r", "utf-8")
            document = f.read()
            response = document.replace("{url}", "teste")

        self.service.publish_message(
            message={
                "file_name": f"{uuid.uuid4().hex}.{extension_file}",
                "file_base64": file_base64,
            }
        )

        return make_response(response, 200)
