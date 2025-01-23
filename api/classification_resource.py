import pickle

from flask import request, Response
from flask_restful import Resource
from functools import lru_cache
from sklearn.feature_extraction.text import TfidfVectorizer

from models.classifier import SavedModel


MODEL_PATH = "models/trained/news_classifier_am.pkl"
VECTORIZER_PATH = "models/trained/tfidfvectorizer.pkl" 

@lru_cache(maxsize=2)
def load_pickle(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)

class ClassificationResource(Resource):
    def __init__(self):
        self.model: SavedModel = load_pickle(MODEL_PATH)
        self.vectorizer: TfidfVectorizer = load_pickle(VECTORIZER_PATH)

    def post(self):
        req = request.json
        if "text" not in req:
            return Response(status=400)
        
        text = req["text"]
        class_ = self.model.predict(text, self.vectorizer)
        return { "class": class_ }
