import unittest

from pip._vendor import requests

from HttpClient.http_client import sources, fetch_news

class HttpClientTestCase(unittest.TestCase):

    def test_news_sources(self):
        self.assertEquals(sources(),
                          ['techcrunch', 'techradar', 'ars-technica'])

    def test_fetch_news_from_invalid_source(self):
        self.assertEquals(fetch_news('Kampala'),
                          'Invalid Source')

    def test_api_call_is_valid(self):
        api_key = '51ffb1a860b7437cbd213e7e16c1c5c7'
        source = 'techcrunch'
        response = requests.get('https://newsapi.org/v1/articles?source=' + source + '&apiKey=' + api_key)
        self.assertTrue(response.ok)


if __name__ == '__main__':
    unittest.main()
