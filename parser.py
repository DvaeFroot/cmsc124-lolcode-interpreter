from token_types import *
from nodes import *

class Error(Exception):
    def __init__(self, token) -> None:
        self.token = token

    def __repr__(self) -> str:
        return f'Error LOL at {self.token}'

    def __str__(self) -> str:
        return f'Error LOL at {self.token}'

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
                raise Error(right)

            res = VisibleNode(left, right)
            return res
        raise Error(self.current_tok)


    def get_input(self):
        if self.current_tok.type in (TT_READ):
            left = self.current_tok
            right = self.advance()
            if right.type not in (TT_IDENTIFIER):
                raise Error(self.current_tok)

            res = GimmehNode(left, right)
            return res
        raise Error(self.current_tok)


    def comparison(self):
        if self.current_tok.type in (GP_COMPARISON):
            op_token = self.current_tok
            self.advance()
            expr1 = self.expr()
            an = self.advance()
            if an.type not in (TT_ARG_SEP):
                raise Error(self.current_tok)
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
                raise Error(self.current_tok)
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
        elif self.current_tok.type in (TT_STR_DELIMITER):
            return self.string()
        elif self.current_tok.type in (TT_BOOLEAN):
            return TroofNode(self.current_tok)

        raise Error(self.current_tok)


    def variableLong(self):
        if self.current_tok.type in (TT_VAR_DEC):
            ihasa_token = self.current_tok

            variable = self.advance()
            if variable.type not in (TT_IDENTIFIER):
                raise Error(self.current_tok)
            variable = VariableNode(self.current_tok)
            itz = self.advance()
            if itz.type not in (TT_VAR_ASSIGN):
                raise Error(self.current_tok)
            self.advance()
            expr = self.expr()

            res = AssignmentLongNode(ihasa_token, variable, itz, expr)
            return res


    def variableShort(self):
        if self.current_tok.type in (TT_IDENTIFIER):

            variable = self.current_tok
            if variable.type not in (TT_IDENTIFIER):
                raise Error(self.current_tok)

            variable = VariableNode(self.current_tok)

            r = self.advance()
            if r.type not in (TT_VAR_VAL_ASSIGN):
                raise Error(self.current_tok)

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
                raise Error(self.current_tok)

            ttype = self.advance()
            if ttype.type not in (TT_TYPE):
                raise Error(self.current_tok)

            res = TypecastLongNode(maek,expr,possibleA,ttype)
            return res


    def boolean(self):
        if self.current_tok.type in (GP_BOOLEAN_LONG):
            op_token = self.current_tok
            self.advance()
            expr1 = self.expr()
            an = self.advance()
            if an.type not in (TT_ARG_SEP):
                raise Error(self.current_tok)
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


    def casebody(self):
        while(self.token_idx < len(self.tokens)):
            if self.tokens[self.token_idx].type not in (TT_CASE,TT_CONTROL_END):
                if self.token_idx < len(self.tokens):
                    if self.current_tok.type in (TT_CASEBREAK):
                        yield CaseBreakNode(self.current_tok)
                    else:
                        yield self.statement()
                    self.advance()
            else:
                 break


    def switchcase(self):
        while(self.token_idx < len(self.tokens)):
            if self.tokens[self.token_idx].type not in (TT_CONTROL_END):
                if self.token_idx < len(self.tokens):
                    omg = self.current_tok
                    value = self.advance()
                    if value.type not in (GP_LITERAL):
                        raise Error(self.current_tok)
                    casebody = list(self.casebody())
                    yield SwitchCaseNode(omg, value, casebody)
            else:
                 break


    def switch(self):
        if self.current_tok.type in (TT_SWITCH):
            op_token = self.current_tok
            self.advance()
            expr = list(self.switchcase())
            oic = self.current_tok
            if oic.type not in (TT_CONTROL_END):
                raise Error(self.current_tok)
            res = SwitchNode(op_token, expr)
            return res
        else:
            raise Error(self.current_tok)


    def string(self):
        if self.current_tok.type in (TT_STR_DELIMITER):
            qt1 = self.current_tok
            string = self.advance()
            if string.type not in (TT_STRING):
                raise Error(self.current_tok)
            qt2 = self.advance()
            if qt2.type not in (TT_STR_DELIMITER):
                raise Error(self.current_tok)
            res = StringNode(qt1, string, qt2)
            return res
        return Error(self.current_tok)


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
        elif self.current_tok.type in (TT_SWITCH):
            res = self.switch()
        elif self.current_tok.type in (TT_STR_DELIMITER):
            res = self.string()

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
            if self.current_tok.type not in (TT_CODE_STRT):
                raise Error(self.current_tok)

            start_node = self.current_tok
            self.advance()

            body_node = list(self.body())

            #End of code
            end_node = self.advance()
            if self.current_tok.type not in (TT_CODE_END):
                raise Error(self.current_tok)

            res = Program(start_node, body_node, end_node)

            return res
        except Error as err:
            return err



