class node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        if self.head is None:
            self.head = node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node(val)

    def print_list(self):
        current = self.head
        while current:
            print(current.val)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse_list_recursive(self):
        def reverse_recursive(prev, current):
            if current is None:
                return prev
            next = current.next
            current.next = prev
            return reverse_recursive(current, next)

        self.head = reverse_recursive(None, self.head)

    def reverse_list_recursive2(self):
        def reverse_recursive2(current):
            if current.next is None:
                self.head = current
                return current
            prev = reverse_recursive2(current.next)
            prev.next = current
            return current

        if self.head:
            reverse_recursive2(self.head).next = None

    def reverse_list_recursive3(self):
        def reverse_recursive3(current):
            if current is None or current.next is None:
                return current
            next = current.next
            current.next = None
            rest = reverse_recursive3(next)
            next.next = current
            return rest

        self.head = reverse_recursive3(self.head)
linked_list = linked_list()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)
linked_list.print_list()
linked_list.reverse_list()
linked_list.print_list()
linked_list.reverse_list_recursive()
linked_list.print_list()
linked_list.reverse_list_recursive2()
linked_list.print_list()
linked_list.reverse_list_recursive3()
linked_list.print_list()
