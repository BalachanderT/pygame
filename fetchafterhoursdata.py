from afterhours.afterhours import AfterHours

# getting started is fairly quick. Simply specify the ticker symbol of interest 
# and pre or after hours trading when instantiating AfterHours

ticker = 'CNDT'

AH = AfterHours(ticker=ticker, typeof='after')

# there are several price types we can secure. This include highprice and lowprice
AH.getdata(datatype='highprice')


# and low price
AH.getdata(datatype='lowprice')


# we can secure all the trading data for a specific symbol using the following
df = AH.secure_all_pages()

