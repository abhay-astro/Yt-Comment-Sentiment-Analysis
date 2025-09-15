import os
import json
import urllib.parse as urlparse

import googleapiclient.discovery
#remember to use your developer key every 90 days or it just expires
#the quota system refreshes after like 10 days

def parseForId(value):
    """
    Examples:
    - http://youtu.be/SA2iWivDJiE
    - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
    - http://www.youtube.com/embed/SA2iWivDJiE
    - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
    """
    query = urlparse.urlparse(value)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ('www.youtube.com', 'youtube.com'):
        if query.path == '/watch':
            p = urlparse.parse_qs(query.query)
            return p['v'][0]
        if query.path[:7] == '/embed/':
            return query.path.split('/')[2]
        if query.path[:3] == '/v/':
            return query.path.split('/')[2]
    # fail?
    return None

def getComment(url):
    comment=[]
    url=parseForId(url)
    # print(url)
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        textFormat="plainText",
        # videoId="AaZ_RSt0KP8",
        videoId=url,
        order="relevance",
        maxResults=100

    )
    response = request.execute()
    # data=json.loads(response)

    # print(response)
    b=response['items']
    for i in b:
       c=i["snippet"]
       topLevelComment=c["topLevelComment"]
       snippetLast=topLevelComment["snippet"]
       comment.append(snippetLast["textDisplay"])

    return comment


