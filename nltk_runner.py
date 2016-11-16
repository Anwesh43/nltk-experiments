import sys
paragraph='hey kevin! How are you? You have reduced a lot. But still you are handsome. By the way are you free tonight?'
words = ['Running','Crying','bathing','eating','call']
if(len(sys.argv) == 2):
    module=sys.argv[1]
    splittedWords = module.split("_")

    exec("from nltk_execs.{0} import *".format(module))
    if splittedWords[len(splittedWords)-1] == "stemmer":
        exec("run({0})".format(words))
    else:
        exec("run('{0}')".format(paragraph))
else:
    print 'please provide extra param'
