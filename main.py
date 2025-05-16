import asyncio
from utils.file_manager import load_txt, load_json
from utils.menu import menu
from utils.logger import logger
from core.multisender import send_one_to_many


CHAINS = load_json('data/chains.json')

def main():
    chain, token = menu()


if __name__ == '__main__':
    main()