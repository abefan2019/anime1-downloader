import os
import anime1_in_search
import anime1_in_download
def main():
    if (not os.path.exists("anime"))or(not os.path.isdir("anime")):
        os.mkdir("anime")
    while True:
        name=input("name: ")
        if name:
            url=anime1_in_search.main(name)
            anime1_in_download.main(url)
        else:
            break
    print("Program finished")
main()
