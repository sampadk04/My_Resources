class List:
    def __init__(self, x = None):
        self.value = x
        self.next = None
        return

    def isempty(self):
        if self.value == None:
            return(True)
        else:
            return(False)

    def append(self,x):
        self.appendr(x)
        return

    # append, recursive
    def appendr(self,x):
        if self.isempty():
            self.value = x
            return

        # if we are at the last node, insert here
        if self.next == None:
            newnode = List(x)
            self.next = newnode
        # else append recursively in rest of the list
        else:
            (self.next).appendr(x)
        return

    # append, iterative
    def appendi(self,x):
        if self.isempty():
            self.value = x
            return

        # Search for end of list
        temp = self
        while temp.next != None:
            temp = temp.next

        # Add new node at end of list
        newnode = List(x)
        temp.next = newnode
        return

    def insert(self,x):
        if self.isempty():
            self.value = x
            return

        newnode = List(x)
        
        # Wrong, cannot modify self!
        # newnode.next = self
        # self = newnode

        # Exchange values in self and newnode
        (self.value, newnode.value) = (newnode.value, self.value)

        # Or,
        # newnode = List(self.value)
        # self.value = x

        # Reconnect
        # newnode.next = self.next
        # self.next = newnode
        (newnode.next, self.next) = (self.next, newnode)

    def delete(self,x):
        self.deletei(x)
        return

    # delete, iterative
    def deletei(self,x):

        if self.isempty():
            return

        # value to be deleted is in first node 

        if self.value == x:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
            return

        # walk down the list and find first x to delete

        temp = self
        while temp.next != None:
            if temp.next.value == x:
                temp.next = temp.next.next
                return
            else:
                temp = temp.next
        return

    # delete, recursive
    def deleter(self,x):
        if self.isempty():
            return

        if self.value == x:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return
        else:
            if self.next != None:
                self.next.delete(x)
                if self.next.value == None:
                    self.next = self.next.next

        return
                
    def __str__(self):
        selflist = []
        if self.value == None:
            return(str(selflist))

        temp = self
        selflist.append(temp.value)
        
        while temp.next != None:
            temp = temp.next
            selflist.append(temp.value)

        return(str(selflist))
