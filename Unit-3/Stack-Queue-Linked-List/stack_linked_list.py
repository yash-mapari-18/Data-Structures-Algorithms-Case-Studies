# Stack implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def display(self):
        current = self.top

        while current:
            print(current.data)
            current = current.next


stack = Stack()

stack.push("Type Hello")
stack.push("Type World")
stack.push("Delete World")

print("Stack:")
stack.display()

print("\nPopped:", stack.pop())
print("Top:", stack.peek())
