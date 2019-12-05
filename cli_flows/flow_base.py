class FlowBase:
    def __init__(self):
        pass

    @staticmethod
    def ask_user_to_overwrite_existing(msg: str):
        result = None
        received_correct_user_input = False
        while not received_correct_user_input:
            overwrite_input = input(f'{msg} ')
            if overwrite_input.lower().strip() == 'n':
                received_correct_user_input = True
                result = False
            elif overwrite_input.lower().strip() == 'y':
                received_correct_user_input = True
                result = True
        return result
