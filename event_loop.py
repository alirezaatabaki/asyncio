import asyncio


async def show(name):
    await asyncio.sleep(3)
    print(f'Hello {name}')


loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(show('ali'))
    # loop.create_task(show('amir'))
    # loop.create_task(show('joe'))
    # loop.create_task(show('jack'))
finally:
    loop.close()
    # loop.stop()
