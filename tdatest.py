
from tda import auth, client
import json
from selenium import webdriver
import math
import time
import json
import pandas as pd
import datetime
import asyncio


from tda.auth import easy_client
from tda.streaming import StreamClient

api_key='GPLIN2BIQGFVHYAZGJFUY93IXOCAMBDJ'
redirect_uri='https://localhost:8080/'
token_path='/Users/tkmapz5/Documents/tickers/token.tk'
client = easy_client(api_key,redirect_uri,token_path)

try:
    session = auth.client_from_token_file(token_path, api_key)
except FileNotFoundError:
    with webdriver.Chrome() as driver:
        session = auth.client_from_login_flow(driver, api_key, redirect_uri, token_path)


# def quote(symbol):
#     quote_response = session.get_price_history(symbol,
#     period_type=client.Client.PriceHistory.PeriodType.DAY,
#     period=client.Client.PriceHistory.Period.TEN_DAYS,
#     frequency_type=client.Client.PriceHistory.FrequencyType.MINUTE,
#     frequency=client.Client.PriceHistory.Frequency.EVERY_MINUTE)
#     assert quote_response.ok, quote_response.raise_for_status()
#     print(json.dumps(quote_response.json(), indent=4))
    
stream_client = StreamClient(client, account_id=498551465)

    

async def read_stream():
    await stream_client.login()
    await stream_client.quality_of_service(StreamClient.QOSLevel.EXPRESS)
    await stream_client.nasdaq_book_subs(['NASDAQ-100'])
    stream_client.add_nasdaq_book_handler(
    lambda msg: print(json.dumps(msg, indent=4)))
    # await stream_client.news_headline_subs(['NASDAQ-ALL'])
    # await stream_client.news_headline_subs(['NASDAQ-60'])
    # stream_client.add_news_headline_handler(
    # lambda msg: print(json.dumps(msg, indent=4)))

    while True:
        print('..')
        await stream_client.handle_message()

StreamClient.news_headline_subs

# if __name__ == '__main__':
#     quote('RLFTF')
