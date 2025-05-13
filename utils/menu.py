from colorama import Fore, Style
from utils.file_manager import load_json
import os


CHAINS = load_json('data/chains.json')

def menu():
    ch, tok = None
    while True:
        os.system('cls')
        print(f'{Fore.BLUE}[1]{Style.RESET_ALL} TESTNET')
        print(f'{Fore.BLUE}[2]{Style.RESET_ALL} MAINNET')
        print(f'{Fore.BLUE}[3]{Style.RESET_ALL} EXIT')

        try:
            opt = int(input('>>> '))
            os.system('cls')
            if opt == 1:
                testnet_menu = [*CHAINS["TESTNET"], 'BACK']

                for idx, chain in enumerate(testnet_menu, start=1):
                    print(f'{Fore.BLUE}[{idx}]{Style.RESET_ALL} {chain}')


            elif opt == 2:
                mainnet_menu = [*CHAINS['MAINNET'], 'BACK']

                for idx, chain in enumerate(mainnet_menu, start=1):
                    print(f'{Fore.BLUE}[{idx}]{Style.RESET_ALL} {chain}')

                tok = int(input(">>> "))
            elif opt == 3:
                break
            else:
                print(f'{Fore.RED}You picked wrong option{Style.RESET_ALL}')

        except Exception as e:
            print('You must input a number')