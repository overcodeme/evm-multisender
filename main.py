import asyncio
from utils.file_manager import load_txt
from utils.menu import menu


WALLETS = load_txt('data/wallets.txt')

async def main():
    menu()


asyncio.run(main())