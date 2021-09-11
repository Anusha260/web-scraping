import json
import os
import requests
from bs4 import BeautifulSoup
from task1 import moviedata

from task5 import get_movie_list_details
with open("task5.json","r") as f:
    movie_url=json.load(f) 
    a=movie_url
def get_movie_details():
    dict={}
    c=0
    for i in a:
    
        if i["LANGUAGE"]==["English"]:
            c=c+1
        else:
            pass
    dict["LANGUAGE"]=c
    with open("task6.json","w+") as file:
            json.dump(dict,file,indent=4)
    return c
get_movie_details()
                  





