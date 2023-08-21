from src.common.request import Request
from bs4 import BeautifulSoup
import logging
import asyncio


if __name__ == "__main__":
    url = 'https://biggeek.ru/products/apple-iphone-14-pro-max-256gb-silver'

    logger = logging.getLogger('debug_request')
    r = Request(logger)

    loop = asyncio.get_event_loop()
    status, body = loop.run_until_complete(r.send_get_request(url))
    body = body.decode('utf-8', errors='ignore')

    bs = BeautifulSoup(body, features="html.parser")
    price = bs.body.find('span', attrs={'class': 'total-prod-price'}).text
    print(f'{price=}')
