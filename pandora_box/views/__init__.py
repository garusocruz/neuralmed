from flask import request
from flask.views import View


class BaseView(View):
    methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"]

    def __init__(self) -> None:
        self.data = request.get_json(silent=True)
        super().__init__()
