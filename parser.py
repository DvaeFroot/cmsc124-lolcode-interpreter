from token_types import *
from nodes import *

class Error(Exception):
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return 'Error LOL'

    def __str__(self) -> str:
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


    def print(self):
        if self.current_tok.type in (TT_OUTPUT):
            left = self.current_tok
            right = self.advance()
            if right.type not in (TT_IDENTIFIER):
                raise Error()

            res = GimmehNode(left, right)
            return res
        raise Error()


    def get_input(self):
        if self.current_tok.type in (TT_READ):
            left = self.current_tok
            right = self.advance()
            if right.type not in (TT_IDENTIFIER):
                return Error()

            res = GimmehNode(left, right)
            return res
        return Error()

    def comparison(self):
        if self.current_tok.type in (GP_COMPARISON):
            op_token = self.current_tok
            self.advance()
            expr1 = self.expr()
            an = self.advance()
            if an.type not in (TT_ARG_SEP):
                raise Error()
            self.advance()
            expr2 = self.expr()
            res = ComparisonNode(op_token, expr1, an, expr2)
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


    def variableLong(self):
        if self.current_tok.type in (TT_VAR_DEC):
            ihasa_token = self.current_tok

            variable = self.advance()
            if variable.type not in (TT_IDENTIFIER):
                return Error()
            variable = VariableNode(self.current_tok)
            itz = self.advance()
            if itz.type not in (TT_VAR_ASSIGN):
                return Error()
            self.advance()
            expr = self.expr()

            res = AssignmentLongNode(ihasa_token, variable, itz, expr)
            return res


    def variableShort(self):
        if self.current_tok.type in (TT_IDENTIFIER):

            variable = self.current_tok
            if variable.type not in (TT_IDENTIFIER):
                return Error()

            variable = VariableNode(self.current_tok)

            r = self.advance()
            if r.type not in (TT_VAR_VAL_ASSIGN):
                return Error()

            self.advance()
            expr = self.expr()

            res = AssignmentShortNode(variable, r, expr)
            return res

    def typecast(self):
        if self.current_tok.type in (TT_TYPECAST_2):

            maek = self.current_tok

            self.advance()
            expr = self.expr()

            possibleA = self.advance()
            if possibleA.type in (TT_A):
                pass
            elif possibleA.type in (TT_TYPE):
                return TypecastShortNode(maek,expr,possibleA)
            else:
                return Error()

            ttype = self.advance()
            if ttype.type not in (TT_TYPE):
                return Error()

            res = TypecastLongNode(maek,expr,possibleA,ttype)
            return res



    def boolean(self):
        if self.current_tok.type in (GP_BOOLEAN_LONG):
            op_token = self.current_tok
            self.advance()
            expr1 = self.expr()
            an = self.advance()
            if an.type not in (TT_ARG_SEP):
                raise Error()
            self.advance()
            expr2 = self.expr()
            res = BooleanLongNode(op_token, expr1, an, expr2)
            return res
        elif self.current_tok.type in (GP_BOOLEAN_SHORT):
            op_token = self.current_tok
            self.advance()
            expr = self.expr()
            res = BooleanShortNode(op_token, expr)
            return res


    def statement(self):
        res = None
        if self.current_tok.type in (GP_ARITHMETIC):
            res = self.expr()
        elif self.current_tok.type in (TT_READ):
            res = self.get_input()
        elif self.current_tok.type in (TT_OUTPUT):
            res = self.print()
        elif self.current_tok.type in (TT_VAR_DEC):
            res = self.variableLong()
        elif self.current_tok.type in (TT_IDENTIFIER):
            res = self.variableShort()
        elif self.current_tok.type in (GP_COMPARISON):
            res = self.comparison()
        elif self.current_tok.type in (GP_BOOLEAN_LONG+GP_BOOLEAN_SHORT):
            res = self.boolean()
        elif self.current_tok.type in (TT_TYPECAST_2):
            res = self.typecast()

        return StatementNode("",res)


    def body(self):
        while(self.token_idx+1 < len(self.tokens)):
            if self.tokens[self.token_idx+1].type not in (TT_CODE_END):
                if self.token_idx+1 < len(self.tokens):
                    yield self.statement()
                    self.advance()
            else:
                 break


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



