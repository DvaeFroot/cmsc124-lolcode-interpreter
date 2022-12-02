class BasicNode:
    def __init__(self,token):
        self.token = token

    def __repr__(self) -> str:
        return f'({self.token})'


class UnaryOpNode:
    def __init__(self,left, right):
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'({self.left}, {self.right})'


class BinOpNode:
    def __init__(self, op_token, expr1, an, expr2) -> None:
        self.op_token = op_token
        self.expr1 = expr1
        self.an = an
        self.expr2 = expr2

    def __repr__(self) -> str:
        return f'({self.op_token}, {self.expr1}, {self.an}, {self.expr2})'


class DoubleOpNode:
    def __init__(self, left, middle, right) -> None:
        self.left = left
        self.middle = middle
        self.right = right

    def __repr__(self) -> str:
        return f'({self.left}, {self.middle}, {self.right})'


class NoobNode(BasicNode):
    def __init__(self, token):
        super().__init__(token)


class NumbrNode(BasicNode):
    def __init__(self, token):
        super().__init__(token)


class NumbarNode(BasicNode):
    def __init__(self, token):
        super().__init__(token)


class YarnNode(BasicNode):
    def __init__(self, token):
        super().__init__(token)


class OperatorNode(BasicNode):
    def __init__(self, token):
        super().__init__(token)


class VariableNode(BasicNode):
    def __init__(self, token):
        super().__init__(token)


class Program:
    def __init__(self, start_node, body_node,end_node) -> None:
        self.start_node = start_node
        self.body_node = body_node
        self.end_node = end_node

    def __repr__(self):
        return f'({self.start_node}, {self.body_node}, {self.end_node})'


class StatementNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


class ArithmeticNode(BinOpNode):
    def __init__(self, op_token, expr1, an, expr2) -> None:
        super().__init__(op_token, expr1, an, expr2)


class GimmehNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


class VisibleNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


class AssignmentShlongNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


class AssignmentLongNode(BinOpNode):
    def __init__(self, op_token, expr1, an, expr2) -> None:
        super().__init__(op_token, expr1, an, expr2)

#VAR R EXPR
class AssignmentShortNode(DoubleOpNode):
    def __init__(self, left, middle, right) -> None:
        super().__init__(left, middle, right)


class ComparisonNode(BinOpNode):
    def __init__(self, op_token, expr1, an, expr2) -> None:
        super().__init__(op_token, expr1, an, expr2)


class BooleanLongNode(BinOpNode):
    def __init__(self, op_token, expr1, an, expr2) -> None:
        super().__init__(op_token, expr1, an, expr2)


class BooleanShortNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


class TypecastLongNode(BinOpNode):
    def __init__(self, op_token, expr1, an, expr2) -> None:
        super().__init__(op_token, expr1, an, expr2)


class TypecastShortNode(DoubleOpNode):
    def __init__(self, left, middle, right) -> None:
        super().__init__(left, middle, right)


class SwitchNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


#OMG VALUE STATEMENT
class SwitchCaseNode(DoubleOpNode):
    def __init__(self, left, middle, right) -> None:
        super().__init__(left, middle, right)

#OMGWTF
class DefaultCaseNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


#
class CaseBreakNode(BasicNode):
    def __init__(self, token):
        super().__init__(token)


#ORLY
class IfNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


#MEBBE VALUE ELSEBODY
class ElseIfNode(DoubleOpNode):
    def __init__(self, left, middle, right) -> None:
        super().__init__(left, middle, right)


#NOWAI
class ElseNode(UnaryOpNode):
    def __init__(self, left, right):
        super().__init__(left, right)


class StringNode(DoubleOpNode):
    def __init__(self, left, middle, right) -> None:
        super().__init__(left, middle, right)


class TroofNode(BasicNode):
    def __init__(self, token):
        super().__init__(token)


class LoopNodeShort:
    def __init__(self, del_start, label_start, operation, yr, var, codeblock, del_end, label_end) -> None:
        self.del_start = del_start
        self.label_start = label_start
        self.operation = operation
        self.yr = yr
        self.var = var
        self.codeblock = codeblock
        self.del_end = del_end
        self.label_end = label_end

    def __repr__(self) -> str:
        return f'({self.del_start}, {self.label_start}, {self.operation}, {self.yr}, {self.var}, {self.codeblock}, {self.del_end}, {self.label_end})'


class LoopNodeLong:
    def __init__(self, del_start, label_start, operation, yr, var, cond, cond_expr, codeblock, del_end, label_end) -> None:
        self.del_start = del_start
        self.label_start = label_start
        self.operation = operation
        self.yr = yr
        self.var = var
        self.cond = cond
        self.cond_expr = cond_expr
        self.codeblock = codeblock
        self.del_end = del_end
        self.label_end = label_end

    def __repr__(self) -> str:
        return f'({self.del_start}, {self.label_start}, {self.operation}, {self.yr}, {self.var}, {self.cond},{self.cond_expr},{self.codeblock}, {self.del_end})'

