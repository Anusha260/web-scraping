import requests
import json
import os
from bs4 import BeautifulSoup
from task1 import moviedata
from task4 import scrape_top_movie

with open('Task1.json','r') as f:
    a=json.load(f)
movies_data=a

def moviedata():
    
    for i in movies_data:
        path="/home/dell50/Desktop/web scraping/.txt"+i["moviename"]+".text"
        # print(path)
        if os.path.exists('file.json'):
            pass
        else:
            create=open("/home/dell50/Desktop/web scraping/.txt"+i["moviename"]+".text","w")
            url=requests.get(i["movieurl"])
            create1=create.write(url.text)
            create.close()

moviedata()

