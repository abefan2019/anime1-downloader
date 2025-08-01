import re
import tkinter as tk
import graphics
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
def inter(opitions):
    if graphics.on:
        return graphics.inter(opitions)
    else:
        for i in range(len(opitions)):
            print("("+str(i+1)+")",opitions[i])
        n=0
        while True:
            n=input("choose (None for all): ")
            if n:
                try:
                    n=int(n)
                    if not (n<1 or n>len(opitions)):
                        return [opitions[n-1]]
                except:
                    pass
                print("enter number between 1 and",len(opitions))
            else:
                return opitions
def outer(*texts,**args):
    string=""
    for text in texts:
        string+=str(text)+" "
    if graphics.on:
        graphics.outer(string,**args)
    else:
        if "end" in args:
            print(string,end=args["end"])
        else:
            print(string)
