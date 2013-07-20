import sys
import json

scores = {} # initialize an empty dictionary
states = {} 

def buildDictionary(afinnfile):
    for line in afinnfile:
      term, score  = line.split("\t") 
      scores[term] = int(score) 
    # print scores.items() # Print every (term, score) pair in the dictionary

def sent(text, st):
    #print st
    if st == "US":    
        return
    if len(st) > 2:
        return
    words, tsent = text.split(" "), 0
    for w in words:
        w = w.lower()
        if (w in scores):
            tsent += scores[w]
    if st in states.keys():
        states[st]+=tsent
    else:
        states[st]=tsent

def computeSents(tweet_file):
    for line in tweet_file:
        tweet = json.loads(line)
        if (u'delete' in tweet):
            continue
        place = tweet[u'place']
        user = tweet[u'user']
        if (place and place[u'country_code']=="US"):
            #print place[u'full_name']+ " @ "+user[u'location']
            sent(tweet[u'text'], place[u'full_name'].split(',')[1].strip())   

def printHappiest():
    max = 0
    for st in states.keys():
        if (states[st] > max):
            max = states[st]
            happiest = st
    print str(happiest)
    

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    buildDictionary(sent_file)
    computeSents(tweet_file)
    printHappiest()

if __name__ == '__main__':
    main()
