import json
import os
import requests
from bs4 import BeautifulSoup
from task1 import moviedata
from task4 import scrape_top_movie
movie=moviedata()
# print(movie)
def get_movie_list_details():
    movie_list=[]
    
    for i in movie[:70]:
        movies=scrape_top_movie(i["movieurl"])
        movie_list.append(movies)
        
    with open("task5.json","w+") as file:
        json.dump(movie_list,file,indent=4)
    return movie_list  
get_movie_list_details()







# import json
# import requests
# from bs4 import BeautifulSoup
# from task1 import moviedata
# from task4 import scrape_movie_details
# movie = moviedata()
# print(movie)
# def get_movie_list_details():
#     movie_list = []
#     count=0
#     for i in movie[:100]:
#         print(i)
#     #     a=scrape_top_movie(i["moviceurl"])
#     #     movie_list.append(a)
#     # print(movie_list)
#     #     count+=1
#     # with open("task5.json","w+") as file5:
#     #     json.dump(movie_list,file5,indent=4)
# get_movie_list_details()

    

    





          

