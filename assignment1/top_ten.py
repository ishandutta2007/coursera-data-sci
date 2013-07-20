import sys
import json
from operator import itemgetter

hashtag_f = {} # initialize an empty dictionary

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

def topTen(tweet_file):
    for line in tweet_file:
        tweet = json.loads(line)
        if (u'delete' in tweet):
            continue
        #hashtags = [u'hashtags']
        for h in tweet[u'entities'][u'hashtags']:
            hashstr=h[u'text']
            if hashstr in hashtag_f.keys():
                hashtag_f[hashstr]+=1
            else:
                hashtag_f[hashstr]=1

def printTopTen():
    #for k,v in hashtag_f.items():
    #    print k + " " + str(v)
    sl = sorted(hashtag_f.iteritems(), key=itemgetter(1), reverse=True)   
    maxtop = 10 if len(sl)>10 else len(sl)
    for i in range(0,maxtop):
        print sl[i][0]+" "+str(float(sl[i][1]))

def main():
    tweet_file = open(sys.argv[1])
    topTen(tweet_file)
    printTopTen()

if __name__ == '__main__':
    main()
