tickers = sys.argv[1]
print(tickers)
lt = []
for ticker in tickers:
    print(ticker)
    if not ticker:
        ticker_data = robin_stocks.get_stock_quote_by_symbol(ticker)
        ticker_percentage_change = (float(ticker_data['last_extended_hours_trade_price']) - float(ticker_data['last_trade_price'])) / float(ticker_data['last_trade_price']) * 100
        lt.append((ticker, round(ticker_percentage_change,2)))
lt = sorted(lt, key = lambda x: (x[1]), reverse = True)
for i in lt:
    print(i)