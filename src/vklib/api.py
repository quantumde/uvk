import requests
from .api_utils import format_url

class Api:

    @staticmethod
    def get(access_token, method, api_version, **kwargs):
        url=format_url(access_token, method, api_version, **kwargs)
        req=requests.get(url)
        return req.json()

    @staticmethod
    def post(access_token, method, api_version, **kwargs):
        url=format_url(access_token, method, api_version, **kwargs)
        req=requests.post(url)
        return req.json()