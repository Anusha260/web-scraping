import requests
import json
import os
import time
import random
from bs4 import BeautifulSoup
from task1 import moviedata
from task5 import get_movie_list_details

with open('task5.json','r') as f:
    a=json.load(f)
movies_data=a
# print(movies_data)
def moviedata(movies_data):
    for i in movies_data:
            random_sleep=random.randint(1,3)
            path=open("/home/dell50/Desktop/web scraping/9.txt"+i["moviename"]+".txt",'w')
            a=str(i)
            create=path.write(a)
            time.sleep(random_sleep)
            path.close()
moviedata(movies_data)





