import requests
from bs4 import BeautifulSoup

url = "https://www.marketwatch.com/investing/stock/aapl?mod=search_symbol"
page = requests.get(url)

soup = BeautifulSoup(page.text, "lxml")

company = soup.find('h1', class_='company__name').text
# print(company)

current_Price = "$"+soup.find('bg-quote', class_='value').text
# print("Current Price:", current_Price)

last_Price = soup.find("td", class_='table__cell u-semi').text
# print("Closing Price:", last_Price)

nested_html = soup.find_all('mw-rangebar', class_='element element--range range--yearly')[0]
# print(nested_html)

lower_range = nested_html.find_all('span', class_='primary')[0].text
higher_range = nested_html.find_all('span', class_='primary')[1].text
week_range = nested_html.find('span', class_='secondary').text

analyst = soup.find('li', class_='analyst__option active').text
range_of_weeks = lower_range+"-"+"-"+higher_range
# print(company, current_Price, last_Price, range_of_weeks, analyst, sep = '\n')


import pandas as pd
df = pd.DataFrame({'Company':[company], 
                 'Current_Price':[current_Price],
                 'Closing_Price':[last_Price],
                 '52_Week_Range':[range_of_weeks]})
print(df)


