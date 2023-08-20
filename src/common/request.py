import logging
from aiohttp import ClientSession
from typing import Tuple, Union


class Request:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    async def send_get_request(self, url: str, resp_in_json: bool = False) -> Tuple[int, Union[dict, str]]:
        return await self.__send_request(url, 'GET', resp_in_json)

    async def send_post_request(self, url: str, resp_in_json: bool = False) -> Tuple[int, Union[dict, str]]:
        return await self.__send_request(url, 'POST', resp_in_json)

    async def __send_request(self, url, method='GET', resp_in_json: bool = False) -> Tuple[int, Union[dict, str]]:
        async with ClientSession() as session:
            if method == 'GET':
                function = session.get
            else:
                function = session.post
            request = await function(url)
            status = request.status
            self.logger.info(f'Response status for url {url} -> {status}')
            if resp_in_json:
                body = await request.json()
            else:
                body = await request.read()
            self.logger.debug(f'Response body for url {url} -> {body}')
            return status, body
