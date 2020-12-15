from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import csv

def scrape():
    information = dict()
    outdoor_dic = dict()
    indoor_dic = dict()
    # link to scrape
    url = "https://www.worldathletics.org/records/by-category/world-records"
    page = requests.get(url)
    soup = bs(page.content)
    tables_out= soup.find("div", {"id": "womenoutdoor"})
    tables_in= soup.find("div", {"id": "womenindoor"})

    # Women outdoor
    headers=[]
    for tr in tables_out.find_all('tr'):    
        for th in tr.find_all('th'):
            new_data = th.text
            new_data = new_data.split()
            headers.append(new_data[0])
    
    outdoor_dic.update({'headers':headers})

    disciplines = []
    for td in tables_out.find_all('td', {'data-th':"DISCIPLINE"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        disciplines.append(new_data)
    outdoor_dic.update({'disciplines':disciplines})

    pref = []
    for td in tables_out.find_all('td', {'data-th':"PERF"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ''
        new_data = separator.join(new_data)
        if(new_data != ''):
            pref.append(new_data)
    outdoor_dic.update({'pref':pref})

    competitor = []
    for td in tables_out.find_all('td', {'data-th':"COMPETITOR"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        competitor.append(new_data)
    outdoor_dic.update({'competitor':competitor})

    DOB = []
    for td in tables_out.find_all('td', {'data-th':"DOB"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        DOB.append(new_data)
    outdoor_dic.update({'DOB':DOB})

    country = []
    for td in tables_out.find_all('td', {'data-th':"COUNTRY"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        country.append(new_data)
    outdoor_dic.update({'country':country})

    date = []
    for td in tables_out.find_all('td', {'data-th':"DATE"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        date.append(new_data)
    outdoor_dic.update({'date':date})

    # Women indoor
    headers=[]
    for tr in tables_in.find_all('tr'):    
        for th in tr.find_all('th'):
            new_data = th.text
            new_data = new_data.split()
            headers.append(new_data[0])
    
    indoor_dic.update({'headers':headers})

    disciplines = []
    for td in tables_in.find_all('td', {'data-th':"DISCIPLINE"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        disciplines.append(new_data)
    indoor_dic.update({'disciplines':disciplines})

    pref = []
    for td in tables_in.find_all('td', {'data-th':"PERF"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ''
        new_data = separator.join(new_data)
        if(new_data != ''):
            pref.append(new_data)
    indoor_dic.update({'pref':pref})

    competitor = []
    for td in tables_in.find_all('td', {'data-th':"COMPETITOR"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        competitor.append(new_data)
    indoor_dic.update({'competitor':competitor})

    DOB = []
    for td in tables_in.find_all('td', {'data-th':"DOB"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        DOB.append(new_data)
    indoor_dic.update({'DOB':DOB})

    country = []
    for td in tables_in.find_all('td', {'data-th':"COUNTRY"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        country.append(new_data)
    indoor_dic.update({'country':country})

    date = []
    for td in tables_in.find_all('td', {'data-th':"DATE"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        date.append(new_data)
    indoor_dic.update({'date':date})

    information.update({"outdoor": outdoor_dic, "indoor": indoor_dic})

    return(information)


scrape()
print("done!")
