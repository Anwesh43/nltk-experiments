from nltk import *
def run(paragraph):
    sentences = sent_tokenize(paragraph)
    words = []
    for sentence in sentences:
        for word in word_tokenize(sentence):
            words.append(word)
    tagged_words = pos_tag(words)
    chunkGrams = r"""Chunk:{<PRP.?><VBZ.?><VBG.?><IN>?<NNP.?>}"""
    parser = RegexpParser(chunkGrams)
    chunks = parser.parse(tagged_words)
    print chunks
    print type(chunks)
    print chunks.__dict__
    chunks.draw()
