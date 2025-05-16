from web3 import Web3
from eth_account import Account
from .abi import ERC20_ABI
from utils.logger import logger


class Sender:

    def __init__(self, w3:Web3,  private_key, token=None):
        self.w3 = w3
        self.token = token
        self.account = Account.from_key(private_key)
        self.contract = w3.eth.contract(address=token['ca'], abi=ERC20_ABI) if token else None


    def _get_balance(self):
        balance = self.contract.functions.balanceOf(self.account.address).call() if self.token else self.w3.eth.get_balance(self.account.address)
        return balance / (10 ** self.token['decimal']) if self.token else balance / (10 ** 18)


    def _approve(self, amount):
        tx = self.contract.functions.approve(self.account.address, self.w3.to_wei(amount, 'ether')).buildTransaction({
            'chainId': self.token['chainId'],
            'gasPrice': self.w3.eth.gas_price,
            'nonce': self.w3.eth.get_transaction_count(self.account.address)
        })

        tx['gas'] = self.w3.eth.estimate_gas(tx)

        signed_tx = self.account.sign_transaction(tx)
        tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        logger.info(f'Transaction sent with hash: {tx_hash.hex()}')

        tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
        if tx_receipt.status == 1:
            logger.success('Successfully approved tokens')
        else:
            logger.error(f'Error while approving tokens: {tx_receipt}')


    def _check_allowance(self):
        allowance_amount = self.contract.functions.allowance(self.token['ca'], self.account.address)
        return allowance_amount / (10 ** self.token['decimals']) if self.token else allowance_amount / (10 ** 18)


    def transfer(self, to, amount):
        if self.token:
            pass
        else:
            tx = {
                'to': to,
                'value': self.w3.to_wei(amount),
                'gas': 200000,
                'gasPrice': self.w3.eth.gas_price,
                'nonce': self.w3.eth.get_transaction_count(self.account.address)
            }

            signed_tx = self.account.sign_transaction(tx)
            tx_hash = self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)

            tx_receipt = self.w3.eth.wait_for_transaction_receipt(tx_hash)
            if tx_receipt.status == 1:
                logger.success(f'Successfully sent {amount} ETH to {to}')


