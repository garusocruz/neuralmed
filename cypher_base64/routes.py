from flask.blueprints import Blueprint
from .views.api_neuralmed import ApiNeuralmedView


api_neuralmed_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

api_neuralmed_view_v1 = ApiNeuralmedView.as_view("api_neuralmed_v1")

api_neuralmed_v1.add_url_rule("/", view_func=api_neuralmed_view_v1)
