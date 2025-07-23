import urllib.request
import time
opener=urllib.request.build_opener()
opener.addheaders=[("User-Agent","Chrome/123.0.0.0")]
urllib.request.install_opener(opener)
def encode(url):return urllib.parse.quote(url)
def decode(url):return urllib.parse.unquote(url)
def html(url):
    time.sleep(0.1)
    while True:
        try:
            fp=urllib.request.urlopen(url)
            mybytes=fp.read()
            string=mybytes.decode("utf8")
            fp.close()
            break
        except:
            print("failed to get",url)
            print("try again in 5 second")
        time.sleep(5)
    time.sleep(0.1)
    return string
def save(url,name):
    time.sleep(0.1)
    while True:
        try:
            urllib.request.urlretrieve(url,name)
            break
        except:
            print("failed to save",url)
            print("try again in 5 second")
        time.sleep(5)
    time.sleep(0.1)
    
