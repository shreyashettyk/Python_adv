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
    # await asyncio.gather(async_sleep(10),async_sleep(2),print_hello())
    # await asyncio.gather(asyncio.wait_for(async_sleep(15),5),async_sleep(2),print_hello())
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(15),5),async_sleep(2),print_hello())
    except asyncio.TimeoutError as e:
        print('Timeout Exception handled')
    print("total time taken ",time.time()-start_time)


if __name__ =="__main__":
    asyncio.run(main())