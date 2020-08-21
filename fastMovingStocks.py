# imports
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd


# list all stocks
#intraday = pd.read_csv('/Users/tkmapz5/Documents/tickers/nasdaqlisted2.csv',index_col=0,parse_dates=True)
#url = “Users/tkmapz5/Documents/tickers/nasdaqlisted.txt"
intraday=pd.read_csv('nasdaqlisted.txt')

print(intraday.head())
print(intraday['Symbol'].head())
print(len(intraday['Symbol']))

def lookup_fn(intraday, key_row, key_col):
 try:
    return intraday.iloc[key_row][key_col]
 except IndexError:
    return 0

movementlist = []
for stock in intraday['Symbol']:
  # get today's data or history based on chaging the values below
  thestock = yf.Ticker(stock)
  hist = thestock.history(period="5d",interval="15m")
  # print(stock)
  low = float(10000)
  high = float(0)
  # print(thestock.info)
  for day in hist.itertuples(index=True, name='Pandas'):
    if day.Low < low:
      low = day.Low
    if high < day.High:
      high = day.High
  
  deltapercent = 100 * (high - low)/low
  Open = lookup_fn(hist, 0, "Open")
  # some error handling: 
  if len(hist >=5):
    Close = lookup_fn(hist, 4, "Close")
  else :
    Close = Open
  if(Open == 0):
    deltaprice = 0
  else:
    deltaprice = 100 * (Close - Open) / Open
    print(stock+" "+str(deltapercent)+ " "+ str(deltaprice))
  pair = [stock, deltapercent, deltaprice]
  movementlist.append(pair)

  for entry in movementlist:
    if entry[1]>float(100):
         print(entry)