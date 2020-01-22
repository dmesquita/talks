from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

from text_similarity_model.transformers import TextTransformer, CosineSimilaritiesEstimator

data_process_pipeline = Pipeline(
    [
        ("tokens", TextTransformer("pt_core_news_sm")),
        ("tfidf", TfidfVectorizer(tokenizer=lambda x:x, lowercase=False))
    ]
)

prediction_pipeline = Pipeline(
    [
        ("data_process", data_process_pipeline),
        ("estimator", CosineSimilaritiesEstimator())
    ]
) 
