import pandas as pd
def get_data():
    file_path = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-08/women.csv"
    women2020 = pd.read_csv(file_path)
    women2020.country[50] = 'UK'
    women2020.country[72] = "India"
    women2020.to_csv('data/women2020.csv', index = False)
    lat_long_file = 'data/lat_lon.csv'
    lat_long = pd.read_csv(lat_long_file)
    Final_data = pd.merge(women2020, lat_long, on='country', how='left')
    Final_data = Final_data.drop_duplicates(subset=['name'])
    Final_data.to_csv('data/complete_data.csv',index = False)
    print("Data created in a CSV file!")

