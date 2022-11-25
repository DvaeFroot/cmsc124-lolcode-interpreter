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

class BasicNode():
    def __init__(self,token):
        self.token = token

    def __repr__(self) -> str:
        return f'({self.token})'

class NoobNode(BasicNode):
    pass

class NumbrNode(BasicNode):
    pass

class NumbarNode(BasicNode):
    pass

class YarnNode(BasicNode):
    pass

class TroofNode(BasicNode):
    pass

class OperatorNode(BasicNode):
    pass

class VariableNode(BasicNode):
    pass

class Program:
    def __init__(self, start_node, body_node,end_node) -> None:
        self.start_node = start_node
        self.body_node = body_node
        self.end_node = end_node

    def __repr__(self):
        return f'({self.start_node}, {self.body_node}, {self.end_node})'


class StatementListNode():
    def __init__(self,statementList):
        self.statementlist = statementList

    def __repr__(self) -> str:
        return f'({self.statementlist})'


class StatementNode():
    def __init__(self,type,statement):
        self.type = type
        self.statement = statement

    def __repr__(self) -> str:
        return f'({self.statement})\n'


class ArithmeticNode(BinOpNode):
    pass

class GimmehNode(UnaryOpNode):
    pass

class VisibleNode(UnaryOpNode):
    pass

class AssignmentLongNode():
    def __init__(self,ihasa,variable,itz,expr):
        self.ihasa = ihasa
        self.variable = variable
        self.itz = itz
        self.expr = expr

    def __repr__(self) -> str:
        return f'({self.ihasa}, {self.variable}, {self.itz}, {self.expr})'

class AssignmentShortNode():
    def __init__(self,variable,r,expr):
        self.variable = variable
        self.r = r
        self.expr = expr

    def __repr__(self) -> str:
        return f'({self.variable}, {self.r}, {self.expr})'


class ComparisonNode(BinOpNode):
    pass

class BooleanLongNode(BinOpNode):
    pass

class BooleanShortNode(UnaryOpNode):
    pass

class TypecastLongNode():
    def __init__(self,maek,expr,a,type):
        self.maek = maek
        self.expr = expr
        self.a = a
        self.type = type

    def __repr__(self) -> str:
        return f'({self.maek}, {self.expr}, {self.a}, {self.type})'

class TypecastShortNode():
    def __init__(self,maek,expr,type):
        self.maek = maek
        self.expr = expr
        self.type = type

    def __repr__(self) -> str:
        return f'({self.maek}, {self.expr}, {self.type})'

class SwitchNode:
    def __init__(self, op_token, expr) -> None:
        self.op_token = op_token
        self.expr = expr

    def __repr__(self) -> str:
        return f'({self.op_token}, {self.expr})'

class SwitchCaseNode:
    def __init__(self, omg, value, statement) -> None:
        self.omg = omg
        self.value = value
        self.statement = statement

    def __repr__(self) -> str:
        return f'({self.omg}, {self.value}, {self.statement})'

class CaseBreakNode(BasicNode):
    pass

class StringNode:
    def __init__(self, qt1, string, qt2) -> None:
        self.qt1 = qt1
        self.string = string
        self.qt2 = qt2

    def __repr__(self) -> str:
        return f'({self.qt1}, {self.string}, {self.qt2})'
