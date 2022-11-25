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
        if self.current_tok.type in (TT_COMMENT_STRT, TT_COMMENT_MULTI_STRT, TT_COMMENT_MULTI_END):
            self.advance()
        return self.current_tok


    def parse(self):
        res = self.code()
        return res


    def literal(self):
        if self.current_tok.type in (TT_FLOAT, TT_INTEGER):
            tok = self.current_tok
            if tok.type in (TT_FLOAT):
                return NumbarNode(tok)
            elif tok.type in (TT_INTEGER):
                return NumbrNode(tok)
        elif self.current_tok.type in (TT_STR_DELIMITER):
            return self.string()
        elif self.current_tok.type in (TT_BOOLEAN):
            return TroofNode(self.current_tok)

        return Error(self.current_tok)


    def print(self):
        if self.current_tok.type in (TT_OUTPUT):
            left = self.current_tok

            self.advance()
            right = self.expr()

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
        elif self.current_tok.type in (TT_IDENTIFIER):
            return VariableNode(self.current_tok)
        elif self.current_tok.type in (GP_COMPARISON):
            return self.comparison()

        raise Error(self.current_tok)


    def variableLong(self):
        if self.current_tok.type in (TT_VAR_DEC):
            ihasa_token = self.current_tok

            variable = self.advance()
            if variable.type not in (TT_IDENTIFIER):
                raise Error(self.current_tok)
            variable = VariableNode(self.current_tok)
            itz = self.tokens[self.token_idx+1]
            if itz.type not in (TT_VAR_ASSIGN):
                res = AssignmentShlongNode(ihasa_token, variable)
                return res
            itz = self.advance()
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
            if self.tokens[self.token_idx].type not in (TT_BREAK, TT_CASE,TT_CONTROL_END):
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
                    if omg.type not in (TT_BREAK):
                        self.advance()
                        value = self.literal()
                        self.advance()
                        casebody = list(self.casebody())
                        yield SwitchCaseNode(omg, value, casebody)
                    elif omg.type in (TT_BREAK):
                        self.advance()
                        casebody = list(self.casebody())
                        yield DefaultCaseNode(omg, casebody)
                        break
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


    def loopbody(self):
        while(self.token_idx < len(self.tokens)):
            if self.tokens[self.token_idx].type not in (TT_LOOP_END):
                if self.token_idx < len(self.tokens):
                    yield self.statement()
                    self.advance()
            else:
                 break


    def loop(self):
        if self.current_tok.type in (TT_LOOP_STRT):
            del_start = self.current_tok
            label_start = self.advance()
            if label_start.type not in (TT_IDENTIFIER):
                raise Error(self.current_tok)
            operation = self.advance()
            if operation.type not in (TT_INC, TT_DEC):
                raise Error(self.current_tok)
            yr = self.advance()
            if yr.type not in (TT_YR):
                raise Error(self.current_tok)
            var = self.advance()
            if var.type not in (TT_IDENTIFIER):
                raise Error(self.current_tok)
            cond = self.advance()
            if cond.type in (TT_WHILE, TT_UNTIL):
                self.advance()
                cond_expr = self.expr()
                self.advance()

                codeblock = list(self.loopbody())
                del_end = self.current_tok

                if del_end.type not in (TT_LOOP_END):
                    raise Error(self.current_tok)
                label_end = self.advance()
                if label_end.type not in (TT_IDENTIFIER):
                    raise Error(self.current_tok)

                res = LoopNodeLong(del_start, label_start, operation, yr, var, cond, cond_expr, codeblock, del_end, label_end)
                return res

            codeblock = list(self.loopbody())
            del_end = self.current_tok
            if del_end.type not in (TT_LOOP_END):
                raise Error(self.current_tok)
            label_end = self.advance()
            if label_end.type not in (TT_IDENTIFIER):
                raise Error(self.current_tok)

            res = LoopNodeShort(del_start, label_start, operation, yr, var, codeblock, del_end, label_end)
            return res


    def ifbody(self):
        while(self.token_idx < len(self.tokens)):
            if self.tokens[self.token_idx].type not in (TT_ELIF, TT_ELSE, TT_CONTROL_END):
                if self.token_idx < len(self.tokens):
                    yield self.statement()
                    self.advance()
            else:
                 break


    def elsecase(self):
        if self.current_tok.type not in (TT_TRUTH):
            raise Error(self.current_tok)
        yield IfNode(self.current_tok, list(self.ifbody()))
        self.advance()
        while(self.token_idx < len(self.tokens)):
            if self.tokens[self.token_idx].type not in (TT_CONTROL_END):
                if self.token_idx < len(self.tokens):
                    omg = self.current_tok
                    if omg.type in (TT_ELIF):
                        self.advance()
                        value = self.literal()
                        self.advance()
                        ifbody = list(self.ifbody())
                        yield ElseIfNode(omg, value, ifbody)
                    elif omg.type in (TT_ELSE):
                        self.advance()
                        casebody = list(self.ifbody())
                        yield ElseNode(omg, casebody)
                        break
            else:
                 break


    def ifelse(self):
        if self.current_tok.type in (TT_IF):
            op_token = self.current_tok
            self.advance()
            expr = list(self.elsecase())
            oic = self.current_tok
            if oic.type not in (TT_CONTROL_END):
                raise Error(self.current_tok)
            res = IfNode(op_token, expr)
            return res
        else:
            raise Error(self.current_tok)


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
        elif self.current_tok.type in (TT_LOOP_STRT):
            res = self.loop()
        elif self.current_tok.type in (TT_IF):
            res = self.ifelse()

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
