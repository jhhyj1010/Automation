#!/usr/bin/env python3

import asyncio
from asyncio import streams

# Async method
async def async_hello(future, input: str):
    print('async hello', input)
    await asyncio.sleep(1)
    future.set_result('Hello World')

# Async method 1
async def async_hello_1(input: str) -> list:
    print('async hello', input)
    await asyncio.sleep(1)
    return [1,2,3]

# Sync method
def hello():
    ft = asyncio.Future()
    asyncio.ensure_future(async_hello(ft, 'jesson'))
    # 重点就是这里，返回一个Future
    return ft


async def run():
    print('Run ...')
    r = await hello()
    print(r)


#loop = asyncio.get_event_loop()
#loop.run_until_complete(run())
#loop.close()

def main():
    loop = asyncio.get_event_loop()
    async def create_tasks():
        tasks = [asyncio.create_task(async_hello_1('jesson')) for i in range(10)] #List comprehension, i can be used in the function or not.
        await asyncio.wait(tasks)
    loop.run_until_complete(create_tasks())

main()