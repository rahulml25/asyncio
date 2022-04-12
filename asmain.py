from typing import Callable, Coroutine, List
import aiohttp
import asyncio
from mtm import note_time


async def http_get(session: aiohttp.ClientSession, url: str) -> Coroutine:
    """Execute an GET http call async """
    async with session.get(url) as response:
        resp = await response.json()
        return resp


async def http_post(session: aiohttp.ClientSession, url: str) -> Coroutine:
    """Execute an POST http call async """
    async with session.post(url) as response:
        resp = await response.json()
        return resp


async def fetch_all(urls: List, inner: Callable):
    """Gather many HTTP call made async """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                inner(
                    session,
                    url
                )
            )
        return await asyncio.gather(*tasks, return_exceptions=True)


def run():
    comments = [f"https://jsonplaceholder.typicode.com/comments/{id_}" for id_ in range(1,500)]
    responses = asyncio.run(fetch_all(comments, http_get))
    # print(responses)


note_time(run)
