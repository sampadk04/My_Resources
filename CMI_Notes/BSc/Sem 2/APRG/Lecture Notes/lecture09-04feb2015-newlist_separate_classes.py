class List:

    def __init__(self, x = None):
        if x != None:
            self.head = Node(x)
        else:
            self.head = None
        return

    def isempty(self):
        return (self.head == None)
    
    def append(self,x):
        if self.isempty():
            self.head = Node(x)
        else:
            self.head.append(x)
        return

    def insert(self,x):
        if self.isempty():
            self.head = Node(x)
        else:
            new = Node(x)
            new.next = self.head
            self.head = new
        return

    def delete(self,x):
        if not(self.isempty()):
            if self.head.value == x:
                self.head = self.head.next
            else:
                self.head.delete(x)
        return

    def __str__(self):
        mylist = []
        if not(self.isempty()):
            node = self.head
            mylist.append(node.value)
            while node.next != None:
                node = node.next
                mylist.append(node.value)

        return(str(mylist))


class Node:
    def __init__(self,x):
        self.value = x
        self.next = None
        return

    def append(self,x):
        self.appendi(x)

    def appendr(self,x):
        if self.next == None:
            self.next = Node(x)
        else:
            self.next.appendr(x)
        return

    def appendi(self,x):
        node = self
        while node.next != None:
            node = node.next
        node.next = Node(x)
        return

    def delete(self,x):
        self.deletei(x)

    def deleter(self,x):
        if self.next != None:
            if self.next.value == x:
                self.next = self.next.next
            else:
                self.next.deleter(x)
        return

    def deletei(self,x):
        node = self
        while node.next != None:
            if node.next.value == x:
                node.next = node.next.next
                return
            node = node.next
        return


