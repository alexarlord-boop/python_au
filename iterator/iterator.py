class node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.lst = []
        self.counter = 0
        self.limit = 0

    def __iter__(self):
        if self.counter != 0:
            self.counter = 0
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
        self.counter = 0

    def get(self, index) -> int:
        if index < len(self.lst):
            return self.lst[index].val
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


if __name__ == "__main__":
    class Student:
        def __init__(self, name, g, subg):
            self.name = name
            self.g = g
            self.subg = subg

        def __str__(self):
            return f"{self.name} {self.g} {self.subg}"


    std1 = Student('A', 101, 1)
    std2 = Student('B', 101, 2)
    std3 = Student('C', 101, 3)

    std_lst = MyLinkedList()
    std_lst.addAtHead(std1)
    std_lst.addAtTail(std2)
    std_lst.addAtTail(std3)

    std_lst.printlist()
    print('--------')
    # std_lst.printlist()
    # print('--------')

    print(next(std_lst))
    print(next(std_lst))
    print(next(std_lst))
    print('--------')

    for std in std_lst:
        print(std)

