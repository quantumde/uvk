import requests
from .wall import Wall
from vklib import wall

class VK:
    oauth_api_base="https://oauth.vk.com/"
    api_version=5.131
    access_token=None
    __id=-1

    def __init__(self,app_id,app_secret,scopes=5059598):
        self.app=app_id,app_secret
        self.scopes=scopes
    
    def __format_clientinfo(self):
        return "client_id={}&client_secret={}".format(*self.app)
    
    def auth(self, username, password):
        url = self.oauth_api_base+"token?grant_type=password&" + \
            self.__format_clientinfo() + "&" + \
            "username={}&password={}".format(username,password) + "&" + \
            "v={}".format(self.api_version) + "&" \
            "scopes={}".format(self.scopes)
        req=requests.get(url)
        data=req.json()
        if data.get("error"):
            print("ERROR LOGIN: UNIMPLEMENTED")
        self.access_token=data.get("access_token")
        self.__id=data.get("user_id")
    
    @property
    def id(self):
        return self.__id

    @property
    def isAuth(self):
        return self.access_token!=None and self.__id > 0
    
    @property
    def wall(self):
        if not self.isAuth:
            return None
        return Wall(self.access_token, self.id, self.api_version)