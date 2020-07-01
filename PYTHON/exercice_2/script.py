class Node():
    """Node Class
    Args: None
    Returns: None
    """
    def __init__(self, data):
        self.data = data
        self.children = []

    def insertNode(self, obj):
        """insertNode
        Args: Node object
        Returns: None
        """
        self.children.append(obj)
        return obj

    def traverse(self, root=False):
        """insertNode
        Args: Node object
        Returns: None
        """
        path = []
        if root:
            path = [self.data]

        if len(self.children) > 0:
            path = path + self.get_children_data()
            for child in self.children:
                if len(child.children) > 0:
                    path = path + child.traverse()
        return path

    def get_children_data(self):
        return [child.data for child in self.children]

# Tree definition
root = Node('7')
node3 = root.insertNode(Node('3'))
root.insertNode(Node('15'))
root.insertNode(Node('16'))
node1 = node3.insertNode(Node('1'))
node8 = node3.insertNode(Node('8'))
node1.insertNode(Node('0'))
node1.insertNode(Node('4'))
node8.insertNode(Node('17'))
node8.insertNode(Node('18'))

# Tree traversing
print(' - '.join(root.traverse(True)))

