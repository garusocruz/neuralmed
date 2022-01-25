from flask import Flask, redirect
from .routes import api_neuralmed_v1

app = Flask(__name__)

app.register_blueprint(api_neuralmed_v1)
app.config["SECRET_KEY"] = "8b892208-7d1a-46e9-92e2-b9e7432d2fea"


@app.errorhandler(404)
def own_404_page(error):
    return redirect("/api/v1")
