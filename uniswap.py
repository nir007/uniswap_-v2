import http.client
from aiohttp import ClientSession
from exceptions import *
from w3_client import W3Client
from loguru import logger

class UniswapClient:
    def __init__(
            self,
            *,
            w3: W3Client,
            session: ClientSession,
    ):
        self.__w3 = w3
        self.__session = session

    async def __send_request(self, *, url: str, method: str = "GET", data: dict = None):
        logger.info(f"Sent request to {method}: {url}")

        async with self.__session.request(
                method=method,
                url=url,
                json=data if method != "GET" else None,
                params=data if method == "GET" else None,
                timeout=15,
                allow_redirects=False,
                headers={
                    "Content-Type": "application/json"
                }
        ) as res:
            content = await res.json(content_type=res.headers["Content-Type"])

            if res.status not in (http.client.OK, http.client.CREATED, http.client.NO_CONTENT):
                raise RuntimeError(f"Bad response code from {url}: {res.status} {content}")

            return content