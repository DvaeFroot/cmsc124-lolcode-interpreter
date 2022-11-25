class Program:
    def __init__(self, start_node, body_node,end_node) -> None:
        self.start_node = start_node
        self.body_node = body_node
        self.end_node = end_node

    def __repr__(self):
        return f'({self.start_node}, {self.body_node}, {self.end_node})'
