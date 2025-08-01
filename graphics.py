import tkinter as tk
import threading
import time
import graphics as static
import regex
import anime1_in_search
import anime1_in_download
static.on=False
def main(*event):
    if static.button["state"]==tk.DISABLED:
        return
    def lam():#async lambda
        name=static.enter.get()
        if name:
            seasons,urls=anime1_in_search.main(name)
            for season,url in zip(seasons,urls):
                anime1_in_download.main(season,url)
        static.button.config(state=tk.NORMAL)
    threading.Thread(target=lam).start()
    static.button.config(state=tk.DISABLED)
def inter(opitions):
    ans=None
    def set_ans(opition):
        nonlocal ans
        ans=opition if type(opition)==list else [opition]
    frame=tk.Frame(static.root)
    frame.pack()
    canvas=tk.Canvas(frame,width=200,height=300,bg="white",scrollregion=(0,0,200,60*len(opitions)+70))
    canvas.create_rectangle(10,10,190,60,fill="silver")
    canvas.create_text(100,20,text="select all")
    button=tk.Button(canvas,text="select",command=lambda opt=opitions:set_ans(opt))
    canvas.create_window(100,45,window=button)
    y=70
    for opition in opitions:
        canvas.create_rectangle(10,y,190,y+50,fill="silver")
        canvas.create_text(100,y+10,text=opition)
        button=tk.Button(canvas,text="select",command=lambda opt=opition:set_ans(opt))
        canvas.create_window(100,y+35,window=button)
        y+=60
    scrollY=tk.Scrollbar(frame,orient="vertical")
    scrollY.pack(side="right",fill="y")
    scrollY.config(command=canvas.yview)
    canvas.config(yscrollcommand=scrollY.set)
    canvas.pack(side="left")
    while not ans:
        time.sleep(0.1)
    frame.destroy()
    return ans
def outer(string,**args):
    output_box=static.output_box
    output_box.config(state=tk.NORMAL)
    while output_box.index("insert")!=output_box.index("end-1c"):
        output_box.delete("end-2c")
    if "end" in args:#\r
        output_box.insert("insert",string)
        output_box.mark_set("insert",output_box.index("insert").split(".")[0]+".0")
    else:
        output_box.insert("insert",string+"\n")
        output_box.mark_set("insert","end")
    output_box.config(state=tk.DISABLED)
if __name__ == "__main__":
    static.on=True
    static.root=tk.Tk()
    static.root.title("anime1-downloader")
    static.search=tk.Frame(static.root)
    static.search.pack(pady=2)
    static.enter=tk.Entry(static.search)
    static.enter.pack(padx=2,side="left")
    static.enter.bind("<Return>",main)
    static.button=tk.Button(static.search,text="search",command=main)
    static.button.pack(padx=5,side="right")
    static.output_box=tk.Text(static.root,height=10,width=50)
    static.output_box.pack(padx=5,pady=5,side="bottom")                       
    static.root.mainloop()
