import sys
import json

scores = {} # initialize an empty dictionary
dscores = {} # derived scores 

def buildDictionary(afinnfile):
    for line in afinnfile:
      term, score  = line.split("\t") 
      scores[term] = int(score) 
    # print scores.items() # Print every (term, score) pair in the dictionary

def derive (pos, neg):
    if ((pos-neg) is 0):
        return 0.0
    if (pos is 0):
        return float(-neg+0.5)
    if (neg is 0):
        return float(pos-0.5)
    return ((float(pos)/float(neg))-1)

def addScores (newterms, score):
    for term in newterms:
        if (term not in dscores):
            dscores[term]=[]
        dscores[term].append(score)
            

def sent(text):
    words, tsent = text.split(" "), 0
    newterms = []
    for w in words:
        w = w.lower()
        neg = 0
        pos = 0
        if (w in scores):
            score = scores[w]
            tsent += score
            if (score>0): 
                pos+=1
            elif (score<0):
                neg+=1
        else:
            newterms.append(w)
    addScores(newterms, derive(pos, neg))
    #print str(float(tsent))

def printResults():
    for k in dscores.keys():
        total, count = 0.0, 0;
        for value in dscores[k]:
            total+=value
            count+=1
        print k+" "+str(total/count)

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
    printResults()
    

if __name__ == '__main__':
    main()
