import json
import requests
from bs4 import BeautifulSoup
movieurl='https://www.rottentomatoes.com/m/toy_story_4'
# moviename='toy_story_4'
def scrape_top_movie(movieurl):
    request=requests.get(movieurl)
    soup=BeautifulSoup(request.text,'html.parser')
    dic={}
    maindiv=soup.find_all('li',class_='meta-row clearfix')
    moviename=soup.find('h1',class_='scoreboard__title').get_text()
    # print(moviename)

    dic['moviename']=moviename
    dic['movieurl']=movieurl
    for v in maindiv:
        x=v.get_text().strip()
        data=x.split()
        # print(data)
        if data[0]=="Rating:":
            dic['Rating']=data[1]
            # print(dic)
        elif data[0]=="Genre:":
            a=[]
            for i in data:
              if i!="Genre:":
                a.append(i)
            dic["Genre"]=a
            # print(dic)
        elif data[1]=="Language:":
            list=[]
            for i in data:
                list.append(i)
            a=list
            a.remove("Original")
            if a[0]=="Language:":
                a=[a[1]]
            dic["LANGUAGE"]=a
        elif data[0]=='Director:':
            di=[]
            for i in data:
                di.append(i)
            di.remove('Director:')
            i=0
            li=[]
            while i<len(di):
                j=0
                a=''
                while j<2:
                    t=i+j
                    a+=di[t]
                    j=j+1
                li.append(a)
                i=i+2
            dic['Director']=li

        elif data[0]=='Producer:':
            di=[]
            for i in data:
                if i!="Producer:":
                    di.append(i)
            dic["Producer"]=di
        elif data[0]=='Runtime:':
            run=[]
            for i in data:
                if i!="Runtime:":
                    a=i.strip()[:-1]
                    run.append(a)
            a=int(run[0])
            b=a*60
            c=int(run[1])
            sum=b+c
            dic["Runtime"]=sum
    with open('task4.json','w') as f:
        json.dump(dic,f,indent=4)
    
    return dic
scrape_top_movie(movieurl)

