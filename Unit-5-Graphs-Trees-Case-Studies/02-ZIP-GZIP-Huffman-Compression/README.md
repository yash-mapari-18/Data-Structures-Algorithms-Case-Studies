# ZIP/GZIP Style File Compression Using Huffman Tree

## SPPU - Second Year Computer Engineering (2024 Pattern)
### PCC-201-COM: Data Structures
### Unit V - Graphs and Trees

## Case Study

ZIP/GZIP-style compression can use **frequency-based encoding**.
Huffman coding assigns shorter binary codes to frequently occurring
characters and longer codes to less frequent characters.

This case study implements Huffman coding using a binary tree.

## Working

1. Count the frequency of every character.
2. Create a node for every character.
3. Insert nodes into a min-heap according to frequency.
4. Remove the two nodes with the smallest frequencies.
5. Merge them into a new internal node.
6. Repeat until one root node remains.
7. Traverse the tree:
   - Left edge = 0
   - Right edge = 1
8. Replace each character with its Huffman code.
9. Decode the encoded data using the same tree.

## Example

For a text with frequent `a` characters, `a` can receive a shorter
code than a character that appears rarely.

The exact codes depend on the input frequencies.

## Complexity

Let `n` be the number of characters in the input and `k` be the number
of distinct characters.

- Frequency counting: O(n)
- Building Huffman tree: O(k log k)
- Encoding: O(n)
- Decoding: O(encoded bit count)

## Important Note

This is an educational implementation of the **Huffman coding technique
used in the syllabus case study**. It demonstrates the core algorithm;
it does not attempt to reproduce the complete ZIP or GZIP file format,
which includes additional headers, metadata, checksums and compression
details.

## How to Run

```bash
python huffman_compression.py
```

Enter a text such as:

```text
data structures and algorithms
```

The program displays:

- Character frequencies
- Huffman codes
- Encoded bit sequence
- Original size
- Encoded size
- Decoded text
- Verification result

## Conclusion

Huffman coding demonstrates how a frequency-based binary tree can be
used for lossless data compression. More frequent characters generally
receive shorter codes, reducing the number of bits needed to represent
the input.
