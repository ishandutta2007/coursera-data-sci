import sys
import json

scores = {} # initialize an empty dictionary

def buildDictionary(afinnfile):
    for line in afinnfile:
      term, score  = line.split("\t") 
      scores[term] = int(score) 
    # print scores.items() # Print every (term, score) pair in the dictionary

def sent(text):
    words, tsent = text.split(" "), 0
    for w in words:
        w = w.lower()
        if (w in scores):
            tsent += scores[w]
    print str(float(tsent))

def computeSents(tweet_file):
    for line in tweet_file:
        tweet = json.loads(line)
        if (u'delete' in tweet):
            continue
        twords, tsent = tweet[u'text'].split(" "), 0
        sent(tweet[u'text'])
        #print "@"+tweet[u'user']+": "+tweet[u'text']


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    buildDictionary(sent_file)
    computeSents(tweet_file)
    

if __name__ == '__main__':
    main()
