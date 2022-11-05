import time

import nltk
import csv
import pandas as pd
import numpy as np

import ldaToVec
import nlp
from sklearn.decomposition import LatentDirichletAllocation as LDA
import lda_p
import datetime
import googletrans
from googletrans import Translator

import reviewToVec
import matplotlib
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

def get_pure_date(list_date):
    list_pure_date = []

    month_english_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September",\
                          "October", "November", "December"]

    for d in list_date:
        date_english = d.split("on ", 1)[1]
        month = date_english.split()[0]
        year = int(date_english.split()[2])
        da = int(date_english.split()[1].split(",")[0])
        month = month_english_list.index(month) + 1
        date_time = datetime.datetime(year, month, da)
        list_pure_date.append(date_time)

    return list_pure_date


def divide_by_date(review_list, date_list, date):
    review_list_past = []
    review_list_later = []
    date_list_past = []
    date_list_later = []

    for index in range(0, len(date_list)):
        d = date_list[index]
        if d < date:
            date_list_past.append(d)
            review_list_past.append(review_list[index])
        elif d >= date:
            date_list_later.append(d)
            review_list_later.append(review_list[index])

    return review_list_past, review_list_later, date_list_past, date_list_later

heading = pd.read_csv('/Users/yuyu/macbook_air_reviews_positive.csv', index_col=0, nrows=0).columns.tolist()
print(heading)

# Get the reviews
reviews_positive_air = pd.read_csv('/Users/yuyu/macbook_air_reviews_positive.csv')['Translated Text'].fillna('no_value').to_list()
reviews_negative_air = pd.read_csv('/Users/yuyu/macbook_air_reviews_negative.csv')['Translated Text'].fillna('no_value').to_list()
reviews_positive_pro = pd.read_csv('/Users/yuyu/macbook_pro_reviews_positive.csv')['Review'].fillna('no_value').to_list()
reviews_negative_pro = pd.read_csv('/Users/yuyu/macbook_pro_reviews_negative.csv')['Review'].fillna('no_value').to_list()
# reviews_air = pd.read_csv('/Users/yuyu/macbook_air_reviews.csv')['Review']
# reviews_pro = pd.read_csv('/Users/yuyu/macbook_pro_reviews.csv')['Review']

'''
n = 1
for review in reviews_positive_air:
    translator = Translator()
    print(translator.detect(review))
    review = nlp.translate_to_en(review)
    print(n)
    print(review)
    n = n + 1
'''


date_positive_air = pd.read_csv('/Users/yuyu/macbook_air_reviews_positive.csv')['Date'].to_list()
date_positive_air = get_pure_date(date_positive_air)
d1 = datetime.datetime(2021, 8, 10)
air_positive_review_past, air_positive_review_later, air_positive_date_past, air_positive_date_later = \
    divide_by_date(reviews_positive_air, date_positive_air, d1)
print(len(air_positive_review_past))
print(len(air_positive_review_later))

date_negative_air = pd.read_csv('/Users/yuyu/macbook_air_reviews_negative.csv')['Date'].to_list()
date_negative_air = get_pure_date(date_negative_air)
air_negative_review_past, air_negative_review_later, air_negative_date_past, air_negative_date_later = \
    divide_by_date(reviews_negative_air, date_negative_air, d1)
print(len(air_negative_review_past))
print(len(air_negative_review_later))




#print(reviews_positive_air)
#for review in reviews_negative_air:
 #  print(review)


# Get the words tokenizing list from reviews
#positive_air_words_list = nlp.tokenize(reviews_positive_air)
#negative_air_words_list = nlp.tokenize(reviews_negative_air)
#positive_pro_words_list = nlp.tokenize(reviews_positive_pro)
#negative_pro_words_list = nlp.tokenize(reviews_negative_pro)
# air_list = nlp.tokenize(reviews_air)
# pro_list = nlp.tokenize(reviews_pro)
positive_air_words_list_past = nlp.tokenize(air_positive_review_past)
positive_air_words_list_later = nlp.tokenize(air_positive_review_later)
negative_air_words_list_past = nlp.tokenize(air_negative_review_past)
negative_air_words_list_later = nlp.tokenize(air_negative_review_later)


# Get the clean words list
#air_positive_clean = nlp.process_words(positive_air_words_list)
#air_negative_clean = nlp.process_words(negative_air_words_list)
#pro_positive_clean = nlp.process_words(positive_pro_words_list)
#pro_negative_clean = nlp.process_words(negative_pro_words_list)
# air_clean = nlp.remove_stop_words(air_no_punc)
# pro_clean = nlp.remove_stop_words(pro_no_punc)
air_positive_clean_past = nlp.process_words(positive_air_words_list_past)
air_positive_clean_later = nlp.process_words(positive_air_words_list_later)
air_negative_clean_past = nlp.process_words(negative_air_words_list_past)
air_negative_clean_later = nlp.process_words(negative_air_words_list_later)

#print(air_positive_clean_past)


#lda_p.build_model(air_clean)
#lda_p.build_model(pro_clean)
#lda_p.build_model(air_positive_clean)
#lda_p.build_model(air_negative_clean)
#lda_p.build_model(pro_positive_clean)
#lda_p.build_model(pro_negative_clean)

lm_past = lda_p.lda_model(air_positive_clean_past)
lm_past.build_model()
#lmn_past = lda_p.lda_model(air_negative_clean_past)
#lmn_past.build_model()

#rl_later = reviewToVec.reviewVec(air_positive_clean_later)
#rl_later.build_model()
#rln_later = reviewToVec.reviewVec(air_negative_clean_later)
#rln_later.build_model()

#lda_vec_list = ['battery', 'fast', 'life', 'quality', 'camera', 'product', 'amazing', 'work', 'super', 'light']
#lda_vec = ldaToVec.ldaVec(lda_vec_list)
#lda_vec.build_model()



# for r in air_positive_review_later:
#   print(r)





