from preprocessing.tools import normalize, remove_punctuation, remove_stopwords


class PreprocessingPipeline:
    def preprocess(self, text: str) -> str:
        text = remove_punctuation(text)
        text = normalize(text)
        return " ".join(remove_stopwords(text))

    def __call__(self, text: str):
        return self.preprocess(text)
