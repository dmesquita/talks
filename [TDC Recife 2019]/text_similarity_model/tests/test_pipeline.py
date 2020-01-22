import unittest

from text_similarity_model.pipeline import data_process_pipeline, prediction_pipeline

class PipelineTest(unittest.TestCase):
    def setUp(self):
        self.pipe = prediction_pipeline
        corpus = ["poxa que frase legal", "oba estou"]
        self.pipe.fit(corpus)

    def test_data_process_pipeline(self):
        pipe2 = data_process_pipeline
        corpus = ["poxa que frase legal", "oba estou"]
        pipe2.fit(corpus)
        features = ['frase', 'legal', 'oba', 'poxa']
        self.assertEqual(features, pipe2[-1].get_feature_names())

    def test_prediction_pipeline(self):
        self.assertEqual(2, len(self.pipe.predict(["oba recife"])))
        self.assertAlmostEqual(0.0, self.pipe.predict(["oba recife"])[0])
