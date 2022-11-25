from token_types import *


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.token_idx = 0

    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_tok = self.tokens[self.token_idx]
        return self.current_tok

    def parse(self):
        res = self.code()

    # OTHER STUFF

    def code(self):
        pass


