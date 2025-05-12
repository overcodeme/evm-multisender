from colorama import Fore, Style
from datetime import datetime, timezone


class Logger:

    def _log(self, wallet, message, color=Fore.WHITE):
        time = f'{datetime.now(timezone.utc).strftime('%d.%m.%Y %H:%M:%S')}'
        print(f'{time} | {color} | {wallet} | {message} {Style.RESET_ALL}')


    def error(self, wallet, message):
        self._log(wallet, message, Fore.RED)

    def success(self, wallet, message):
        self._log(wallet, message, Fore.GREEN)

    def info(self, wallet, message):
        self._log(wallet, message)


logger = Logger()