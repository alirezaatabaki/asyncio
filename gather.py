import asyncio


async def show(name):
    await asyncio.sleep(3)
    print(f"hello {name}")


async def main():
    await asyncio.gather(
        show('joe'),
        show('jack'),
        show('joe')
    )


asyncio.run(main())
