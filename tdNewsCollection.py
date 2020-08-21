import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
import re
import csv

def write_to_csv(dict_data):
csv_columns = ['date_time', 'head_lines', 'docKey']
csv_file = "news.csv"
try:
with open(csv_file, 'w') as csvfile:
writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
writer.writeheader()
for data in dict_data:
writer.writerow(data)
except IOError:
print("I/O error")


def get_news():
url = "https://research.tdameritrade.com/grid/public/markets/news/morenews.asp?logData=Market%20News%20-%3E%20Search&searchDate=1597723200000#searchNewsBy=date&searchNewsDateRange=1"
url2 = "https://research.tdameritrade.com/grid/public/markets/news/morenews.asp"
querystring = {}

headers = {}
# 'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
# 'x-rapidapi-key': "4d2c98d85dmshdafdc86febf9e5ap18090fjsn1a1d97d3a204"
# }

response = requests.request("GET", url2, headers=headers, params=querystring)
soup = BeautifulSoup(response.text, 'html.parser')
attrs = {
'href': re.compile(r'story.asp.*docKey=1-.*$')
}
news_list = soup.find_all('a', attrs=attrs, string=re.compile(r'^((?!\().)*$'))
dict_data = []
for news in news_list:
dict_data.append({'date_time': news.next_sibling.text, 'head_lines': news.text,
'docKey': news.attrs.get('href')[news.attrs.get('href').index('docKey='):]})

return dict_data


if __name__ == '__main__':
data = get_news()
write_to_csv(data)