from nltk.tokenize import word_tokenize,sent_tokenize
def run(paragraph):
    sentences=sent_tokenize(paragraph)
    print sentences
    words=[]
    index=0
    for sentence in sentences:
        words[index:]=word_tokenize(sentence)
        index=len(words)+1
    print words
    print '$'.join(words)
