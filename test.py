import urllib2
import json

def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def getSummonerData(summ):
    url = """
    https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/%s?api_key=82bf0ad8-fcb0-4fe8-a911-ab05d5693242
    """
    url = url%(summ)

    result = urllib2.urlopen(url)
    something = result.read()
    d = json.loads(something)
    for a in d:
        summID = d[a]["id"]

    #print summID

    url = """
    https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/%s/ranked?season=SEASON4&api_key=82bf0ad8-fcb0-4fe8-a911-ab05d5693242
    """
    url = url%(summID)

    result = urllib2.urlopen(url)
    something = result.read()
    d = convert(json.loads(something))
    #fixed = {}
    #fixed["modifyDate"] = d[d.keys()[0]]
    #fixed["summonerId"] = d[d.keys()[1]]
    #fixed["champions"] = d[d.keys()[2]]
    
    print(d["champions"][0]["id"])
    return d

