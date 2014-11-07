import urllib2
import json
url = """
https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/NoNamer69?api_key=82bf0ad8-fcb0-4fe8-a911-ab05d5693242
"""

result=urllib2.urlopen(url)
something = result.read()
d = json.loads(something)
for a in d:
    summID = d[a]["id"]

#print summID
    
url = """
https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/%s/ranked?season=SEASON4&api_key=82bf0ad8-fcb0-4fe8-a911-ab05d5693242
"""
url = url%(summID)

result=urllib2.urlopen(url)
something = result.read()
d = json.loads(something)
for a in d:
    print d[a]
