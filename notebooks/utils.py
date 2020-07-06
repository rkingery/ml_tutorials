import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from collections import Counter, defaultdict

# Text Processing Packages
import re
import string
import spacy
import nltk
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
nltk.download('stopwords')

# Sklearn Packages (mainly for utility functions)
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score
from imblearn.under_sampling import RandomUnderSampler

np.random.seed(42)

def sub_special_tokens(text):
    # note I stole many of these regexes regularly from S.O.
    # convert simple URLs to xxurl token (e.g. www.google.com, http:google.com -> xxurl)
    text = re.sub(r' www.', ' http://www.', text)
    text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', ' xxurl ', text)
    # convert (British) phone numbers to xxphone token (e.g. 09058097218 -> xxphone)
    pat = r'\d{3}[-\.\s]??\d{4}[-\.\s]??\d{4}|\d{5}[-\.\s]??\d{3}[-\.\s]??\d{3}|(?:\d{4}\)?[\s-]?\d{3}[\s-]?\d{4})'
    text = re.sub(pat, ' xxphone ', text)
    # replace monetary values with xxmon token
    text = text.replace('£','$ ')
    text = re.sub(r'(\d+)[ ]{0,1}p', '$ 0.\1', text)
    text = re.sub(r'\$[ ]*(\d+[,\.])*\d+', ' xxmon ', text)
    # put xxup token before words in all caps (easy way to recognize info from capitalizing a word)
    text = re.sub(r'(\b[A-Z][A-Z0-9]*\b)', r' xxup \1 ', text)
    # put xxcap token before words with capitalized first letter (easy way to recognize first word in a sentence)
    text = re.sub(r'(\b[A-Z][a-z0-9]+\b)', r' xxcap \1 ', text)
    # convert some common text "emojis" to xxemoji: ;), :), :(, :-(, etc
    text = re.sub(r'[:;][ ]*[-]*[ ]*[()]', ' xxemoji ', text)
    return text

def normalize_text(text):
    # converts common patterns into special tokens
    # text = sub_special_tokens(text)
    # convert text to lowercase
    text = text.lower()
    # strip out any lingering html tags
    text = re.sub(r'<[^>]*>', '', text)
    # convert all common abrevs to regular word
    text = text.replace('&',' and ')
    text = re.sub(r'\bu\b', ' you ', text)
    text = re.sub(r'\bur\b', ' your ', text)
    text = re.sub(r'\b2\b', ' to ', text)
    text = re.sub(r'\b4\b', ' for ', text)
    # put spaces between punctuation (eg: 9.Blah -> 9 . Blah)
    puncts = r'[' + re.escape(string.punctuation) + r']'
    text = re.sub('(?<! )(?=' + puncts + ')|(?<=' + puncts + ')(?! )', r' ', text)
    # strip non-ascii characters (easy way to denoise text a bit)
    text = text.encode("ascii", errors="ignore").decode()
    # remove all punctuation except ?
    # text = re.sub(r"[^\w\s?]",' xxpunct ',text)
    text = re.sub(r"[^\w\s?]",' ',text)
    # convert all other numbers to xxnum token (e.g. 123, 1.2.3, 1-2-3 -> xxnum)
    # text = re.sub(r'\b([.-]*[0-9]+[.-]*)+\b', ' xxnum ', text)
    # remove nltk's common set of stop words (common for classical NLP analysis)
    stop_words = stopwords.words('english')
    text = ' '.join(word for word in text.split() if word not in stop_words)
    # stem words using nltk snowball stemmer, e.g. converts {run, running, runs} all to "run"
    stemmer = SnowballStemmer('english')
    stemmed_text = ''
    for word in text.split():
            stemmed_text = stemmed_text + stemmer.stem(word) + ' '
    text = stemmed_text
    # sub the occurance of 2 or more spaces with a single space
    text = re.sub(r'[ ]{2,}',' ',text)
    return text

def get_spam_data(balanced=False):
    text_file = Path.cwd().parent / 'resources/spam.csv'
    df = pd.read_csv(text_file, encoding='ISO-8859-1')
    df = df[['v1', 'v2']]
    df.columns = ['labels', 'text_raw']
    df.labels = df.labels.replace('ham', 0)
    df.labels = df.labels.replace('spam', 1)
    df['text'] = df['text_raw'].apply(normalize_text)
    df = df.drop('text_raw', axis=1)
    if balanced:
        X = df['text'].values.reshape(-1,1)
        y = df['labels'].values.reshape(-1,1)
        X,y = RandomUnderSampler().fit_resample(X, y)
        df = pd.DataFrame(data={'labels': y.flatten(), 'text': X.flatten()})
    df = df.sample(frac=1).reset_index(drop=True)
    return df
