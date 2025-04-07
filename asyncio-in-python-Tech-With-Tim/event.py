import asyncio


async def waiter(event):

    print("waiting for the event to be set")
    await event.wait()
    print("event has been set, continuing execution!")

async def setter(event):
    await asyncio.sleep(2) # Simulate doing some work
    event.set()
    await asyncio.sleep(5) 
    print('after waiting 5 second!')
    print("event has been set!")


async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))

asyncio.run(main())