import requests
from bs4 import BeautifulSoup
import json
movieurl="https://www.rottentomatoes.com/m/toy_story_4"
movieName="toy_story_4"
def scrape_movie_details(movieName,movieurl):
    url=requests.get(movieurl)
    data=BeautifulSoup(url.text,"html.parser")
    mainDiv=data.find_all("li",class_="meta-row clearfix")
    # print(mainDiv)
    dict1={}
    for i in mainDiv:           
        a=i.text
        b=a.split(":")
        # print(b)
        if "\nRating" in b:
            dict1["Rating"]= b[1].replace("\n","").strip()
        elif "\nGenre" in b:
            ga=b[1].replace("\n                        ","").strip()
            list1=[]
            s=""
            for i in ga:
                if i==",":
                    list1.append(s)
                    s=""
                else:
                    s+=i                
            dict1["Genre"]=list1
        elif "\nOriginal Language" in b:
            dict1["language"]=b[1].replace("\n","").strip()
            # dir1=[j.strip() for j in b]
            # dict1["language"]=dir1

        elif "\nDirector" in b:
            i=0
            list2=[]
            while i <len(b):
                if i==0:
                    i+=1
                    continue
                list2.append(b[i].replace("\n",""))
                i+=1
            dict1["director"]=list2
        elif "\nProducer" in b:
            i=0
            list3=[]
            while i <len(b):
                if i==0:
                    i+=1
                    continue
                list3.append(b[i].replace("\n        ","").strip())
                i+=1
            # dir2=[k.replace("Producer","") for k in b]
            # print(dir2)
            dict1["Producer"]=list3
        elif "\nRuntime" in b:
            print(b)
            print(movieName)
            s=b[1].replace("\n","").strip()
            h=int(s[0])*60
            i=0
            j=" "
            while i<len(s):
                if s[i]=="h" or s[i]=="m"  or s[i]==" " or i==0 or s[i]=="M":
                    i+=1
                    continue
                else:
                    j+=s[i]
                    i+=1
                h+=int(j)
                
            # print(j)
            # print(type(j))
            # print(h)
            # h+=int(j)
            dict1["Runtime"]=h
            dict1["movieName"]=movieName                   
    with open("task4.json","w+") as file4:
            json.dump(dict1,file4,indent=4)
            a=json.dumps(dict1)
            return dict1
scrape_movie_details("toy_story_4","https://www.rottentomatoes.com/m/toy_story_4")