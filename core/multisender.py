from .tx_sender import Sender
from web3 import Web3


def send_one_to_many(chain_rpc, private_key, token=None):
    w3 = Web3(Web3.HTTPProvider(chain_rpc))
    sender = Sender(w3, private_key, token)