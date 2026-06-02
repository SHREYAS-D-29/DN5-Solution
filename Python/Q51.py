import hashlib
class URLShortener:
    def __init__(self): self.db={}
    def shorten(self,url):
        s=hashlib.md5(url.encode()).hexdigest()[:6]; self.db[s]=url; return s
u=URLShortener(); code=u.shorten('https://example.com'); print(code,u.db[code])
