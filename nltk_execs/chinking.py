from nltk import *
def run(paragraph):
    words = []
    sentences = sent_tokenize(paragraph)
    for sentence in sentences:
        for word in word_tokenize(sentence):
            words.append(word)
    tagged_words = pos_tag(words)
    chunkGrams = r"""Chunk:{<.*>+}
                }<PRP.?><VBZ.?><VBG.?><IN>?<NNP.?>{"""
    parser = RegexpParser(chunkGrams)
    chunks = parser.parse(tagged_words)
    print chunks
    chunks.draw()
