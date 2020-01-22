import dill
import pandas as pd

from text_similarity_model.pipeline import prediction_pipeline

version = "1.0.0"

class Model(object):
    def __init__(self):
        self.pipeline = prediction_pipeline
        self.version = version

    def _get_all_text_fields(self, documents):
        if isinstance(documents, pd.DataFrame):
            X = documents[["title","description"]].to_dict(orient="records") 
            X = [k["title"]+" "+k["description"] for k in X]
        else:
            X = documents["title"] + " " + documents["description"]
            X = [X]
            
        return X

    def train(self, documents: pd.DataFrame) -> None:
        self.documents = documents
        X_train = self._get_all_text_fields(documents)

        self.pipeline.fit(X_train)

    def predict(self, X: dict, n_results: int) -> list:
        if not isinstance(X, dict):
            raise ValueError("Value to predict needs to be a dict and not {}".format(type(X)))

        X_predict = self._get_all_text_fields(X) 

        similarity_scores = self.pipeline.predict(X_predict)
        similar_documents = similarity_scores.nlargest(n_results)
        
        results = []

        for i,score in similar_documents.iteritems():
            item = self.documents.iloc[i].to_dict()
            item["ano"] = int(item["ano"])
            item["score"] = score
            item["index"] = i
            results.append(item)

        output = {"predictions":results,"version":self.version}

        return output 

    def serialize(self, fname):
        with open(fname, "wb") as f:
            dill.dump(self.pipeline, f)
            dill.dump(self.documents, f)

    @staticmethod
    def deserialize(fname):
        model = Model()
        with open(fname, "rb") as f:
            model.pipeline = dill.load(f)
            model.documents = dill.load(f)

            return model
