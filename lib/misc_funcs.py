import re
import requests

def stripNoiseSub(string : str):
    #removing code comments (both kinds)
    string = re.sub("\/\*.*\*\/", "", string, flags=re.DOTALL)
    string = re.sub("\/\/.*", "", string)
    
    #removing all whitespace except whitespace within quotes
    listPartition = string.split('"')
    for index, segment in enumerate(listPartition):
        if index%2 == 0:
            listPartition[index] = re.sub("\s+", "", segment)
            
    return ('"'.join(listPartition))

def getAuthToken(email, password):
    pass
    
