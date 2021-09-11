import requests
import json
from bs4 import BeautifulSoup
from task1 import moviedata
from task5 import scrape_top_movie

with  open("task5.json","r") as f:
    data=json.load(f)
# print(data)
# s_data=data

def  analyse_language_and_directors():
    dic={}
    for i in data:
        # print(i)
        for Director in i["Director"]:
            # print(Director)
            dic[Director]={}
        # print(dic)
    for i in range(len(data)):
        for Director in dic:
            if  Director in data[i]["Director"]:
                for  LANGUAGE  in data[i]["LANGUAGE"]:
                    dic[Director][LANGUAGE]=0
        # print(dic)
    for i in range(len(data)):
        for Director in dic:
            if  Director in data[i]["Director"]:
                for LANGUAGE  in data[i]["LANGUAGE"]:
                    dic[Director][LANGUAGE]+=1
        # print(dic)
        with open("task10.json","w") as f:
            json.dump(dic,f,indent=4)


    return dic
    # with open("task10.json","w") as f:
        # json.dump(dic,f,indent=4)
analyse_language_and_directors()
    # pprint.pprint(dic)
# with open("task10.json","w") as f:
    # json.dump(director_by_language,f,indent=4)


# print(director_by_language)