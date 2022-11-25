from token_types import *
from nodes import *

class Error(Exception):
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return 'Error LOL'


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.token_idx = -1
        self.advance()


    def advance(self):
        self.token_idx += 1
        if self.token_idx < len(self.tokens):
            self.current_tok = self.tokens[self.token_idx]
        return self.current_tok


    def parse(self):
        res = self.code()
        return res


    def expr(self):
        if self.current_tok.type in (GP_ARITHMETIC):
            op_token = self.current_tok

            self.advance()
            left = self.expr()
            an = self.advance()
            if an.type not in (TT_ARG_SEP):
                return Error()
            self.advance()
            right = self.expr()

            res = ArithmeticNode(op_token, left, an, right)
            return res
        elif self.current_tok.type in (TT_FLOAT, TT_INTEGER):
            tok = self.current_tok
            if tok.type in (TT_FLOAT):
                return NumbarNode(tok)
            elif tok.type in (TT_INTEGER):
                return NumbrNode(tok)

        return Error()


    def statement(self):
        if self.current_tok.type in (GP_ARITHMETIC):
            res = self.expr()
        elif self.current_tok.type in (TT_OUTPUT):
            res = self.print()
        return res


    def body(self):
        while(self.tokens[self.token_idx+1].type not in (TT_CODE_END)):
            if self.token_idx+1 < len(self.tokens):
                yield self.statement()
                self.advance()
            elif self.token_idx+1 >= len(self.tokens):
                raise Error()
            else:
                yield None

    def code(self):

        try:
            #Start of code
            if self.current_tok.type != TT_CODE_STRT:
                return Error()

            start_node = self.current_tok
            self.advance()

            body_node = list(self.body())

            #End of code
            end_node = self.advance()
            if self.current_tok.type != TT_CODE_END:
                return Error()

            res = Program(start_node, body_node, end_node)

            return res
        except Error as err:
            print(err)



