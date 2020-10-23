"""
    coroutine is a function that can suspend its execution before reaching return.
"""
import asyncio


async def show():
    await asyncio.sleep(3)
    print("HELLO WORLD...")


asyncio.run(show())  # First method to use asyncio - call coroutine by run method
