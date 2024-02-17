# Creating a stack
class Stack:
    def __init__(self):
        self.items = []   # Creating a list.... The stack at the end is a list.

    def is_empty(self):
        return self.items == []

    def push(self, item):  # We used append in this way.
        self.items.append(item)

    def pop(self):  # Give error if the stack is empty
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Stack2:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):  # We used 'insert' in this way.
        self.items.insert(0, item)

    def pop(self):  # Give error if the stack is empty
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


# ---------- The difference between append and insert ---------
# - append => insert item at the end of the list.
# - insert => insert item at a specified place.
