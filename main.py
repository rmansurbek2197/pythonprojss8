import asyncio
import aiohttp

async def fetch_page(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def main():
    urls = ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
        for html in htmls:
            print(html)

asyncio.run(main())