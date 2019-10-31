import urllib.request
import json

from .key import Apikey
from .handlers import title_url


def title_request(title):
    '''
    get data from omdbapi
    '''
    title = title_url(title)
    url = 'http://www.omdbapi.com/?apikey={apikey}&t={title}&'.format(apikey=Apikey.APIKEY, title=title)
    response = urllib.request.urlopen(url)
    body = response.read()

    return json.loads(body.decode("utf-8"))
