from utils.file_manager import load_json, load_txt
from utils.menu import menu
from core.multisender import send_one_to_many
from colorama import Fore, Style
import os


CHAINS = load_json('data/chains.json')
PRIVATE_KEY = load_txt('data/private_key.txt')
WALLETS = load_txt('data/wallets.txt')

def main():
    if not PRIVATE_KEY:
        print(Fore.RED + 'You must input private key in private_key.txt' + Style.RESET_ALL)

    if not WALLETS:
        print(Fore.RED + 'You must input wallets in wallets.txt' + Style.RESET_ALL)

    tom, chain, token = menu()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'Chain: {Fore.CYAN}{chain}{Style.RESET_ALL}')
    print(f'Token: {Fore.CYAN}{token}{Style.RESET_ALL}')

    if CHAINS[tom][chain]['TOKENS'][token]['CONTRACT_ADDRESS']:
        send_one_to_many(chain_rpc=CHAINS[tom][chain]["RPC"], private_key=PRIVATE_KEY[0], token={'ca': CHAINS[tom][chain][token]['CONTRACT_ADDRESS']}, chainID=CHAINS[tom][chain]['ChainID'])
    else:
        send_one_to_many(chain_rpc=CHAINS[tom][chain]["RPC"], private_key=PRIVATE_KEY[0], chainID=CHAINS[tom][chain]['ChainID'])


if __name__ == '__main__':
    main()