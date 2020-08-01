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

    # here i take a {} bracket for change in div_data and writting a value inside of string for that i user f{}
    div_id = f'hdtab{id_num}'
    links = soup.find('div',id=div_id)
    link = links.find_all('a',attrs={"target" : "_new"})
    
    # here i take a primary_dict for storing data as a key value form.
    primary_dict = {}
    
    # here i take if (link) because of some a_tags are empty and they give empty data that's why i take if(); then its go to inside of loop
    if (link):

        # here i take a loop for finding links and contents of website
        for i in link:
            link_url = (i['href'])
            contents = (i.text)
            primary_dict[contents] = link_url
        # print(json_dict)

    #here i use try except because of i have getting indexerror for handling that i used this.
    try:

        #and here i insert primary data in secondry data as a key value form for looking a better view.

        # and for making key i user headline_list and inserting value i user primary_dict.
        secondry_dict[headline_list[0][Count-Count2].strip()]=primary_dict

        # here i append all data in a list for looking a good view and accesing esaily.....
        data_list.append(secondry_dict)
    except IndexError:
        pass
    Count2-=1

#here i making a file and inserting all data in that file.
File = open('AllData.json','w')
json.dump(data_list,File)
    
    
