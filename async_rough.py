

import asyncio


async def third_function():
    print("This is the third function.")
    await asyncio.sleep(1)  # Simulate some asynchronous operation
    print("Back in the third function.")
    print("This is the third function again.")
    print("This is the third function once more.")



async def second_function():
    print("This is the second function.")
    await third_function()
    print("Back in the second function.")
    print("This is the second function again.")
    print("This is the second function once more.")

    



async def first_function():
    print("This is the first function.")
    await second_function()
    print("Back in the first function.")
    print("This is the first function again.")
    print("This is the first function once more.")

asyncio.run(first_function())





