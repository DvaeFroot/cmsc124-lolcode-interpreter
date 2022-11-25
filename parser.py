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
        self.advance()

    def advance(self):
        if self.token_idx < len(self.tokens):
            self.current_tok = self.tokens[self.token_idx]
        self.token_idx += 1
        return self.current_tok

    def parse(self):
        res = self.code()
        return res

    def expr(self):
        return self.advance()

    # OTHER STUFF

    def code(self):
        #Start of code
        print(self.current_tok.val)
        if self.current_tok.type != TT_CODE_STRT:
            return Error()

        start_node = self.current_tok

        body_node = self.expr()

        #End of code
        end_node = self.advance()
        if self.current_tok.type != TT_CODE_END:
            return Error()

        res = Program(start_node, body_node, end_node)

        return res


