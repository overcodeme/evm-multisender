from colorama import Fore, Style
from utils.file_manager import load_json
import os


CHAINS = load_json('data/chains.json')

def menu():
    chain, token = None, None
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{Fore.BLUE}[1]{Style.RESET_ALL} TESTNET')
        print(f'{Fore.BLUE}[2]{Style.RESET_ALL} MAINNET')
        print(f'{Fore.BLUE}[3]{Style.RESET_ALL} EXIT')

        try:
            opt = int(input('>>> '))
            if opt == 1:
                while True:
                    testnet_menu = [*CHAINS["TESTNET"], 'BACK']

                    os.system('cls' if os.name == 'nt' else 'clear')
                    for idx, ch in enumerate(testnet_menu, start=1):
                        print(f'{Fore.BLUE}[{idx}]{Style.RESET_ALL} {ch}')

                    ch = int(input(">>> "))

                    if ch == len(testnet_menu):
                        break
                    chain = testnet_menu[ch-1]

                    while True:
                        tokens_menu = [*CHAINS['TESTNET'][chain]['TOKENS'], 'BACK']
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for idx, tok in enumerate(tokens_menu, start=1):
                            print(f'{Fore.BLUE}[{idx}]{Style.RESET_ALL} {tok}')

                        tok = int(input(">>> "))

                        if tok == len(tokens_menu):
                            break

                        token = mainnet_menu[tok-1]

                        return [chain, token]

            elif opt == 2:
                while True:
                    mainnet_menu = [*CHAINS['MAINNET'], 'BACK']
                    os.system('cls' if os.name == 'nt' else 'clear')
                    for idx, ch in enumerate(mainnet_menu, start=1):
                        print(f'{Fore.BLUE}[{idx}]{Style.RESET_ALL} {ch}')

                    ch = int(input(">>> "))
                    chain = mainnet_menu[ch-1]

                    while True:
                        tokens_menu = [*CHAINS['MAINNET'][chain]['TOKENS'], 'BACK']
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for idx, tok in enumerate(tokens_menu, start=1):
                            print(f'{Fore.BLUE}[{idx}]{Style.RESET_ALL} {tok}')

                        tok = int(input(">>> "))

                        if tok == len(tokens_menu):
                            break

                        token = mainnet_menu[tok-1]

                        return [chain, token]

            elif opt == 3:
                break
            else:
                print(f'{Fore.RED}You picked wrong option{Style.RESET_ALL}')

        except ValueError:
            print('You must input a number')

        except Exception as e:
            print(f'An error occurred: {e}')