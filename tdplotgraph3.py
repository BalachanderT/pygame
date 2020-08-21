import math

import matplotlib.pyplot as plt
import mplfinance as mpf
import numpy as np
import openpyxl
import pandas as pd
import pandas_datareader as web
from matplotlib.backends.backend_pdf import PdfPages
from pandas import DataFrame
import IPython.display as IPydisplay

plt.style.use('fivethirtyeight')

intraday = pd.read_csv('/Users/tkmapz5/Documents/tickers/ticker123.csv',index_col=0,parse_dates=True)
#intraday = intraday.drop('Volume',axis=1)
intraday.index.name = 'Date'
intraday.shape
intraday.head(3)
intraday.tail(3)

iday = intraday.loc['2020-07-21':'2020-08-03',:]

# To display in a new window
#mpf.plot(iday,type='candle',mav=(3,6,9),volume=True,show_nontrading=True)

# To Save to jpg file at the workspace location. Need to update the ticker info in fname and title based on ticker
mpf.plot(iday,type='candle',title='SRNE Price Action',volume=True,savefig=dict(fname='SRNE.jpg',dpi=300,pad_inches=0.25))
