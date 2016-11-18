import nltk
def run(paragraph):
    sentences = nltk.sent_tokenize(paragraph)
    pos_per_sent = []
    speech_dict = {}
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        pos_tag =nltk.pos_tag(words)
        for pst in pos_tag:
            W,S = pst
            if not(speech_dict.has_key(S)):
                speech_dict[S] = 0
                print S
            speech_dict[S] = speech_dict[S]+1
    print pos_per_sent
    print speech_dict
