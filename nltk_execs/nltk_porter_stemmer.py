from nltk.stem import PorterStemmer
def run(words):
    ps = PorterStemmer()
    stemmed_words = []
    for word in words:
        stemmed_words.append(ps.stem(word))
    print stemmed_words
