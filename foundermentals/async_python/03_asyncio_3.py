import asyncio
import aiohttp

async def fetch_url(session,url):
    async with session.get(url) as responce:
        print(f'fetched {url} with status {responce.status}')

async def main():
    urls = ['https://httpbin.org/delay/3'] * 3
    async with  aiohttp.ClientSession() as session:
        tasks = [fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks)


asyncio.run(main())
