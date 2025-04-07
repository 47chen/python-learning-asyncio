import asyncio
import random

semaphore = asyncio.Semaphore(3)

async def crawl(url):
    async with semaphore:
        await asyncio.sleep(random.uniform(0.5, 2))
        print(f'Crawled {url}...')
    
async def main():
    urls = urls = [f"http://site.com/page{i}" for i in range(10)]

    await asyncio.gather(*(crawl(url) for url in urls))

asyncio.run(main())