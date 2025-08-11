import asyncio
import time



async def async_sleep(duration):
    print("Before")
    print(f"Sleeping for {duration} s")
    await(asyncio.sleep(duration))
    print(f"After sleep for {duration} s")

async def print_hello():
    print("Hello world")


async def main():
    start_time = time.time()
    task = asyncio.create_task(async_sleep(1))
    await async_sleep(10)
    await print_hello()
    await task
    
    print("total time taken ",time.time()-start_time)


if __name__ =="__main__":
    asyncio.run(main())