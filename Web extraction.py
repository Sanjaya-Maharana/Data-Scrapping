import csv
import pandas as pd 
import requests 
from bs4 import BeautifulSoup
import numpy as np
urls=[]
url_id=37
l=[]
headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

dataset = pd.read_csv("input.csv")
y=dataset['URL_ID']
x=dataset['URL']
id=1

for i in x:
    url=i
    if url=='nan':
        break
    page=requests.get(url,headers = headers)
    if (page.status_code==200):
        print('Data Fatch Success')
        soup = BeautifulSoup(page.content,'html.parser')
        pq = soup.findAll(attrs={'class':'td-post-content'})
        a=pq[0].text.replace('\n',' ')
        text = a#.text.replace('\xa0',' ').replace('\n',' ')
        head = soup.find('h1')
        head=head.text.replace('<h1 class="entry-title">',' ').replace('</h1>',' ')
        data=[[url_id,url,head,text]]
        df = pd.DataFrame(data, columns = ['url_Id','url','head','text'])
        print(url_id,url)
        url_id+=1
        
        file = open('output.csv', 'a+', newline ='',encoding='utf-8')
        with file:
            write = csv.writer(file)
            write.writerows(data)
            print("successfully loaded")
        