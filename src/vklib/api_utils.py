api_base="https://api.vk.com/method/"
def format_url(access_token, method, api_version, **kwargs):
    url=api_base+method+"?v={}&access_token={}".format(api_version, access_token) + \
    "&" + "&".join("{}={}".format(a, kwargs[a]) for a in kwargs)
    return url