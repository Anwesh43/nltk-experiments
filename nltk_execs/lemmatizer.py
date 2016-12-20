from nltk.stem import WordNetLemmatizer
from util import *
def run(paragraph):
    lemmatizer = WordNetLemmatizer()
    words = get_words_from_paragraph(paragraph)
    lWords =  map(lemmatizer.lemmatize,words)
    print lWords
