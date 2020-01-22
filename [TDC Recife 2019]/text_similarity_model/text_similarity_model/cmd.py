"""Talks similarity model

Usage:
    text_similarity_model train <json-dir> <model-name>
    text_similarity_model (-h | --help)

Arguments:
    <json-dir>          File with talks data.
    <model-name>        Serialized model name.

Options:
    -h --help           Show this screen.

"""

import os

import pandas as pd
from docopt import docopt

from text_similarity_model.model import Model

def train_model(json_dir, model_name):
    print("Training model with data from {}".format(json_dir))
    
    df = pd.read_json(json_dir) 
    model = Model()
    model.train(df)

    model.serialize("models/"+model_name)

def main():
    arguments = docopt(__doc__)

    if arguments['train']:
        train_model(arguments['<json-dir>'],
                    arguments['<model-name>']
        )

if __name__ == '__main__':
    main()
