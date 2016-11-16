import sys
paragraph = ''
try:
    with open('./input.txt') as f:
        paragraph = f.read()
except:
    print 'file does not exist'
paragraph = paragraph.replace('\n','')
print paragraph
if(len(sys.argv) == 2):
    module=sys.argv[1]
    splittedWords = module.split("_")

    exec("from nltk_execs.{0} import *".format(module))
    exec("run('{0}')".format(paragraph))
else:
    print 'please provide extra param'
