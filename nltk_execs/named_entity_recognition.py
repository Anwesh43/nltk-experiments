from nltk import *
from util import *
def run(paragraph):
    words = get_words_from_paragraph(paragraph)
    tagged_words = pos_tag(words)
    named_entities = ne_chunk(tagged_words)
    print named_entities
    named_entities.draw()
