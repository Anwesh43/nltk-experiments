import sys
paragraph='hey kevin! How are you? You have reduced a lot. But still you are handsome. By the way are you free tonight?'
if(len(sys.argv) == 2):
    module=sys.argv[1]
    exec("from nltk_execs.{0} import *".format(module))
    exec("run('{0}')".format(paragraph))
else:
    print 'please provide extra param'
