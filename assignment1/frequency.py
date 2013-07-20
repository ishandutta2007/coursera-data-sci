import sys
import json

wfreq = {}
wcount = 0.0

def count(tweet_file):
    global wcount
    global wfreq
    for line in tweet_file:
        tweet = json.loads(line)
        if (u'delete' in tweet):
            continue
        twords = tweet[u'text'].split()
        for w in twords:
            w = w.lower()
            if w in wfreq.keys():
                wfreq[w]+=1
            else:
                wfreq[w]=1
                wcount+=1

def frequency(tweet_file):
    count(tweet_file)
    for w in wfreq.keys():
        f = float(wfreq[w]/wcount)
        print w+" "+str(round(f, 4))

def main():
    tweet_file = open(sys.argv[1])
    frequency(tweet_file)
    

if __name__ == '__main__':
    main()
