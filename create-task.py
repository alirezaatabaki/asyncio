import asyncio


async def show():
    await asyncio.sleep(2)
    print("HELLO WORLD ...")
    print(asyncio.current_task())
    print(asyncio.all_tasks())  # resturn all task


# Using this method to make your program concurrent
async def main():
    t1 = asyncio.create_task(show())
    t2 = asyncio.create_task(show())

    await t1
    await t2


asyncio.run(main())
