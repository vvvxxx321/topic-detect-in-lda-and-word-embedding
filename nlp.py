import csv
import nltk
import numpy as np
# nltk.download('punkt')
from nltk import word_tokenize
from nltk import sent_tokenize
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#nltk.download('wordnet')
#nltk.download('omw-1.4')
import googletrans
from googletrans import Translator


# Word tokenizing
def tokenize(review_list):
    words_list = []
    for review in review_list:
        words = word_tokenize(review)
        words_list.append(words)

    words_list = np.asarray(words_list, dtype=object)

    return words_list


def process_words(words_list):
    lemmatizer = WordNetLemmatizer()

    words_no_punc_list = []

    for words in words_list:
        words_no_punc = []
        for word in words:
            word = lemmatizer.lemmatize(word)
            if word.isalpha():
                words_no_punc.append(word.lower())
        words_no_punc_list.append(words_no_punc)

    words_no_punc_list = np.asarray(words_no_punc_list, dtype=object)

    stopws = stopwords.words("english")
    new_stopws = ['macbook', 'mac', 'air', 'pro', 'wa', 'ha', "mbp", "one", "excelente", "thanks", "love", "recommend", "use", \
                  'much', 'still', 'like', 'computer', 'laptop', 'lot', 'thing', 'even', 'make', 'new', 'came', 'everything', 'old', \
                  'wow', 'need', 'perfect', 'good', 'best', 'great', 'ever', 'know', 'could', 'also', 'would', 'apple', 'get']
    stopws.extend(new_stopws)

    clean_words_list = []

    for words in words_no_punc_list:
        clean_words = []
        for word in words:
            if word not in stopws:
                clean_words.append(word)
        clean_words_list.append(clean_words)

    clean_words_list = np.asarray(clean_words_list, dtype=object)

    return clean_words_list


def translate_to_en(review):
    translator = Translator()
    translator.raise_Exception = True
    review_en = translator.translate(review)

    return review_en




