from flask import Response
from flask_restful import Resource

class HealthResource(Resource):
    def get(self):
        return Response(status=200)
