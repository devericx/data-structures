class LinkedList:
    class Node:
        def __init__(self, data, next = None):
            self.data = data
            self.next = next
    
    def __init__(self, data = None):
        self.head = self.Node(data)
        
    def add_to_head(self, data):
        new = self.Node(data, self.head)
        self.head = new

    def add_to_tail(self, data):
        new = self.Node(data)
        tail = self.end()
        tail.next = new
        
    def remove(self, data):
        return

    def remove_from_head(self):
        return

    def remove_from_tail(self):
        return

    def end(self):
        i = self.head
        while i.next != None:
            i = i.next  
        return i
    
    def print(self):
        i = self.head
        while i != None:
            if i.next != None:
                print(str(i.data) + " -> ", end = "")
            else: print(str(i.data))
            i = i.next
        print()

if __name__ == "__main__":
    print("[+] Creating LinkedList 'list' with head node value of 1 ...\n")
    list = LinkedList(1)

    list.print()

    print("[+] Adding node with data = 2 to tail of 'list' ...\n")
    list.add_to_tail(2)

    list.print()

    print("[+] Adding node with data = 0 to head of 'list' ...\n")
    list.add_to_head(0)

    list.print()
