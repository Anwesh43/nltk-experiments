from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
def run(paragraph):
    ps = PorterStemmer()
    stemmed_words = []
    paragraph = paragraph.replace('.','')
    words = word_tokenize(paragraph)
    print words
    for word in words:
        stemmed_words.append(ps.stem(word))
    print stemmed_words
