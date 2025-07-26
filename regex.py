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
def m3u8(murl,files):#remove ad
    if "http" in files[0]:
        uuid=files[0].split("/")[-4]
        return [file for file in files if file.split("/")[-4]==uuid]
    else:
        uuid=int(files[-1][-9:-3])
        return [path(murl)+file for file in files if int(file[-9:-3])<=uuid]
