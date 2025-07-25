import anime1_in_search
import anime1_in_download
def main():
    while True:
        name=input("name: ")
        if name:
            season,url=anime1_in_search.main(name)
            anime1_in_download.main(season,url)
        else:
            break
    print("Program finished")
main()
