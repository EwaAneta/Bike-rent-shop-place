import requests
import pandas as pd
import json


#set width of the terminal window to 1000
pd.options.display.width = 1000
# set amount of displayed df columns to 8
pd.set_option('display.max_columns', 8)

# defining URLs to download data from GUS BDL - limit of 100 lines per page (380 lines needed)
url_population_0 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/745231?format=json&year=2020&unit-level=5&page-size=100&page=0'
url_population_1 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/745231?format=json&year=2020&unit-level=5&page-size=100&page=1'
url_population_2 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/745231?format=json&year=2020&unit-level=5&page-size=100&page=2'
url_population_3 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/745231?format=json&year=2020&unit-level=5&page-size=100&page=3'

url_average_income_0 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/64429?format=json&year=2020&unit-level=5&page-size=100&page=0'
url_average_income_1 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/64429?format=json&year=2020&unit-level=5&page-size=100&page=1'
url_average_income_2 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/64429?format=json&year=2020&unit-level=5&page-size=100&page=2'
url_average_income_3 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/64429?format=json&year=2020&unit-level=5&page-size=100&page=3'

url_tourism_0 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/399257?format=json&year=2020&unit-level=5&page-size=100&page=0'
url_tourism_1 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/399257?format=json&year=2020&unit-level=5&page-size=100&page=1'
url_tourism_2 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/399257?format=json&year=2020&unit-level=5&page-size=100&page=2'
url_tourism_3 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/399257?format=json&year=2020&unit-level=5&page-size=100&page=3'

url_sport_0 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/59628?format=json&year=2020&unit-level=5&page-size=100&page=0'
url_sport_1 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/59628?format=json&year=2020&unit-level=5&page-size=100&page=1'
url_sport_2 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/59628?format=json&year=2020&unit-level=5&page-size=100&page=2'
url_sport_3 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/59628?format=json&year=2020&unit-level=5&page-size=100&page=3'

url_lane_len_0 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/288080?format=json&year=2020&unit-level=5&page-size=100&page=0'
url_lane_len_1 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/288080?format=json&year=2020&unit-level=5&page-size=100&page=1'
url_lane_len_2 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/288080?format=json&year=2020&unit-level=5&page-size=100&page=2'
url_lane_len_3 = 'https://bdl.stat.gov.pl/api/v1/data/by-variable/288080?format=json&year=2020&unit-level=5&page-size=100&page=3'

# defining the headers to be passed as the 'headers' parameter of the requests.get () function

api_key = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
#headers = {
#    'X-ClientId': api_key
#}
headers = {}

# in order to use the GUS BDL with an API key, you should:
# 1) remove / comment 'heading = {}'
# 2) assign your own API key to the variable 'api_key'
# 3) remove comment from 'headers'X-ClientId': api_key} '

# obtaining JSON responses from GUS BDL
population_0 = requests.get(url_population_0, headers=headers)
population_1 = requests.get(url_population_1, headers=headers)
population_2 = requests.get(url_population_2, headers=headers)
population_3 = requests.get(url_population_3, headers=headers)

average_income_0 = requests.get(url_average_income_0, headers=headers)
average_income_1 = requests.get(url_average_income_1, headers=headers)
average_income_2 = requests.get(url_average_income_2, headers=headers)
average_income_3 = requests.get(url_average_income_3, headers=headers)

tourism_0 = requests.get(url_tourism_0, headers=headers)
tourism_1 = requests.get(url_tourism_1, headers=headers)
tourism_2 = requests.get(url_tourism_2, headers=headers)
tourism_3 = requests.get(url_tourism_3, headers=headers)

sport_0 = requests.get(url_sport_0, headers=headers)
sport_1 = requests.get(url_sport_1, headers=headers)
sport_2 = requests.get(url_sport_2, headers=headers)
sport_3 = requests.get(url_sport_3, headers=headers)

lane_len_0 = requests.get(url_lane_len_0, headers=headers)
lane_len_1 = requests.get(url_lane_len_1, headers=headers)
lane_len_2 = requests.get(url_lane_len_2, headers=headers)
lane_len_3 = requests.get(url_lane_len_3, headers=headers)

# extracting 'results' dictionary list from dictionary JSON representation
population_data_0 = population_0.json()['results']
population_data_1 = population_1.json()['results']
population_data_2 = population_2.json()['results']
population_data_3 = population_3.json()['results']

average_income_data_0 = average_income_0.json()['results']
average_income_data_1 = average_income_1.json()['results']
average_income_data_2 = average_income_2.json()['results']
average_income_data_3 = average_income_3.json()['results']

tourism_data_0 = tourism_0.json()['results']
tourism_data_1 = tourism_1.json()['results']
tourism_data_2 = tourism_2.json()['results']
tourism_data_3 = tourism_3.json()['results']

sport_data_0 = sport_0.json()['results']
sport_data_1 = sport_1.json()['results']
sport_data_2 = sport_2.json()['results']
sport_data_3 = sport_3.json()['results']

lane_len_data_0 = lane_len_0.json()['results']
lane_len_data_1 = lane_len_1.json()['results']
lane_len_data_2 = lane_len_2.json()['results']
lane_len_data_3 = lane_len_3.json()['results']

def gus_var_dict(data):
    """
    Converts the list of dictionaries 'results' and returns a dictionary with the keys of the names of counties.

     Args:
         (list of dict) data - list of dictionaries extracted from 'results' of the dictionary JSON representation downloaded from GUS BDL
     Returns:
         (dict) new dict - a dictionary, the keys of which are the names of poviats ('name'), and the values of the 'val' value of the GUS feature for one year
    """
    # create a dictionary to be returned by the function
    new_dict = dict()
    # iterating of keys in dictionaries from the list, transforming the value 'name' into a dictionary key, removing the key-value pair 'id' from the dictionary
    for k in data:
        new_dict[k.pop('name')] = k
        k.pop('id')
    # iteration of the created dictionary by new keys (names of poviats) and
    # overwriting key values with key values 'val' from a one-element list which is the value of the dictionary 'values'
    for k in new_dict.keys():
        new_dict[k] = new_dict[k]['values'][0]['val']


    return new_dict

# calling gus_var_dict function
population_dict_0 = gus_var_dict(population_data_0)
population_dict_1 = gus_var_dict(population_data_1)
population_dict_2 = gus_var_dict(population_data_2)
population_dict_3 = gus_var_dict(population_data_3)

average_income_dict_0 = gus_var_dict(average_income_data_0)
average_income_dict_1 = gus_var_dict(average_income_data_1)
average_income_dict_2 = gus_var_dict(average_income_data_2)
average_income_dict_3 = gus_var_dict(average_income_data_3)

tourism_dict_0 = gus_var_dict(tourism_data_0)
tourism_dict_1 = gus_var_dict(tourism_data_1)
tourism_dict_2 = gus_var_dict(tourism_data_2)
tourism_dict_3 = gus_var_dict(tourism_data_3)

sport_dict_0 = gus_var_dict(sport_data_0)
sport_dict_1 = gus_var_dict(sport_data_1)
sport_dict_2 = gus_var_dict(sport_data_2)
sport_dict_3 = gus_var_dict(sport_data_3)

lane_len_dict_0 = gus_var_dict(lane_len_data_0)
lane_len_dict_1 = gus_var_dict(lane_len_data_1)
lane_len_dict_2 = gus_var_dict(lane_len_data_2)
lane_len_dict_3 = gus_var_dict(lane_len_data_3)

# creating a DataFrames to hold pointers and defining the first column name for the first pointer at the same time
df0 = pd.DataFrame.from_dict(population_dict_0, columns = ['Ludność ogółem'], orient = 'index')
df1 = pd.DataFrame.from_dict(population_dict_1, columns = ['Ludność ogółem'], orient = 'index')
df2 = pd.DataFrame.from_dict(population_dict_2, columns = ['Ludność ogółem'], orient = 'index')
df3 = pd.DataFrame.from_dict(population_dict_3, columns = ['Ludność ogółem'], orient = 'index')

# adding dictionaries with succeeding pointers as DataFrames columns
df0['Przeciętne miesięczne wynagrodzenia brutto'] = pd.Series(average_income_dict_0)
df1['Przeciętne miesięczne wynagrodzenia brutto'] = pd.Series(average_income_dict_1)
df2['Przeciętne miesięczne wynagrodzenia brutto'] = pd.Series(average_income_dict_2)
df3['Przeciętne miesięczne wynagrodzenia brutto'] = pd.Series(average_income_dict_3)

df0['Stopień wykorzystania miejsc noclegowych ogółem'] = pd.Series(tourism_dict_0)
df1['Stopień wykorzystania miejsc noclegowych ogółem'] = pd.Series(tourism_dict_1)
df2['Stopień wykorzystania miejsc noclegowych ogółem'] = pd.Series(tourism_dict_2)
df3['Stopień wykorzystania miejsc noclegowych ogółem'] = pd.Series(tourism_dict_3)

df0['Kluby sportowe - ćwiczący ogółem'] = pd.Series(sport_dict_0)
df1['Kluby sportowe - ćwiczący ogółem'] = pd.Series(sport_dict_1)
df2['Kluby sportowe - ćwiczący ogółem'] = pd.Series(sport_dict_2)
df3['Kluby sportowe - ćwiczący ogółem'] = pd.Series(sport_dict_3)

df0['Długość ścieżek rowerowych'] = pd.Series(lane_len_dict_0)
df1['Długość ścieżek rowerowych'] = pd.Series(lane_len_dict_1)
df2['Długość ścieżek rowerowych'] = pd.Series(lane_len_dict_2)
df3['Długość ścieżek rowerowych'] = pd.Series(lane_len_dict_3)

# merging the 4 resulting partial DataFrames into one DataFrame
df = pd.concat([df0, df1, df2, df3])

# calculation of the attractiveness index of poviats for the bike rental locations
df['Indeks atrakcyjności powiatu dla wypożyczalni'] = df['Ludność ogółem'] * df['Przeciętne miesięczne wynagrodzenia brutto'] * df['Stopień wykorzystania miejsc noclegowych ogółem'] * df['Długość ścieżek rowerowych']

# calculation of the attractiveness index of poviats for the location of bicycle shops
df['Indeks atrakcyjności powiatu dla salonu'] = df['Ludność ogółem'] * df['Przeciętne miesięczne wynagrodzenia brutto'] * df['Kluby sportowe - ćwiczący ogółem'] * df['Długość ścieżek rowerowych']

# data normalization on a scale of 0 to 100
df_norm = 100 * (df - df.min()) / (df.max() - df.min())

# presentation of the DataFrame with indexes of the attractiveness of poviats for the location of bike shops
print('\nDane z obliczonymi indeksami atrakcyjności powiatów, posortowane wg indeksu atrakcyjności powiatu dla lokalizacji salonu: \n')
print(df_norm.sort_values(by = 'Indeks atrakcyjności powiatu dla salonu', ascending = False))

# presentation of the DataFrame with indexes of the attractiveness of poviats for the location of bike rental
print('\nDane z obliczonymi indeksami atrakcyjności powiatów, posortowane wg indeksu atrakcyjności powiatu dla lokalizacji wypożyczalni: \n')
print(df_norm.sort_values(by = 'Indeks atrakcyjności powiatu dla wypożyczalni', ascending = False))

# save the DataFrame to the file 'Indeksy_atrakcyjności_lokalizacji.csv' with encoding of Polish characters
df_norm.to_csv('Indeksy_atrakcyjności_lokalizacji.csv', encoding='utf-8-sig')
