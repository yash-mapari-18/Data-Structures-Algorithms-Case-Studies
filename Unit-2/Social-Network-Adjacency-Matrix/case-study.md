# Unit II – Case Study: Social Network Adjacency Matrix

## 1. Introduction

Social networking platforms such as Facebook, Instagram, LinkedIn, and other community platforms may have millions of users.

Users are connected through:

- Friendships
- Followers
- Following relationships
- Professional connections
- Group memberships
- Other network relationships

Data structures and algorithms are required to store, search, and process these relationships efficiently.

This case study explains how arrays, 2D arrays, sparse matrices, searching, and sorting can be applied to a social network.

---

## 2. Problem Statement

Consider a small social network containing five users:

```text
U1, U2, U3, U4, U5
```

Their friendship relationships can be represented using an adjacency matrix.

```text
       U1 U2 U3 U4 U5
U1:     0  1  1  0  0
U2:     1  0  0  1  0
U3:     1  0  0  0  1
U4:     0  1  0  0  1
U5:     0  0  1  1  0
```

Here:

- `1` = connection/friendship exists
- `0` = no direct connection

For an undirected friendship network, the matrix is symmetric.

---

## 3. Objectives

The objectives are:

1. Represent social network connections using arrays.
2. Understand Array ADT operations.
3. Represent relationships using a 2D array.
4. Understand sparse matrix representation.
5. Search for users and connections efficiently.
6. Understand different sorting techniques.
7. Compare internal and external sorting.
8. Understand stability, efficiency, and number of passes.
9. Understand the memory problem when the number of users becomes very large.

---

# 4. Array and Array as an Abstract Data Type

An array stores elements of the same type in an organized structure.

For example:

```text
Users = [U1, U2, U3, U4, U5]
```

An Array ADT defines the operations that can be performed on an array without focusing on the internal implementation.

### Common Array ADT Operations

| Operation | Description |
|---|---|
| Create | Create an array |
| Insert | Add an element |
| Access | Access an element using index |
| Update | Change an element |
| Search | Find an element |
| Delete | Remove an element |
| Traverse | Visit all elements |

For a social network, an array can store:

- User IDs
- Friend IDs
- Follower counts
- User activity information

---

# 5. Operations on Array

Suppose:

```python
users = ["U1", "U2", "U3", "U4", "U5"]
```

### Access

```python
users[0]
```

Output:

```text
U1
```

### Update

```python
users[0] = "User1"
```

### Search

Search can be performed to find whether a particular user exists.

### Traversal

```python
for user in users:
    print(user)
```

---

# 6. Storage Representation

A normal array stores elements in contiguous memory locations.

For a one-dimensional array:

```text
Index:   0    1    2    3    4
         |    |    |    |    |
Value:  U1   U2   U3   U4   U5
```

For a 2D array:

```text
          Column
          0  1  2  3  4
       0  0  1  1  0  0
Row    1  1  0  0  1  0
       2  1  0  0  0  1
       3  0  1  0  0  1
       4  0  0  1  1  0
```

---

# 7. Multidimensional Arrays

## 2D Array

A 2D array consists of rows and columns.

For a social network:

```text
connections[user1][user2]
```

can indicate whether two users are connected.

Example:

```python
connections[0][1] = 1
```

This means U1 and U2 are connected.

## nD Array

An n-dimensional array contains more than two dimensions.

For example, a social network application could organize data by:

```text
Time × Region × User × Feature
```

This can be represented conceptually using an nD array.

---

# 8. Adjacency Matrix

An adjacency matrix is a 2D array used to represent connections in a graph.

For `n` users, the matrix contains:

```text
n × n
```

entries.

For example, for 5 users:

```text
5 × 5 = 25 entries
```

But for 1,000,000 users:

```text
1,000,000 × 1,000,000
= 1,000,000,000,000
= 10^12 entries
```

That is one trillion entries.

Therefore, a normal adjacency matrix becomes extremely expensive in memory for millions of users.

---

# 9. Sparse Matrix Representation

Most users in a large social network are not directly connected to every other user.

Therefore, most entries of the adjacency matrix are `0`.

Such a matrix is called a **sparse matrix**.

Instead of storing all zero values, we can store only the non-zero connections.

Example:

```text
(0,1)
(1,0)
(1,3)
(2,4)
(3,1)
(4,2)
```

Each pair represents an existing connection.

A triplet-style 2D representation can also be used:

```text
Row  Column  Value
0     1       1
1     0       1
1     3       1
2     4       1
3     1       1
4     2       1
```

This saves memory when the number of actual connections is much smaller than `n²`.

---

# 10. Searching in a Social Network

Searching is required to find users, user IDs, or connections.

## 10.1 Sequential / Linear Search

Linear search checks elements one by one.

Example:

```text
U1 → U2 → U3 → U4 → U5
```

If we search for U4, the algorithm checks:

```text
U1 → U2 → U3 → U4
```

### Complexity

- Best case: O(1)
- Worst case: O(n)

It is simple but inefficient for very large unsorted datasets.

---

## 10.2 Binary Search

Binary search works on a sorted array.

Example:

```text
[1001, 1005, 1010, 1020, 1030]
```

The middle element is checked first.

The search space is repeatedly divided into half.

### Complexity

```text
O(log n)
```

Binary search is much faster than linear search for large sorted arrays.

---

## 10.3 Fibonacci Search

Fibonacci Search uses Fibonacci numbers to divide a sorted array into smaller search regions.

It is another searching technique for sorted data.

### Complexity

```text
O(log n)
```

It can be useful in situations where sequential access characteristics are important.

---

## 10.4 Indexed Sequential Search

Indexed Sequential Search divides data into blocks.

An index is created for the blocks, and the index is used to find the appropriate block.

Then sequential search is performed inside that block.

Example:

```text
Index
  |
  +---- Block 1
  +---- Block 2
  +---- Block 3
  +---- Block 4
```

This can reduce the amount of data that must be searched.

---

# 11. Sorting in Social Networks

Sorting is used for:

- Sorting user IDs
- Sorting friend lists
- Sorting followers
- Sorting posts
- Sorting search results
- Sorting users by follower count
- Sorting recommendation results

Common sorting algorithms include:

- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort
- Merge Sort

For large datasets, efficient algorithms such as Quick Sort and Merge Sort are generally preferred over quadratic-time simple sorting algorithms.

---

# 12. Stability in Sorting

A sorting algorithm is **stable** if equal-key elements maintain their original relative order.

Example:

```text
User A → 500 followers
User B → 500 followers
```

If the sorting algorithm is stable, User A remains before User B when both have the same follower count.

Typical properties:

| Algorithm | Stable? |
|---|---|
| Bubble Sort | Yes |
| Insertion Sort | Yes |
| Selection Sort | Generally No |
| Quick Sort | Generally No |
| Merge Sort | Yes |

Stability can be useful when records have multiple sorting criteria.

---

# 13. Efficiency of Sorting

Efficiency mainly refers to:

- Time complexity
- Space complexity

Example:

| Algorithm | Average Time |
|---|---:|
| Bubble Sort | O(n²) |
| Insertion Sort | O(n²) |
| Selection Sort | O(n²) |
| Quick Sort | O(n log n) |
| Merge Sort | O(n log n) |

For very large social-network datasets, algorithms with approximately `O(n log n)` performance are generally more suitable.

---

# 14. Number of Passes

A pass means one complete iteration over the relevant elements during sorting.

For example, Bubble Sort may require up to:

```text
n - 1 passes
```

For `5` elements, the worst case can require:

```text
4 passes
```

The number of passes affects the total work performed by the algorithm.

---

# 15. Internal and External Sorting

## Internal Sorting

Internal sorting is used when the complete dataset fits in main memory/RAM.

Examples:

- Sorting a small user list
- Sorting a small friend list
- Sorting search results

Algorithms include:

- Quick Sort
- Merge Sort
- Insertion Sort

## External Sorting

External sorting is used when the dataset is too large to fit into RAM.

Large social-network datasets may contain billions of records.

Such data can be stored on secondary storage and processed in blocks.

A common technique is **External Merge Sort**.

Conceptually:

```text
Large Dataset
     |
     v
Split into smaller blocks
     |
     v
Sort individual blocks
     |
     v
Merge sorted blocks
     |
     v
Final sorted dataset
```

---

# 16. Quick Sort in the Case Study

Quick Sort follows the Divide and Conquer strategy.

Steps:

1. Select a pivot.
2. Partition elements around the pivot.
3. Recursively sort the left part.
4. Recursively sort the right part.

### Complexity

- Best/Average: O(n log n)
- Worst: O(n²)

Quick Sort can be useful for sorting user records or search results when an in-memory dataset is being processed.

---

# 17. Merge Sort in the Case Study

Merge Sort also follows Divide and Conquer.

Steps:

1. Divide the data into two halves.
2. Recursively sort both halves.
3. Merge the sorted halves.

### Complexity

```text
Best:    O(n log n)
Average: O(n log n)
Worst:   O(n log n)
```

Merge Sort is especially useful for large datasets and is also the basis of many external sorting approaches.

---

# 18. Python Implementation – Adjacency Matrix

```python
users = ["U1", "U2", "U3", "U4", "U5"]

connections = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0]
]


def check_connection(user1, user2):
    return connections[user1][user2] == 1


print("Social Network Connections:")

for i in range(len(users)):
    print(users[i], ":", connections[i])


print("\nChecking U1 and U2:")

if check_connection(0, 1):
    print("U1 and U2 are friends.")
else:
    print("U1 and U2 are not friends.")
```

### Output

```text
Social Network Connections:
U1 : [0, 1, 1, 0, 0]
U2 : [1, 0, 0, 1, 0]
U3 : [1, 0, 0, 0, 1]
U4 : [0, 1, 0, 0, 1]
U5 : [0, 0, 1, 1, 0]

Checking U1 and U2:
U1 and U2 are friends.
```

---

# 19. Python Implementation – Sparse Matrix

```python
connections = [
    [0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

# 2D triplet representation:
# [row, column, value]
sparse_connections = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 3, 1],
    [2, 4, 1],
    [3, 1, 1],
    [4, 2, 1]
]

print("Existing connections:")

for row, column, value in sparse_connections:
    print(f"User {row} -> User {column} = {value}")
```

### Output

```text
Existing connections:
User 0 -> User 1 = 1
User 1 -> User 0 = 1
User 1 -> User 3 = 1
User 2 -> User 4 = 1
User 3 -> User 1 = 1
User 4 -> User 2 = 1
```

---

# 20. Complexity Analysis

### Normal Adjacency Matrix

For `n` users:

```text
Space = O(n²)
```

Checking whether two users are connected:

```text
connections[i][j]
```

takes:

```text
O(1)
```

### Sparse Representation

If there are `E` actual connections, sparse storage is approximately:

```text
O(E)
```

instead of:

```text
O(n²)
```

when the graph is sparse.

---

# 21. Advantages

1. Simple representation of relationships.
2. Easy to implement using a 2D array.
3. Direct connection checking takes O(1).
4. Easy to understand and visualize.
5. Sparse representation reduces unnecessary zero storage.
6. Searching techniques can be applied to user data.
7. Sorting techniques can organize user records and results.
8. The same concepts can be extended to graph-based applications.

---

# 22. Limitations

1. A normal adjacency matrix requires O(n²) memory.
2. Most entries may be zero in a large social network.
3. Memory consumption becomes extremely high for millions of users.
4. Updating and maintaining a huge matrix can be expensive.
5. A dense matrix is not suitable for most large sparse social networks.

For large sparse graphs, adjacency lists or compressed sparse graph representations are usually more memory-efficient.

---

# 23. Real-World Applications

This case study is applicable to:

- Facebook friendship networks
- Instagram follower networks
- LinkedIn professional connections
- Recommendation systems
- Community detection
- Friend recommendation
- Social network analysis
- Graph-based machine learning
- Network analysis
- Knowledge graphs

---

# 24. Conclusion

A social network can be represented using arrays and graphs.

An adjacency matrix is a 2D array in which rows and columns represent users and the values represent relationships.

For a small number of users, an adjacency matrix is simple and useful. However, for millions of users, a normal matrix requires O(n²) memory and can become impractical.

Because real social networks are usually sparse, sparse matrix or adjacency-list-style representations can save significant memory.

Searching algorithms such as Linear Search, Binary Search, Fibonacci Search, and Indexed Sequential Search help locate user data, while sorting algorithms such as Quick Sort and Merge Sort help organize large datasets efficiently.

Therefore, choosing the correct data structure and algorithm is essential for building scalable social networking systems.
