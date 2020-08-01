import requests,pprint,json
from bs4 import BeautifulSoup
# url = 'https://www.rediff.com/headline.html'
url = 'http://www.rediff.com/issues/300720hl.html'

# here i getting  data by requests
request=requests.get(url).text

# here i use BeautifulSoup ,BeautifulSoup is a pyton library for pulling out data from html
soup=BeautifulSoup(request,'html.parser')

# here i take a empty list for storing all data in this listt
data_list = []


# here i find all headings of headline....like news movies sports cricket business.........
headline = soup.find('div',attrs={'id':'hdtab1'})
a_tag =headline.find_all('font',class_='f12')

# here a take a empty list for storing all headline heading...
headline_list = []
for i in a_tag:
    title = (i.text.split('|'))
    headline_list.append(title)

#??################ here i apply  loop for getting data from id and a tag and target tag and href.
Count=10
Count2=10
for id_num in range(1,14):
    if id_num==7 or id_num==8:
        continue
    secondry_dict = {}
    div_id = f'hdtab{id_num}'

    links = soup.find('div',id=div_id)
    link = links.find_all('a',attrs={"target" : "_new"})

    primary_dict = {}
    if (link):
        for i in link:
            link_url = (i['href'])
            contents = (i.text)
            primary_dict[contents] = link_url
        # print(json_dict)
    try:
        secondry_dict[headline_list[0][Count-Count2].strip()]=primary_dict
        data_list.append(secondry_dict)
    except IndexError:
        pass
    Count2-=1
File = open('AllData.json','w')
json.dump(data_list,File)
