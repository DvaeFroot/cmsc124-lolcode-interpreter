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


class ArithmeticNode():
    def __init__(self,operator,left,an,right):
        self.operator = operator
        self.left = left
        self.an = an
        self.right = right

    def __repr__(self) -> str:
        return f'({self.operator}, {self.left}, {self.an}, {self.right})\n'

class GimmehNode():
    def __init__(self,left, right):
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'({self.left}, {self.right})'


class VisibleNode():
    def __init__(self,left, right):
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'({self.left}, {self.right})'

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

class ComparisonNode:
    def __init__(self, op_token, expr1, an, expr2) -> None:
        self.op_token = op_token
        self.expr1 = expr1
        self.an = an
        self.expr2 = expr2

    def __repr__(self) -> str:
        return f'({self.op_token}, {self.expr1}, {self.an}, {self.expr2})'


class BooleanLongNode:
    def __init__(self, op_token, expr1, an, expr2) -> None:
        self.op_token = op_token
        self.expr1 = expr1
        self.an = an
        self.expr2 = expr2

    def __repr__(self) -> str:
        return f'({self.op_token}, {self.expr1}, {self.an}, {self.expr2})'


class BooleanShortNode:
    def __init__(self, op_token, expr) -> None:
        self.op_token = op_token
        self.expr = expr

    def __repr__(self) -> str:
        return f'({self.op_token}, {self.expr})'
