from src.common.request import Request
from bs4 import BeautifulSoup
import logging
import asyncio


if __name__ == "__main__":
    url = 'https://www.cifrus.ru/search.php?search_1=32361'

    logger = logging.getLogger('debug_request')
    r = Request(logger)

    loop = asyncio.get_event_loop()
    status, body = loop.run_until_complete(r.send_get_request(url))
    body = body.decode('utf-8', errors='ignore')

    bs = BeautifulSoup(body, features="html.parser")
    price = bs.body.find('span', attrs={'class': 'price-new'}).text
    print(f'{price=}')
