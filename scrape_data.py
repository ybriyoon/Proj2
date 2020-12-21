from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import csv
import pandas as pd

def scrape():
    information = dict()
    outdoor_dic = dict()
    indoor_dic = dict()
    # link to scrape
    url = "https://www.worldathletics.org/records/by-category/world-records"
    page = requests.get(url)
    soup = bs(page.content, features="lxml")
    tables_out= soup.find("div", {"id": "womenoutdoor"})
    tables_in= soup.find("div", {"id": "womenindoor"})

    # Women outdoor
    headers=[]
    for tr in tables_out.find_all('tr'):    
        for th in tr.find_all('th'):
            new_data = th.text
            new_data = new_data.split()
            headers.append(new_data[0])
    
    disciplines = []
    for td in tables_out.find_all('td', {'data-th':"DISCIPLINE"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        disciplines.append(new_data)
    
    pref = []
    for td in tables_out.find_all('td', {'data-th':"PERF"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ''
        new_data = separator.join(new_data)
        if(new_data != ''):
            pref.append(new_data)

    competitor = []
    for td in tables_out.find_all('td', {'data-th':"COMPETITOR"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        competitor.append(new_data)

    DOB = []
    for td in tables_out.find_all('td', {'data-th':"DOB"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        DOB.append(new_data)

    country = []
    for td in tables_out.find_all('td', {'data-th':"COUNTRY"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        country.append(new_data)

    date = []
    for td in tables_out.find_all('td', {'data-th':"DATE"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        date.append(new_data)
    
    data_df = pd.DataFrame({'Discipline': disciplines,
                        'Perf': pref,
                        'Competitor': competitor,
                        'DOB': DOB,
                        'Country': country,
                        'Date':date
                       })
    for index, row in data_df.iterrows():
        row['Date']= row['Date'][7:11]

    data_df = data_df.sort_values("Date")
    outdoor_dic = data_df.to_dict('split')
    
    # Women indoor
    headers=[]
    for tr in tables_in.find_all('tr'):    
        for th in tr.find_all('th'):
            new_data = th.text
            new_data = new_data.split()
            headers.append(new_data[0])
    
    disciplines = []
    for td in tables_in.find_all('td', {'data-th':"DISCIPLINE"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        disciplines.append(new_data)

    pref = []
    for td in tables_in.find_all('td', {'data-th':"PERF"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ''
        new_data = separator.join(new_data)
        if(new_data != ''):
            pref.append(new_data)

    competitor = []
    for td in tables_in.find_all('td', {'data-th':"COMPETITOR"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        competitor.append(new_data)

    DOB = []
    for td in tables_in.find_all('td', {'data-th':"DOB"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        DOB.append(new_data)

    country = []
    for td in tables_in.find_all('td', {'data-th':"COUNTRY"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        country.append(new_data)

    date = []
    for td in tables_in.find_all('td', {'data-th':"DATE"}):
        new_data = td.text
        new_data = new_data.split()
        separator = ' '
        new_data = separator.join(new_data)
        date.append(new_data)

    data_df = pd.DataFrame({'Discipline': disciplines,
                        'Perf': pref,
                        'Competitor': competitor,
                        'DOB': DOB,
                        'Country': country,
                        'Date':date
                       })
    for index, row in data_df.iterrows():
        row['Date']= row['Date'][7:11]

    data_df = data_df.sort_values("Date")
    indoor_dic = data_df.to_dict('split')

    information.update({"outdoor": outdoor_dic, "indoor": indoor_dic})

    return(information)
