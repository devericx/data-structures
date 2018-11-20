from queue import Queue

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

    def pre_order(self):
        print(self.value)

        if self.left_child:
            self.left_child.pre_order()
        
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):
        if self.left_child:
            self.left_child.in_order()
        
        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()
        
        print(self.value)

    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.left_child:
                queue.put(current_node.left_child)
            
            if current_node.right_child:
                queue.put(current_node.right_child)
    
if __name__ == "__main__":
    root = BinaryTree(1)
    root.insert_left(2)
    root.insert_right(5)

    root.left_child.insert_left(3)
    root.left_child.insert_right(4)

    root.right_child.insert_left(6)
    root.right_child.insert_right(7)

    print("Pre-order:")
    root.pre_order()
    print()

    print("In-order:")
    root.in_order()
    print()

    print("Post-order:")
    root.post_order()
    print()

    print("BFS:")
    root.bfs()
    print()