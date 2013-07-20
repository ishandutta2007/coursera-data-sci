import urllib
import json


#print type(rdict)
#print response.read()
#print rdict.keys()
#print type (rdict[u'results'])
#print rdict[u'results'][0]
#print rdict[u'results'][0][u'text']


for page in range(1,10):
    print '======= Page '+str(page)+'=======' 
    response = urllib.urlopen("http://search.twitter.com/search.json?q=la+crisis&page="+str(page))
    rdict = json.load(response)
    for i in rdict[u'results']:
        print "@"+i[u'from_user_name']+": "+i[u'text']


#print rdict.items()
#jres = json.JSONDecoder().decode(response)
#print jres
#print json.dumps(jres, sort_keys= False,indent=4, separators=(",",": "))
