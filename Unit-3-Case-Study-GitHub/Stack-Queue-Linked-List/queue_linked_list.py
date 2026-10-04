# Queue implementation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None

        data = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def display(self):
        current = self.front

        while current:
            print(current.data)
            current = current.next


queue = Queue()

queue.enqueue("Document 1")
queue.enqueue("Document 2")
queue.enqueue("Document 3")

print("Queue:")
queue.display()

print("\nPrinted:", queue.dequeue())

print("Remaining Queue:")
queue.display()
