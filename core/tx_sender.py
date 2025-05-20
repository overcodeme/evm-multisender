from web3 import Web3
from eth_account import Account
from .abi import ERC20_ABI
from utils.logger import logger


class Sender:

    def __init__(self, w3:Web3,  private_key, token):
        self.w3 = w3
        self.token = token
        self.private_key = private_key
        self.wallet_address = Account.from_key(private_key).address
        self.token = token

        if 'ca' in token:
            self.contract = w3.eth.contract(address=token['ca'], abi=ERC20_ABI)
        else:
            self.contract = w3.eth.contract(address='', abi=ERC20_ABI)


    def get_balance(self):
        balance = self.contract.functions.balanceOf(self.wallet_address).call() if 'ca' in self.token else self.w3.eth.get_balance(self.wallet_address)
        return balance / (10 ** self.token['decimal']) if 'ca' in self.token else balance / (10 ** 18)


    def approve(self, amount):
        if 'ca' in self.token:
            tx = self.contract.functions.approve(self.wallet_address, self.w3.to_wei(amount, 'ether')).buildTransaction({
                'chainId': self.token['chainId'],
                'gasPrice': self.w3.eth.gas_price,
                'nonce': self.w3.eth.get_transaction_count(self.wallet_address)
            })
            tx['gas'] = self.w3.eth.estimate_gas(tx)

            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            logger.info(f'Transaction sent with hash: 0x{tx_hash.hex()}')

            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            if tx_receipt.status == 1:
                logger.success('Successful`ly approved tokens')
            else:
                logger.error(f'Error while approving tokens: {tx_receipt}')


    def check_allowance(self):
        if 'ca' in self.token:
            allowance_amount = self.contract.functions.allowance(self.token['ca'], self.wallet_address)
            return allowance_amount / (10 ** self.token['decimals'])


    def transfer(self, to, amount):
        if 'ca' in self.token:
            tx = self.token.functions.transfer(to, self.w3.to_wei(amount, 'ether')).build_transaction({
            "chainId": self.token['ChainID'],
            "from": self.wallet_address,
            "gasPrice": self.w3.eth.gas_price,
            "nonce": self.w3.eth.get_transaction_count(self.wallet_address),
            "to": self.w3.to_checksum_address(to)
            })
            tx['gas'] = self.w3.eth.estimate_gas(tx)
        else:
            tx = {
                "chainId": self.token['ChainID'],
                "from": self.wallet_address,
                "gas": 21000,
                "gasPrice": self.w3.eth.gas_price,
                "nonce": self.w3.eth.get_transaction_count(self.wallet_address),
                "to": self.w3.to_checksum_address(to),
                "value": self.w3.to_wei(amount, 'ether')
            }

            signed_tx = self.w3.eth.account.sign_transaction(tx, self.private_key)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.raw_transaction)
            logger.info(f'Transaction sent with hash: 0x{tx_hash.hex()}')

            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            if tx_receipt.status == 1:
                logger.success(f'Successfully sent {amount} {self.token['symbol']} to {to}')


