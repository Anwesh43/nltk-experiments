from nltk import word_tokenize,sent_tokenize
import pandas as pd
def filterSymbols(word):
    symbols = [',','.','?','!']
    return word not in symbols
def run(paragraph):
    sentences = sent_tokenize(paragraph)
    wordArrays = [word_tokenize(sentence) for sentence in sentences]
    words = []
    for wordArray in wordArrays:
        if len(words) == 0:
            words = wordArray
        else:
            words = words+wordArray
    words =  filter(filterSymbols,words)
    word_freq_dist = {}
    for word in words:
        if word not in word_freq_dist.keys():
            word_freq_dist[word] = 0
        word_freq_dist[word] = word_freq_dist[word]+1
    print word_freq_dist
    df = pd.DataFrame(zip(word_freq_dist.keys(),word_freq_dist.values()),columns=['Word','Count'])
    print df
