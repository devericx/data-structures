class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    
    def insert_left(self, value):
        new = BinaryTree(value)
        if self.left_child:
            new.left_child = self.left_child
            self.left_child = new
        else:
            self.left_child = new

    def insert_right(self, value):
        new = BinaryTree(value)
        if self.right_child:
            new.right_child = self.right_child
            self.right_child = new
        else:
            self.right_child = new