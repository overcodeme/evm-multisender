from colorama import Fore, Style
from datetime import datetime, timezone


class Logger:

    def _log(self, message, color=Fore.WHITE):
        time = f'{datetime.now(timezone.utc).strftime('%d.%m.%Y %H:%M:%S')}'
        print(f'{time} | {color} | {message} {Style.RESET_ALL}')


    def error(self, message):
        self._log(message, Fore.RED)

    def success(self, message):
        self._log (message, Fore.GREEN)

    def info(self, message):
        self._log(message)


logger = Logger()