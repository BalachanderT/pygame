import asyncio
import json
import tda

from selenium import webdriver

# token_path = '/path/to/token.pickle'
# api_key = 'YOUR_API_KEY@AMER.OAUTHAP'
# redirect_uri = 'https://your.redirecturi.com'
# primary_account_id = 1234567890

token_path = '/Users/tkmapz5/Documents/tickers/token.tk'
api_key = 'GPLIN2BIQGFVHYAZGJFUY93IXOCAMBDJ'
redirect_uri = 'http://localhost:8080/'
primary_account_id = 498551465

c = tda.auth.easy_client(api_key, redirect_uri, token_path,
        webdriver_func=lambda: webdriver.Chrome())

client = tda.streaming.StreamClient(c, account_id=primary_account_id)

async def read_stream():
    await client.login()
    await client.quality_of_service(client.QOSLevel.EXPRESS)

    await client.nasdaq_book_subs(['BFRA'])
    client.add_nasdaq_book_handler(
            lambda msg: print(json.dumps(msg, indent=4)))

    while True:
        await client.handle_message()

asyncio.get_event_loop().run_until_complete(read_stream())