import pandas as pd
import numpy as np

if __name__ == '__main__':
    df = pd.read_json("data/external/palestras.json")

    df.title.replace('Não encontrada',np.NaN, inplace=True)

    df.description.replace('Não encontrada',np.NaN, inplace=True)
    df.description = df.description.apply(lambda value: np.NaN if (len(str(value)) < 5) else value)

    df.dropna(inplace=True)

    df.title = df.title.apply(lambda x: x.strip())
    df.description = df.description.apply(lambda x: x[0].strip())
    df.description = df.description.apply(lambda value: str(value))
    df.drop_duplicates(subset="description", inplace=True)
    
    df.to_json("data/raw/palestras.json")

