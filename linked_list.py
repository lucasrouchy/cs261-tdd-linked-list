# LinkedList: A doubly-linked list.
# Bonus: Has an insert_in_order that, when used, keeps the values of
#        each node in ascending order.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_sorted_list.py.
# YOUR NAME

class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.next = self
        self.prev = self
    def is_sentinel(self):
        if self.value == None:
            return True
    def is_empty(self):
        if self.prev == self and self.next == self:
            return True
    def is_last(self):
        if self.next.is_sentinel():
            return self
    def last(self):
        if self.is_last():
            return self
        return self.next.last()
    def append(self, new_node):
        if self.is_empty():
            self.next = new_node
            new_node.next = self
            self.prev = new_node
            new_node.prev = self
            return
        if self.is_sentinel():
            self.prev = new_node
            new_node.next = self
            self = self.last()
            self.next = new_node
            new_node.prev = self
            return
        return self.next.append(new_node)
    def delete(self):
        self = self.prev
        self.prev = self.prev.prev
        self = self.next
        self.next = self.next.next
    
    #def insert(self):

