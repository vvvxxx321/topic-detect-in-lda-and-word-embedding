from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from nltk.corpus import wordnet
from nltk.probability import FreqDist
import pyLDAvis.sklearn
import gensim
from gensim import corpora
import pprint

class lda_model:
    def __init__(self, data_set):
        self.data_set = data_set

    def build_model(self):
        cv = CountVectorizer()
        dictionary = corpora.Dictionary(self.data_set)
        doc_term_matrix = [dictionary.doc2bow(rev) for rev in self.data_set]
        LDA = gensim.models.ldamodel.LdaModel

        model = LDA(corpus=doc_term_matrix, id2word=dictionary, num_topics=10, random_state=100, chunksize=1000, passes=50)
        print(model.print_topics())




