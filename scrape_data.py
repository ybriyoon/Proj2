from splinter import Browser
from bs4 import BeautifulSoup
import requests
import csv


# link to scrape
url = "https://www.worldathletics.org/records/by-category/world-records"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")


# write to new csv
filename = 'test.csv'
csv_writer = csv.writer(open(filename, 'w', encoding='utf-8'))



# scraping the table 
tables_out= soup.find("div", {"id": "womenoutdoor"})
tables_in= soup.find("div", {"id": "womenindoor"})


for tr in tables_out.find_all('tr'):
    data=[]
    
    for th in tr.find_all('th'):
        data.append(th.text)
    
        if(data):
            print("headers: {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue


    for td in tables_out.find_all('td', {'data-th':"DISCIPLINE"}):  
        data.append(td.text)
    
        if(data):
            print("DISCIPLINE {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue
    
    for td in tables_out.find_all('td', {'data-th':"PERF"}):
        data.append(td.text)
    
        if(data):
            print("PERF: {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue

    for td in tables_out.find_all('td', {'data-th':"WIND"}):
        data.append(td.text)
    
        if(data):
            print("WIND: {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue

    for td in tables_out.find_all('td', {'data-th':"COMPETITOR"}):
        data.append(td.text)
    
        if(data):
            print("COMPETITOR: {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue

    for td in tables_out.find_all('td', {'data-th':"DOB"}):
        data.append(td.text)
    
        if(data):
            print("DOB: {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue
  
    for td in tables_out.find_all('td', {'data-th':"COUNTRY"}):
        data.append(td.text)
    
        if(data):
            print("COUNTRY: {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue

    for td in tables_out.find_all('td', {'data-th':"VENUE"}):
        data.append(td.text)
    
        if(data):
            print("VENUE: {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue

    
    for td in tables_out.find_all('td', {'data-th':"DATE"}):
        data.append(td.text)
    
        if(data):
            print("DATE: {}".format(','.join(data)))
            csv_writer.writerow(data)
            continue
