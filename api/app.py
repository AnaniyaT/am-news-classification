
import flask_restful

from flask import Flask
from flask_cors import CORS

from api.classification_resource import ClassificationResource
from api.health_resource import HealthResource
from models.classifier import SavedModel


def create_app():
    app = Flask(__name__)
    
    api = flask_restful.Api(app)
    api.add_resource(
        HealthResource,
        "/health"
    )
    api.add_resource(
        ClassificationResource,
        "/classify"
    )
    
    cors = CORS(resources={r'/*': {'origins': '*'}})
    cors.init_app(app)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
