# Unit III – Case Study: Implementation of Stack and Queue Operations Using Linked Lists

## 1. Introduction

Stack, Queue, and Linked List are important linear data structures.

They are widely used in:

- Operating systems
- Web browsers
- Compilers
- CPU scheduling
- Network systems
- Undo/Redo operations
- Expression evaluation
- Printer scheduling
- Memory management

This case study explains these data structures and demonstrates how Stack and Queue operations can be implemented using Linked Lists.

---

# 2. Stack

A Stack is a linear data structure that follows:

**LIFO – Last In, First Out**

The element inserted last is removed first.

Example:

```text
        TOP
         |
       [30]
       [20]
       [10]
         |
       BOTTOM
```

If `30` is inserted last, it will be removed first.

## Stack Operations

### Push

Adds an element to the top.

```text
Before: 10 → 20
Push 30
After:  10 → 20 → 30
```

### Pop

Removes the top element.

```text
10 → 20 → 30
Pop
10 → 20
```

### Peek

Returns the top element without removing it.

### IsEmpty

Checks whether the stack contains no elements.

### IsFull

Mainly relevant to fixed-size array implementations.

---

# 3. Multiple Stacks

Multiple stacks means maintaining more than one stack.

For example:

```text
Stack 1              Stack 2

TOP                  TOP
 |                    |
[30]                 [50]
[20]                 [40]
[10]                 [35]
```

Multiple stacks can be implemented using:

- Multiple arrays
- A shared array
- Multiple linked lists

They can be useful when different categories of data need separate LIFO structures.

---

# 4. Applications of Stack

Stacks are used in:

1. Function calls
2. Recursion
3. Undo/Redo
4. Browser back button
5. Expression conversion
6. Expression evaluation
7. Parentheses matching
8. Depth First Search
9. Backtracking
10. Compiler processing

---

# 5. Expression Notations

Arithmetic expressions can be represented in three common forms.

## Infix

Operator is written between operands.

```text
A + B
```

Example:

```text
A + B * C
```

## Prefix

Operator is written before operands.

```text
+ A B
```

For:

```text
A + B * C
```

Prefix form is:

```text
+ A * B C
```

## Postfix

Operator is written after operands.

```text
A B +
```

For:

```text
A + B * C
```

Postfix form is:

```text
A B C * +
```

---

# 6. Infix to Postfix Conversion

A stack is commonly used for converting infix expressions into postfix expressions.

Example:

```text
Infix:
A + B * C
```

Because multiplication has higher precedence:

```text
Postfix:
A B C * +
```

General steps:

1. Scan the expression from left to right.
2. If the symbol is an operand, add it to output.
3. If it is `(`, push it onto the stack.
4. If it is an operator, compare precedence.
5. Pop higher/equal precedence operators from the stack when required.
6. Push the current operator.
7. At the end, pop remaining operators.

---

# 7. Infix to Prefix Conversion

Another stack-based method is used for Prefix conversion.

Example:

```text
Infix:
A + B * C
```

Prefix:

```text
+ A * B C
```

A common method is:

1. Reverse the infix expression.
2. Swap `(` and `)`.
3. Convert the resulting expression to postfix.
4. Reverse the postfix result.

---

# 8. Postfix Expression Evaluation

A stack can also evaluate postfix expressions.

Example:

```text
Postfix:
2 3 4 * +
```

Steps:

```text
Push 2
Push 3
Push 4

4 * 3 = 12

Stack:
2, 12

2 + 12 = 14
```

Final result:

```text
14
```

### Algorithm

1. Scan postfix expression from left to right.
2. If operand, push it.
3. If operator:
   - Pop operand 2.
   - Pop operand 1.
   - Apply the operator.
   - Push the result.
4. The final stack element is the answer.

---

# 9. Queue

A Queue is a linear data structure that follows:

**FIFO – First In, First Out**

The element inserted first is removed first.

Example:

```text
FRONT                         REAR
  |                             |
 [10] → [20] → [30] → [40]
```

`10` will be removed first.

---

# 10. Queue Operations

### Enqueue

Adds an element at the rear.

```text
10 → 20
Enqueue 30

10 → 20 → 30
```

### Dequeue

Removes an element from the front.

```text
10 → 20 → 30
Dequeue

20 → 30
```

### Front

Returns the first element.

### Rear

Returns the last element.

### IsEmpty

Checks whether the queue is empty.

---

# 11. Circular Queue

In a normal array queue, empty positions at the beginning may not be reused easily after several dequeue operations.

A Circular Queue solves this problem by connecting the last position back to the first.

Conceptually:

```text
      +-------------------+
      |                   |
      v                   |
[0] → [1] → [2] → [3] → [4]
 ^                       |
 |_______________________|
```

The rear can wrap around to the beginning.

### Advantages

- Better utilization of array space.
- Avoids unnecessary shifting.
- Efficient enqueue and dequeue.
- Useful for fixed-size buffers.

---

# 12. Priority Queue

A Priority Queue stores elements according to their priority.

The element with higher priority is served before an element with lower priority.

Example:

```text
Patient A → Priority 3
Patient B → Priority 1
Patient C → Priority 5
```

If higher number means higher priority:

```text
Patient C
Patient A
Patient B
```

## Applications

Priority Queues are used in:

- CPU scheduling
- Hospital emergency systems
- Network packet scheduling
- Dijkstra's algorithm
- Prim's algorithm
- Event simulation
- Job scheduling

## Advantages

1. Important tasks can be processed first.
2. Useful for scheduling systems.
3. Efficient for priority-based processing.
4. Can be implemented using heaps, arrays, or linked structures.

---

# 13. Linked List

A Linked List is a dynamic linear data structure consisting of nodes.

Each node contains:

1. Data
2. Link/reference to another node

Example:

```text
HEAD
 |
 v
[10 | next] → [20 | next] → [30 | NULL]
```

Unlike arrays, linked-list nodes do not need to occupy contiguous memory locations.

---

# 14. Primitive Operations on Linked List

## Create

Create a new node.

## Traverse

Visit every node.

```text
10 → 20 → 30
```

## Search

Find a particular value.

## Insert

Insert a node:

- At beginning
- At end
- At a particular position

## Delete

Delete a node:

- From beginning
- From end
- From a particular position

## Sort

Arrange nodes in ascending or descending order.

Example:

```text
30 → 10 → 20
```

After sorting:

```text
10 → 20 → 30
```

## Concatenate

Join two linked lists.

```text
List 1: 10 → 20

List 2: 30 → 40

After concatenation:

10 → 20 → 30 → 40
```

---

# 15. Types of Linked Lists

## 15.1 Singly Linked List

Each node contains data and one next pointer.

```text
HEAD
 |
 v
[10] → [20] → [30] → NULL
```

Traversal is generally forward only.

---

## 15.2 Linear Linked List

The last node points to `NULL`.

```text
10 → 20 → 30 → NULL
```

This is the standard linear linked-list structure.

---

## 15.3 Circular Linked List

The last node points back to the first node.

```text
       +----------------+
       |                |
       v                |
10 → 20 → 30 → 40 ------+
^
|
HEAD
```

There is no `NULL` at the end.

### Applications

- Round-robin scheduling
- Circular buffers
- Multiplayer turn systems
- Repeated task scheduling

---

# 16. Doubly Linked List

A Doubly Linked List contains two links:

- Previous
- Next

Example:

```text
NULL ← [10] ⇄ [20] ⇄ [30] → NULL
```

It supports traversal in both directions.

### Advantages

- Forward traversal
- Backward traversal
- Easier deletion when a node reference is available

### Applications

- Browser history
- Undo/Redo
- Navigation systems
- Music playlists

---

# 17. Case Study: Stack Using Linked List

## Problem

Suppose a web browser needs an undo system.

Each new action is stored on a Stack.

The most recent action must be undone first.

Therefore, LIFO behavior is required.

A Linked List can be used to implement this Stack dynamically.

## Example

User performs:

```text
Type "Hello"
Type "World"
Delete "World"
```

Stack:

```text
TOP
 |
Delete "World"
Type "World"
Type "Hello"
```

When Undo is selected:

```text
Pop → Delete "World"
```

The latest operation is removed first.

---

# 18. Stack Linked List Implementation

```python
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
```

### Output

```text
Stack:
Delete World
Type World
Type Hello

Popped: Delete World
Top: Type World
```

---

# 19. Case Study: Queue Using Linked List

## Problem

Consider a printer system.

Multiple documents are waiting to be printed.

The document that arrives first should normally be printed first.

Therefore, FIFO behavior is required.

A Queue implemented using a Linked List is suitable.

Example:

```text
FRONT                           REAR
  |                               |
Doc1 → Doc2 → Doc3 → Doc4
```

When a document is printed:

```text
Dequeue Doc1
```

Remaining queue:

```text
FRONT
  |
Doc2 → Doc3 → Doc4
```

---

# 20. Queue Linked List Implementation

```python
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
```

### Output

```text
Queue:
Document 1
Document 2
Document 3

Printed: Document 1

Remaining Queue:
Document 2
Document 3
```

---

# 21. Time Complexity

## Stack using Linked List

| Operation | Complexity |
|---|---:|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |
| Search | O(n) |

## Queue using Linked List

| Operation | Complexity |
|---|---:|
| Enqueue | O(1) |
| Dequeue | O(1) |
| Front | O(1) |
| Search | O(n) |

The O(1) enqueue/dequeue operations are achieved by maintaining `front` and `rear` references.

---

# 22. Advantages of Linked-List Implementation

### Stack

1. Dynamic memory allocation.
2. No fixed size requirement.
3. Push and Pop are O(1).
4. Overflow occurs only when system memory is exhausted.

### Queue

1. Dynamic size.
2. Efficient enqueue and dequeue.
3. No shifting of elements.
4. Suitable when queue size changes frequently.

---

# 23. Array vs Linked List Implementation

| Feature | Array | Linked List |
|---|---|---|
| Size | Usually fixed/dynamic depending on language | Dynamic |
| Memory | Contiguous | Non-contiguous |
| Random Access | O(1) | O(n) |
| Insert/Delete at beginning | Can be costly | O(1) with head |
| Extra Pointer Memory | No | Yes |
| Stack/Queue Dynamic Size | Limited by array capacity | Easy |

---

# 24. Real-World Applications

## Stack

- Browser history
- Undo/Redo
- Function calls
- Expression evaluation
- Parentheses matching
- DFS

## Queue

- Printer queue
- CPU scheduling
- Network requests
- Customer service systems
- Task processing
- Breadth First Search

## Linked List

- Music playlists
- Browser navigation
- Memory management
- Undo/Redo systems
- Dynamic collections
- Scheduling systems

---

# 25. Conclusion

Stack follows LIFO while Queue follows FIFO.

Stacks are useful for expression conversion, expression evaluation, recursion, and undo operations.

Queues are useful for scheduling, printing, network processing, and task management.

Linked Lists provide dynamic memory allocation and make it possible to implement Stack and Queue without requiring a fixed-size array.

In this case study:

```text
Linked List
     |
     +---- Stack
     |       |
     |       +---- Push
     |       +---- Pop
     |       +---- Peek
     |
     +---- Queue
             |
             +---- Enqueue
             +---- Dequeue
```

Thus, Linked Lists provide a flexible and efficient way to implement Stack and Queue operations in real-world applications.
