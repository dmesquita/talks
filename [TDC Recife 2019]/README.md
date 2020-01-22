## Computando similaridades entre palestras do TDC

### Obtendo os dados

```
$ make data
```

### Limpando os dados

```
$ make process_data

```

### Instalando o package do model

```
$ pip3 install -e /text_similarity_model

```

### Treinando o modelo 

```
$ text_similarity_model train <json-dir> <model-name> 

```

### Rodando a API 

```
$ python3 api/api.py 

```
