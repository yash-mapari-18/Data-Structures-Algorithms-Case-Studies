# Dictionary Application Using Hash Tables

## SPPU - Second Year Computer Engineering (2024 Pattern)
### PCC-201-COM: Data Structures
### Unit IV - Hashing

## Case Study

**Dictionary Application using Hash Tables**

Implement a dictionary where words and meanings are stored and retrieved
using hashing with collision resolution.

---

## 1. Objective

The objective of this case study is to implement a simple dictionary
application using a hash table. The application stores words as keys
and their meanings as values.

The application demonstrates how hashing can provide efficient
insertion, searching, updating, and deletion of dictionary entries.

---

## 2. Problem Statement

A dictionary contains a large number of words and their meanings.
Searching through all words sequentially can become inefficient.

To solve this problem, a hash table is used to map each word to a
bucket using a hash function. If multiple words map to the same
bucket, a collision occurs. This implementation resolves collisions
using **separate chaining**.

---

## 3. Data Structure Used

### Hash Table

A hash table stores data in an array of buckets.

Each dictionary entry contains:

- **Key:** Word
- **Value:** Meaning

Example:

```text
apple  -> A fruit
book   -> A collection of pages
car    -> A road vehicle
```

---

## 4. Hash Function

The program calculates the hash value using the ASCII/Unicode value
of every character in the word.

```text
hash_value = sum(ord(character))
index = hash_value % table_size
```

For example, the characters of a word are converted into numeric
values, added together, and reduced to a valid bucket index using the
modulo operation.

---

## 5. Collision Resolution

### Separate Chaining

If two different words produce the same bucket index, both entries
are stored in the same bucket using a list.

Example:

```text
Bucket 4 -> [cat: Animal] -> [dog: Animal]
```

Here, `cat` and `dog` are different keys but have the same hash index.
This is a **collision**.

The list attached to the bucket is called a chain.

---

## 6. Operations Implemented

### Insert

Adds a new word and its meaning to the hash table.

If the word already exists, its meaning is updated.

### Search

Calculates the hash index of the word and searches the corresponding
bucket/chain.

### Delete

Removes the word and its meaning from the hash table.

### Display

Displays every bucket and its contents.

---

## 7. Algorithm

### Insert Algorithm

1. Accept a word and its meaning.
2. Calculate the hash value of the word.
3. Calculate the bucket index.
4. Search the chain at that index.
5. If the word already exists, update its meaning.
6. Otherwise, add the word and meaning to the chain.

### Search Algorithm

1. Accept the word to search.
2. Calculate its hash value.
3. Find the corresponding bucket.
4. Traverse the chain.
5. If the word is found, return its meaning.
6. Otherwise, display "Word not found".

### Delete Algorithm

1. Accept the word to delete.
2. Calculate its hash value.
3. Find the corresponding bucket.
4. Search the chain.
5. Remove the word if found.

---

## 8. Complexity Analysis

| Operation | Average Case | Worst Case |
|---|---:|---:|
| Insert | O(1) | O(n) |
| Search | O(1) | O(n) |
| Delete | O(1) | O(n) |

Average-case performance is O(1) when the hash function distributes
keys uniformly and the load factor is controlled.

In the worst case, many keys can collide and form a long chain, making
the operation O(n).

---

## 9. Concepts Demonstrated

This case study demonstrates the following Unit IV concepts:

- Hash table
- Hash function
- Bucket
- Collision
- Synonym
- Separate chaining
- Open hashing
- Basic hash table operations
- Efficient search and insertion

---

## 10. Technologies Used

- Python 3
- Standard Python library only

---

## 11. How to Run

Make sure Python 3 is installed.

Run:

```bash
python dictionary.py
```

The application provides a menu for:

```text
1. Insert Word
2. Search Word
3. Delete Word
4. Display Hash Table
5. Exit
```

---

## 12. Sample Entries

You can test the application with:

```text
apple     -> A fruit
book      -> A collection of pages
computer  -> An electronic programmable machine
python    -> A high-level programming language
```

---

## 13. Conclusion

The Dictionary Application demonstrates the practical use of hash
tables for storing and retrieving key-value pairs efficiently.

A hash function maps each word to a bucket, while separate chaining
handles collisions when multiple words map to the same bucket.

Thus, hashing provides an efficient approach for implementing the
core operations of a dictionary application.
