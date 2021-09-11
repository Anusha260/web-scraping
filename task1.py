import requests
from bs4 import BeautifulSoup
import json
user=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
data=BeautifulSoup(user.text,"html.parser")
# print(data)
def moviedata():
    List=[]
    maindiv=data.find("div",class_="body_main container")
    subdiv=maindiv.find("table",class_="table")
    table=subdiv.find_all("tr")
    for i in table:
        d1={}
        alltds=i.find_all('td')
        for j in alltds:
            rank=i.find("td",class_="bold").get_text()[:-1]
            d1["rank"]=int(rank)
            rating=i.find("span",class_="tMeterScore").get_text()[1:3]
            d1["rating"]=int(rating)
            review=i.find("td",class_="right hidden-xs").get_text()
            d1["review"]=int(review)
            moviename=i.find("a",class_="unstyled articleLink")["href"][3:]
            d1["moviename"]=moviename
            movieurl=i.find("a",class_="unstyled articleLink")["href"]
            URL="https://www.rottentomatoes.com/"+movieurl
            d1["movieurl"]=URL
            movieyear=i.find("a",class_="unstyled articleLink").text
            year=movieyear.strip()
            d1["movieyear"]=int(movieyear[-5:-1])
            # List.append(d1.copy())
            if d1 not in List:
                List.append(d1.copy())
        list2=[]
        for i in List:
            if i!={}:
                list2.append(i)
    with open("Task1.json","w+") as file:
        json.dump(list2,file ,indent=4)
    return list2
moviedata()

    