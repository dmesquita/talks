import unittest
import pandas as pd

from text_similarity_model.model import Model

class ModelTest(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(
            [ 
           { 
              "ano":2017,
              "cidade":"florianopolis",
              "description":"Um painel de discussão com alguns desenvolvedores Xamarin sobre como é o desenvolvimento de apps em Xamarin em diferentes locais do planeta.",
              "index":100,
              "title":"Painel: Debate sobre o desenvolvimento de Apps em Xamarin para clientes ao redor do mundo",
              "trilha":"trilha-xamarin",
              "trilha_url":"http://www.thedevelopersconference.com.br/tdc/2017/florianopolis/trilha-xamarin"
           },
           { 
              "ano":2017,
              "cidade":"portoalegre",
              "description":"Que conceito é esse analisado pela Forbes, pelo Gartrner, pela Harvard Business Review e pela MIT Sloan School of Management e como ele afeta a carreira de todos que trabalham com Data & Analytics, principalmente em DataScience.",
              "index":10000,
              "title":"Data Driven Organizations: como este conceito afeta a carreira de DataScience",
              "trilha":"trilha-data-science",
              "trilha_url":"http://www.thedevelopersconference.com.br/tdc/2017/portoalegre/trilha-data-science"
           },
           { 
              "ano":2017,
              "cidade":"portoalegre",
              "description":"Você tem escutado falar de Microserviços ao longo dos meses e provavelmente já olhou sobre 12-factor e também e aplicações cloud-native. Mas existem milhares de frameworks Java e ferramentas que você pode utilizar para confeccionar o seu software e juntar as partes em uma arquitetura orientada a Microserviços. É claro que você quer usar a melhor de cada uma delas.",
              "index":10113,
              "title":"Desenvolva Aplicações usando arquiteturas orientada a microserviços",
              "trilha":"trilha-microservices",
              "trilha_url":"http://www.thedevelopersconference.com.br/tdc/2017/portoalegre/trilha-microservices"
           }
        ]
        ) 

    def test_model(self):
        model = Model()
        model.train(self.df)
        self.assertEqual(2, len(model.predict({"title":"",
                                                "description":"Desenvolva"}, 2)))

    def test_deserialize(self):
        model = Model()
        model.train(self.df)
        model.serialize("../models/test_model.pkl")
        model_loaded = Model.deserialize("../models/test_model.pkl")
        self.assertEqual(2, len(model.predict({"title":"",
                                                "description":"Desenvolva"}, 2)))
