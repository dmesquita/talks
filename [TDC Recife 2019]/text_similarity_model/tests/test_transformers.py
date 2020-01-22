import unittest
import spacy

from text_similarity_model.transformers import TextTransformer, CosineSimilaritiesEstimator
from sklearn.feature_extraction.text import TfidfVectorizer

class TransformersTest(unittest.TestCase):
    def test_lemmatization_defaults(self):
        lt = TextTransformer("pt_core_news_sm")
        self.assertListEqual([["jogar"]], lt.transform(["eu jogo"]))
        self.assertListEqual([["jogar"]], lt.transform(["eu quero jogar"]))
        self.assertListEqual([["gostar","jogar"]], lt.transform(["eu gosto de jogar"]))

    def test_lemmatization_false(self):
        lt = TextTransformer("pt_core_news_sm", lemmatization=False, remove_stopwords=False)
        self.assertListEqual([["eu","jogo"]], lt.transform(["eu jogo"]))

    def test_stopwords_false(self):
        lt = TextTransformer("pt_core_news_sm", remove_stopwords=False)
        self.assertListEqual([["eu","jogar"]], lt.transform(["eu jogo"]))

    def test_cosine_similarities(self):
        lt = TextTransformer("pt_core_news_sm")
        vec = lt.transform(["eu quero jogo"])
        vect = TfidfVectorizer(tokenizer= lambda x: x,lowercase=False)
        tfidf = vect.fit_transform(vec)

        cs = CosineSimilaritiesEstimator() 
        cs.fit(tfidf) 

        self.assertAlmostEqual(1.00,cs.predict(
                                vect.transform(lt.transform(["quero jogar"])))[0]
                                , places=3)

        self.assertAlmostEqual(0.0,cs.predict(
                                vect.transform(lt.transform(["tá errado"])))[0]
                                , places=3)
