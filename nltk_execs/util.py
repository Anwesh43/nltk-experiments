from nltk import *
def get_words_from_paragraph(paragraph):
    words = []
    for sentence in sent_tokenize(paragraph):
        for word in word_tokenize(sentence):
            words.append(word)
    return words
