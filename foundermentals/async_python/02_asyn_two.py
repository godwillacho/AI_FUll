import asyncio


async def brew(name):
    print(f'Brewing {name}....')
    await asyncio.sleep(2)
    print(f'{name} is ready')

async def main():
    await asyncio.gather(
        brew('masala chai'),
        brew('green chai'),
        brew('ginger chai'),
    )

asyncio.run(main())