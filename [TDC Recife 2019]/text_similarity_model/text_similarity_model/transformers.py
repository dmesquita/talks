import pandas as pd
import spacy

from sklearn.base import BaseEstimator, TransformerMixin, ClusterMixin
from sklearn.metrics.pairwise import cosine_similarity

class TextTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, nlp_model="en", lemmatization=True, remove_stopwords=True) -> None:
        self.model_ = spacy.load(nlp_model)
        self.nlp_model = nlp_model
        self.lemmatization = lemmatization
        self.remove_stopwords = remove_stopwords

    def fit(self, X: list, y=None) -> 'TextTransformer':
        return self

    def transform(self, X: list) -> list:
        X_ = []
        X_docs = list(self.model_.pipe(X, disable=["parser","ner"]))  
        for doc in X_docs:
            tokens = []
            if self.lemmatization:
                if self.remove_stopwords:
                    tokens = [t.lemma_ for t in doc if not t.is_stop]
                else:
                    tokens = [t.lemma_ for t in doc]
            else:
                if self.remove_stopwords:
                    tokens = [t.lower_ for t in doc if not t.is_stop]
                else:
                    tokens = [t.lower_ for t in doc]
                
            X_.append(tokens)

        return X_

class CosineSimilaritiesEstimator(BaseEstimator, ClusterMixin):
    """Get cosine similarities"""
    def fit(self, X, y=None) -> None:
        self.X_corpus = X
        return self

    def predict(self, X: 'sparse matrix') -> pd.Series:
        cosine_similarities = pd.Series(cosine_similarity(
                                                        self.X_corpus, X
                                                        ).flatten())
        return cosine_similarities 
