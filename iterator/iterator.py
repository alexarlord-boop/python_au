class node:
    def __init__(self, val):
        self.val = {"name": val[0], "group": val[1], "subgroup": val[2]}
        self.next = None

    def __str__(self):
        return f"Name: {self.val['name']} Group: {self.val['group']} Subgroup: {self.val['subgroup']}"


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.lst = []
        self.counter = 0
        self.limit = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.get(self.counter - 1)
        else:
            raise StopIteration

    def printlist(self):
        for elem in self:
            print(elem)

    def get(self, index) -> int:
        if index < len(self.lst):
            return f"{index}. " + str(self.lst[index])
        else:
            return -1

    def addAtHead(self, val) -> None:
        new_node = node(val)
        new_node.next = self.head
        self.head = new_node
        self.lst.insert(0, self.head)
        self.limit += 1

    def addAtTail(self, val) -> None:
        new_node = node(val)

        if len(self.lst) == 0:
            self.lst.append(new_node)
            self.head = new_node
            return

        lastnode = self.lst[len(self.lst) - 1]
        lastnode.next = new_node
        self.lst.append(new_node)
        self.limit += 1

    def addAtIndex(self, index: int, val) -> None:
        new_node = node(val)
        if index == 0:
            self.lst.insert(index, new_node)
            new_node.next = self.head
            self.head = new_node
            return

        prev_node = self.lst[index - 1]
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.next = next_node
        self.lst.insert(index, new_node)
        self.limit += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.lst):
            if index == 0:
                delete_node = self.head
                delete_node.next = None
                self.head = self.head.next
                self.lst.pop(index)
                return

            prev_node = self.lst[index - 1]
            delete_node = prev_node.next
            prev_node.next = delete_node.next
            delete_node.next = None
            self.lst.pop(index)

            self.limit -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

ml = MyLinkedList()
ml.addAtHead(['A', 102, 2])
ml.addAtHead(['B', 102, 2])
ml.addAtHead(['C', 102, 1])

# print(next(ml))
# print(next(ml))
# print(next(ml))

# for student in ml:
#     print(student)

# ml.printlist()