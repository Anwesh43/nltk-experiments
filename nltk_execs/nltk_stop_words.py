from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
def run(paragraph):
    sentences=sent_tokenize(paragraph)
    words=[]
    index=0
    for sentence in sentences:
        words[index:]=word_tokenize(sentence)
        index=len(words)+1
    stop_word_set=set(stopwords.words('english'))
    suitable_words=[]
    for word in words:
        if not(word.lower() in stop_word_set):
            suitable_words.append(word)
    print suitable_words
