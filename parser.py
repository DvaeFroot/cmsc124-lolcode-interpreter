from token_types import *
from nodes import *

class Error:
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return 'Error LOL'


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
        return res

    # OTHER STUFF

    def code(self):
        #Start of code
        if self.current_tok.type != TT_CODE_STRT or self.current_tok.type == TT_EOF:
            return Error()

        self.advance()

        #End of code

        return


