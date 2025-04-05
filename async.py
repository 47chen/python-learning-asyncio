import requests
import time
import aiohttp
import asyncio

# def do_request():
#     req = requests.get("https://example.com")
#     print("example.com =>", req.status_code)


# def main():
#     for _ in range(0, 10):
#         do_request()

# if __name__ == '__main__':
#     start_time = time.time()
#     main()
#     end_time = time.time()
#     total_time = end_time - start_time
#     print(f"\nTotal execution time: {total_time:.2f} seconds")



async def do_request(session, url):
    async with session.get(url) as response:
        print(f'{url} => {response.status}')
        return await response.text()

async def main():
    urls = ['https://example.com'] * 10
    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = [do_request(session, url) for url in urls]
        await asyncio.gather(*tasks)

    end_time = time.time()

    total_time = end_time - start_time
    print(f'\nTotal execution timw with asnycio: {total_time:.2f}')


if __name__ == '__main__':
    asyncio.run(main())
    