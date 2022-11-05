from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from collections import namedtuple
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from gensim.test.utils import common_texts
from gensim.test.utils import datapath
from gensim import utils
import gzip

#reviews_positive_air = reviews_positive_air = pd.read_csv('/Users/yuyu/macbook_air_reviews_positive.csv')['Translated Text'].fillna('no_value').to_list()


def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield l


class reviewVec:
    def __init__(self, data_set):
        self.data_set = data_set

    def build_model(self):
        list_vector = []
        training_data = parse('/Users/yuyu/Downloads/Electronics.json.gz')
        tagged_data = [TaggedDocument(words=d, tags=[str(i)]) for i, d in enumerate(training_data)]
        model = Doc2Vec(tagged_data, vector_size=100, min_count=1, epochs=30, seed=100, dm=1)
        vectors = []
        for sen in self.data_set:
            v = model.infer_vector(sen)
            vectors.append(v)
        vectors = np.asarray(vectors)

        pca = PCA(n_components=2, random_state=100)
        PCA_result = pca.fit_transform(vectors)
        plt.scatter(PCA_result[:,0], PCA_result[:,1])
        plt.show()





