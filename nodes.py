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

class StatementNode():
    def __init__(self,type,statement):
        self.type = type
        self.statement = statement

class ArithmeticNode():
    def __init__(self,operator,left,an,right):
        self.operator = operator
        self.left = left
        self.an = an
        self.right = right

class OperatorNode():
    def __init__(self,token):
        self.token = token

class NumbrNode():
    def __init__(self,token):
        self.token = token

class NumbarNode():
    def __init__(self,token):
        self.token = token