from urllib import request
from datetime import datetime
import json


def getData(url):
    """returns the top 20 json objects of the specified url :)"""
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    response = request.urlopen(url)
    string = response.read().decode('utf-8')
    json_Response = json.loads(string)
    if json_Response['status'] != 'ok':
        print('error occured :status '+json_Response['status'])
        return None
    return json_Response['articles']

def converJsonDateToPython(Articles):
    """Converts the json date string in each article to the python date"""
    i = 0
    for article in Articles:
        article['publishedAt']=article['publishedAt'].replace('+','Z')
        article['publishedAt']=article['publishedAt'].split('Z')[0]
        article['publishedAt'] = article['publishedAt'].split('.')[0]
        pydate = datetime.strptime(article['publishedAt'],"%Y-%m-%dT%H:%M:%S")
        article['publishedAt']=pydate.strftime("%d/%m/%Y, %H:%M")
        article['id'] = i
        i += 1
    return Articles
