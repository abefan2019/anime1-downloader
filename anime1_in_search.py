import os
import web
import regex
def search(name):
    urls=[]
    codes=[]
    n=1
    urls.append(true_url(n,name))
    codes.append(web.html(urls[-1]))
    while "/page" in codes[-1]:
        n+=1
        print("Found:",web.decode(urls[-1]))
        urls.append(true_url(n,name))
        codes.append(web.html(urls[-1]))
    urls.pop()
    codes.pop()
    print(len(urls),"urls found")
    return codes
def true_url(n,name):
    return "https://anime1.in/page/"+str(n)+"?s="+web.encode(name)
def season_urls(code):
    urls=[]
    code=regex.find(code,"<main","</main>")[0]
    animes=regex.find(code,"<article","</article>")
    for anime in animes:
        data=regex.find(anime,'<div class="entry-meta">',"</div>")[0]
        href="https://anime1.in"+regex.find(data,'href="','"')[0]
        urls.append(href)
    return urls
def get_title(url):
    code=web.html(url)
    title=regex.find(code,'<h1 class="page-title">',"</h1>")[0]
    return title
def main(name):
    codes=search(name)
    seasons=[]
    for code in codes:
        seasons+=season_urls(code)
    seasons=list(set(seasons))
    print(len(seasons),"animes found")
    results={}
    for i in range(len(seasons)):
        print("reading",str(int(i/len(seasons)*100))+"%",end="\r")
        title=get_title(seasons[i])
        results[title]=seasons[i]
    print("reading 100%")
    del seasons
    results=dict(sorted(results.items()))
    names=list(results.keys())
    for i in range(len(names)):
        print("("+str(i+1)+")",names[i])
    n=int(input("choose: "))
    name=names[n-1]
    url=results[name]
    print("choosed",name)
    os.makedirs(os.path.join("anime",name),exist_ok=True)
    return name,url
