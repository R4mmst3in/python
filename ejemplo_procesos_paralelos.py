# https://docs.python.org/3/library/asyncio-task.html
import asyncio
import time


async def say_after (delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"Started at {time.strftime('%X')}")

    t1 = say_after(1, 'Hello')
    t2 = say_after(2, 'World')

    await asyncio.gather(t1, t2)

    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())