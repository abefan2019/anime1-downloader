import re
def find(code,s1,s2):
    return re.findall(s1+"(.*?)"+s2,code,re.DOTALL)
def files(code,types):
    return re.findall(".*"+types,code)
def path(url):
    while True:
        if url[-1]=="/":
            break
        else:
            url=url[:-1]
    return url
def full_path(murl,file):
    return file if "http" in file else path(murl)+file
