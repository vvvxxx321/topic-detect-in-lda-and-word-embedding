import gensim
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import numpy as np
from gensim.test.utils import common_texts

class ldaVec:
    def __init__(self, data_set):
        self.data_set = data_set


    def build_model(self):
        vector_list = []
        model = Word2Vec(common_texts, min_count=1, vector_size=100, sg=0, seed=100)
        for word in self.data_set:
            vw = model.wv[word]
            vector_list.append(vw)
        vector_list = np.asarray(vector_list)


        pca = PCA(n_components=2, random_state=100)
        PCA_result = pca.fit_transform(vector_list)
        plt.scatter(PCA_result[:, 0], PCA_result[:, 1])
        plt.show()



