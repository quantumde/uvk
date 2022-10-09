from . import Api

class Wall:
    def __init__(self, access_token, id, api_version):
        self.access_token, self.id, self.api_version = access_token, id, api_version
    
    def post(self,wall_id,message,from_group=0,signed=0,friends_only=0,close_comments=0,mute_notifications=0)->int:
        data=Api.post(self.access_token, "wall.post", self.api_version, owner_id=wall_id,
        friends_only=friends_only, from_group=from_group,
        message=message, signed=signed, close_comments=close_comments,
        mute_notifications=mute_notifications, )
        if not data.get("response") or not data.get("response").get("post_id"):
            return -1
        return data.get("response").get("post_id")