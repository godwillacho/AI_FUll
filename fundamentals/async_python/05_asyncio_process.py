from concurrent.futures import ProcessPoolExecutor 
import asyncio

def encrypt(data):
    return f'encrypted {data[::-1]}'

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, 'credit_card_1234')
        print(f'{result}')
if __name__=="__main__":
    asyncio.run(main())