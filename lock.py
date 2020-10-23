import asyncio

num = 0


async def add(lock):
    await lock.acquire()  # You can also use "with" context manager
    try:
        global num
        num += 1000
    finally:
        lock.release()


async def sub(lock):
    await lock.acquire()
    try:
        global num
        num -= 1000
    finally:
        lock.release()


async def main():
    lock = asyncio.Lock()
    await asyncio.gather(add(lock), sub(lock))


print(num)
