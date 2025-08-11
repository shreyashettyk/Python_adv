#there is no parallelism in this code all the corountines run one after another


import asyncio



async def async_sleep():
    print("Before")
    print("Slpeeong for 5 s")
    await(asyncio.sleep(5))
    print("After")

async def print_hello():
    print("Hello world")


async def main():
    await async_sleep()
    await print_hello()


if __name__ =="__main__":
    asyncio.run(main())