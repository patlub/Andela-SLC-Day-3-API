import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def sources():
    """Returns all valid news sources"""
    sources = ['techcrunch', 'techradar', 'ars-technica']
    for source in sources:
        print(source)
    return sources


def fetch_news(source):
    """
    Http Client to interact with NASA's public APi

    Args:
        source: News Source
    """
    sources = ['google-news', 'hacker-news', 'techcrunch',
               'techradar', 'ars-technica']
    if source not in sources:
        print('Invalid Source')
        return 'Invalid Source'
    else:
        api_key = '51ffb1a860b7437cbd213e7e16c1c5c7'

        print('Fetching News from ' + source + '.................\n')
        req_url = 'https://newsapi.org/v1/articles?source=' + source + '&apiKey=' + api_key
        req = Request(req_url)
        try:
            response = urlopen(req)

        # Returns error from server
        except HTTPError as e:
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)

        # Returns error if server is unreachable
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.reason)

        # json parse the response to print only the relevant information
        else:
            json_obj = json.load(response)
            print('Source:' + json_obj['source'] + '\n')
            for article in json_obj['articles']:
                print('Author: ' + article['author'] + '\n')
                print('Title: ' + article['title'] + '\n')
                print('Article: ' + article['description'] + '\n')

                print('=========================================')
