#pip install aiohttp[speedups]

import aiohttp
import asyncio

async def get_site(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text()
            print(f'Leu {len(html)} caracteres de {url}')

async def main():
    await asyncio.gather(
        get_site('https://example.com'),
        get_site('https://python.org')
    )

asyncio.run(main())