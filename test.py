import urllib2
import json
import os

def getall(): #This accesses the txt to get all the champions and IDs without having to access the API each time.
    if not os.path.isfile("champions.txt"):
        writeall()
    f = open("champions.txt","r")
    champs = f.readlines()
    every = {}
    for a in champs:
        both = a.split(":")
        every[int(both[0])] = both[1]
    return every

def writeall(): #This uses the Riot API to update the list of champions and their correlated champion IDs. Stored in a txt.
    every = {0:"All Champions"}
    for a in range(122):
        b = a+1
        failed = [46,47,49,52,65,66,70,71,73,87,88,93,94,95,97,100,108,109,116,118]
        for a in failed:
            every[a]="STUPID RIOT HAS A HORRIBLE API AND HAS NO PAGE FOR THIS NUMBER"
        if not b in failed:
            url = """
        https://na.api.pvp.net/api/lol/static-data/na/v1.2/champion/"""+str(b)+"""?api_key=5ac2dcac-bbf6-4147-b4e7-199143508b63
        """
            request = urllib2.urlopen(url)
            result = request.read()
            d = json.loads(result)
            every[b]=d["name"] + " " + d["title"]
    f = open("champions.txt","w")
    for a in every.keys():
        f.write(str(a) + ":" + every[a] + "\n")
    f.close()
    
def convert(input): #Gets rid of unicode text
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def getSummonerData(summ): #Gets the summoner data for a certain name
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
    
    return d
