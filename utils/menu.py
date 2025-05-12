from colorama import Fore, Style


def menu():
    while True:
        print(f'{Fore.BLUE}[1]{Style.RESET_ALL} TESTNET')
        print(f'{Fore.BLUE}[2]{Style.RESET_ALL} MAINNET')

        try:
            opt = int(input('>>> '))

            if opt == 1:
                print('You chose TESTNET')
            elif opt == 2:
                print('You chose MAINNET')
            else:
                print('Wrong option')
        except Exception as e:
            print('You must input a number')