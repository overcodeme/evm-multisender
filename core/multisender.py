from .tx_sender import Sender
from web3 import Web3
from utils.logger import logger
from utils.file_manager import load_txt
from colorama import Fore, Style


WALLETS = load_txt('data/wallets.txt')

def send_one_to_many(chain_rpc, private_key, token=None):
    w3 = Web3(Web3.HTTPProvider(chain_rpc))
    sender = Sender(w3, private_key, token)

    try:
        print(f'Balance: {Fore.CYAN}{sender.get_balance()}{Style.RESET_ALL}')
        amount = float(input('Input amount to send on each wallet: '))
        summary = amount * len(WALLETS)

        if token:
            allowance_amount = sender.check_allowance()

            if allowance_amount < summary:
                sender.approve(summary)

        for i, w in enumerate(WALLETS, start=1):
            logger.info(f'Progress: {i}/{len(WALLETS)}')
            sender.transfer(w, amount)

    except Exception as e:
        logger.error(f'An exception occurred: {e}')