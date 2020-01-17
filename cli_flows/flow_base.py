from abc import ABC, abstractmethod


class FlowBase(ABC):
    def __init__(self):
        super(FlowBase, self).__init__()

    @staticmethod
    def ask_user_to_overwrite_existing(msg: str, yes_symbol, no_symbol):
        result = None
        received_correct_user_input = False
        while not received_correct_user_input:
            overwrite_input = input(f'{msg} ')
            if overwrite_input.lower().strip() == yes_symbol:
                received_correct_user_input = True
                result = True
            elif overwrite_input.lower().strip() == no_symbol:
                received_correct_user_input = True
                result = False
        return result

    @abstractmethod
    def start(self):
        pass
