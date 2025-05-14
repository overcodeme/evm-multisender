import asyncio
from utils.file_manager import load_txt, load_json
from utils.menu import menu
from utils.logger import logger


WALLETS = load_txt('data/wallets.txt')
CHAINS = load_json('data/chains.json')

async def main():
    chain, token = menu()


asyncio.run(main())