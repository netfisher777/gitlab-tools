import sys
import time
from multiprocessing import Process


class LoadingBar:
    BACKSPACE_CODE = '\x08'
    CLEAR_LINE_CODE = '\033[2K\033[1G'

    def __init__(self, label: str, symbol: str, number_of_symbols: int, timeout: float):
        self.__label = label
        self.__symbol = symbol
        self.__number_of_symbols = number_of_symbols
        self.__timeout = timeout
        self.__running = False
        self.__loading_task: Process = None

    def __show_loading(self):
        label = self.__label
        symbol = self.__symbol
        number_of_symbols = self.__number_of_symbols
        timeout = self.__timeout
        if label:
            sys.stdout.write(label)
            sys.stdout.flush()
        clear_symbols = False
        while self.__running:
            for tick in range(number_of_symbols):
                if not clear_symbols:
                    sys.stdout.write(symbol)
                    sys.stdout.flush()
                    time.sleep(timeout)
                else:
                    sys.stdout.write(f'{LoadingBar.BACKSPACE_CODE}')
                    sys.stdout.write(' ')
                    sys.stdout.write(f'{LoadingBar.BACKSPACE_CODE}')
                    sys.stdout.flush()
                    time.sleep(timeout)
            clear_symbols = not clear_symbols

    def start(self):
        self.__running = True
        self.__loading_task = Process(target=self.__show_loading)
        self.__loading_task.start()

    def stop(self):
        self.__running = False
        self.__loading_task.terminate()
        sys.stdout.write(LoadingBar.CLEAR_LINE_CODE)
        sys.stdout.flush()
