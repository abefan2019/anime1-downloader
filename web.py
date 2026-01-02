import urllib.request
import time
import regex
import concurrent.futures
opener=urllib.request.build_opener()
opener.addheaders=[("User-Agent","Chrome/123.0.0.0")]
urllib.request.install_opener(opener)
def encode(url):return urllib.parse.quote(url)
def decode(url):return urllib.parse.unquote(url)
def html(url):
    time.sleep(0.1)
    p=False
    while True:
        try:
            fp=urllib.request.urlopen(url)
            mybytes=fp.read()
            string=mybytes.decode("utf8")
            fp.close()
            break
        except:
            regex.outer("failed to get",url)
            regex.outer("try again in 5 second")
            p=True
        time.sleep(5)
    if(p):
        regex.outer("get",url)
    time.sleep(0.1)
    return string
def save(url,name):
    p=False
    while True:
        try:
            urllib.request.urlretrieve(url,name)
            break
        except:
            regex.outer("failed to save",url)
            regex.outer("try again in 5 second")
            p=True
        time.sleep(5)
    if(p):
        regex.outer("save",url)
def saves(urls,names):
    done=0
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        job=[executor.submit(save,url,name) for url,name in zip(urls,names)]
        for _ in concurrent.futures.as_completed(job):
            done+=1
            regex.outer("saving","%.1f"%(done/len(urls)*100)+"%",end="\r")
    regex.outer("saving 100%")
