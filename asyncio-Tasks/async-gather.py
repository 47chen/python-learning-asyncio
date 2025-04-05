import asyncio
import threading
from datetime import datetime


async def do_async_job():
    await asyncio.sleep(2)
    print(datetime.now().isoformat(), 'thread id', threading.current_thread().ident)


async def main():
    await do_async_job()
    print('1')
    await do_async_job()
    print('2')
    await do_async_job()
    print('3')
    


asyncio.run(main())