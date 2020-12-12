class Node:
    def __init__(self, data) -> None:
        super().__init__()
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class LinkedList:
    def __init__(self, head=None) -> None:
        super().__init__()
        self.head = head
        self.count = 0

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.count += 1

    def find(self, idx):
        if idx > self.count - 1:
            return
        else:
            tmp = 0
            node = self.head
            while tmp < idx:
                node = node.get_next()
                tmp += 1
            return node.get_data()

    def delete_at(self, idx):
        if idx > self.count - 1:
            return
        elif idx == 0:
            self.head = self.head.get_next()
            self.count -= 1
        else:
            tmp = 0
            node = self.head
            while tmp < idx - 1:
                node = node.get_next()
                tmp += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        node = self.head
        while node is not None:
            print(node.get_data(), end="\t")
            node = node.get_next()
        print()


llist = LinkedList()
llist.insert(23)
llist.insert(12)
llist.insert(54)
llist.insert(21)
llist.dump_list()
print(llist.find(0))
print(llist.find(1))
print(llist.find(2))
print(llist.find(3))
print(llist.find(4))

llist.delete_at(2)
llist.dump_list()
