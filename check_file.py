
class Check:
    def __init__(self):
        self.winner = None
    def check_who_win(self, choices):
        if 0 in choices and 1 in choices and 2 in choices:
            self.winner = choices
            return True

        if 3 in choices and 4 in choices and 5 in choices:
            self.winner = choices
            return True

        if 6 in choices and 7 in choices and 8 in choices:
            self.winner = choices
            return True

        if 0 in choices and 3 in choices and 6 in choices:
            self.winner = choices
            return True

        if 1 in choices and 4 in choices and 7 in choices:
            self.winner = choices
            return True

        if 2 in choices and 5 in choices and 8 in choices:
            self.winner = choices
            return True

        if 0 in choices and 4 in choices and 8 in choices:
            self.winner = choices
            return True

        if 2 in choices and 4 in choices and 6 in choices:
            self.winner = choices
            return True

