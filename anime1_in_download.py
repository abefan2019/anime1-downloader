import os
import ffmpeg #ffmpeg-python
import web
import regex
def search(url):
    urls=[]
    codes=[]
    n=1
    urls.append(url)
    codes.append(web.html(urls[-1]))
    while "<article" in codes[-1]:
        n+=1
        print("Found:",web.decode(urls[-1]))
        urls.append(url+"page/"+str(n))
        codes.append(web.html(urls[-1]))
    urls.pop()
    codes.pop()
    print(len(urls),"urls found")
    return codes
def ep_urls(code):
    eps={}
    code=regex.find(code,"<main","</main>")[0]
    animes=regex.find(code,"<article","</article>")
    for anime in animes:
        data=regex.find(anime,'<h2 class="entry-title">',"</h2>")[0]
        href="https://anime1.in"+regex.find(data,'"','"')[0]
        name=regex.find(data,">","<")[0]
        eps[name]=href
    return eps
def tmp():
    if os.path.exists("tmp") and os.path.isdir("tmp"):
        files=os.listdir("tmp")
        for file in files:
            os.remove(os.path.join("tmp",file))
    else:
        os.mkdir("tmp")
def download(url):
    tmp()
    code=web.html(url)
    nurl="https://anime1.in"+regex.find(code,'" src="','"')[0]#player
    ncode=web.html(nurl)
    murl=regex.find(ncode,'<source src="','"')[0]#m3u8
    mcode=web.html(murl)
    murl=regex.path(murl)+regex.files(mcode,"m3u8")[0]#true m3u8
    mcode=web.html(murl)
    m3u8=regex.m3u8(murl,regex.files(mcode,"ts"))
    for i in range(len(m3u8)):
        web.save(m3u8[i],os.path.join("tmp","%06d"%i+".ts"))
        print("saving","%.1f"%(i/len(m3u8)*100)+"%",end="\r")
    print("saving 100% ")
def combine(season,name):
    files=sorted(os.listdir("tmp"))
    txt=os.path.join("tmp",'order.txt')
    with open(txt,"w") as f:
        for file in files:
            f.write("file '"+file+"'\n")
    ffmpeg.input(txt,format="concat").output(os.path.join("anime",season,name+".mp4"),c='copy').run()
    tmp()
def main(season,url):
    codes=search(url)
    eps={}
    for code in codes:
        eps.update(ep_urls(code))
    eps=dict(sorted(eps.items()))
    names=list(eps.keys())
    for i in range(len(names)):
        print("("+str(i+1)+")",names[i])
    n=input("choose (None for all): ")
    if n:
        n=int(n)
        name=names[n-1]
        eps={name:eps[name]}
    for ep in eps:
        print(ep,"downloading")
        download(eps[ep])
        print(ep,"downloaded")
        print(ep,"combining")
        combine(season,ep)
        print(ep,"combined")
        print(ep,"finished")
