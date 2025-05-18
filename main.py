from utils.file_manager import load_json, load_txt
from utils.menu import menu
from core.multisender import send_one_to_many
from colorama import Fore, Style


CHAINS = load_json('data/chains.json')
PRIVATE_KEY = load_txt('data/private_key.txt')
WALLETS = load_txt('data/wallets.txt')

def main():
    if not PRIVATE_KEY:
        print(Fore.RED + 'You must input private key in private_key.txt' + Style.RESET_ALL)

    if not WALLETS:
        print(Fore.RED + 'You must input wallets in wallets.txt' + Style.RESET_ALL)

    chain, token = menu()
    print(f'Chain: {Fore.CYAN}{chain}{Style.RESET_ALL}')
    print(f'Token: {Fore.CYAN}{token}{Style.RESET_ALL}')

    if CHAINS[token]['CONTRACT_ADDRESS']:
        send_one_to_many(chain_rpc=CHAINS[chain]["RPC"], private_key=PRIVATE_KEY, token={'symbol': token, 'ca': CHAINS[chain][token]['CONTRACT_ADDRESS'], 'chainID': CHAINS[chain][token]['ChainID']})
    else:
        send_one_to_many(chain_rpc=CHAINS[chain]["RPC"], private_key=PRIVATE_KEY)


if __name__ == '__main__':
    main()