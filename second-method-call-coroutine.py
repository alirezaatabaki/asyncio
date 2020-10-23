import asyncio


async def show():
    await asyncio.sleep(2)
    print("HELLO WORLD ...")


# Second method to using asyncio - use another coroutine to call other coroutine
async def main():
    await show()
    await show()


asyncio.run(main())
