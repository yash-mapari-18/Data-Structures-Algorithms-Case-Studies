# Case Study: E-Commerce Product Sorting using Divide and Conquer Strategy

## 1. Introduction
E-commerce websites contain thousands or millions of products. Users may want to sort products by price, rating, discount, popularity, or reviews. Divide and Conquer provides an efficient approach for sorting large datasets.

## 2. Problem Statement
Sort a large list of product prices from lowest to highest.

**Input:** `60000, 25000, 2000, 1500, 15000, 5000, 1000, 30000`

**Output:** `1000, 1500, 2000, 5000, 15000, 25000, 30000, 60000`

## 3. Objective
- Sort a large number of products efficiently.
- Apply Divide and Conquer.
- Reduce sorting time.
- Improve user experience.

## 4. Divide and Conquer
The strategy has three steps:
1. **Divide:** Split the array into smaller parts.
2. **Conquer:** Recursively sort each part.
3. **Combine:** Merge the sorted parts.

## 5. Algorithm: Merge Sort
```text
MERGE_SORT(array)
1. If array has 0 or 1 element, return it.
2. Find the middle.
3. Divide into left and right halves.
4. Recursively sort both halves.
5. Merge the sorted halves.
6. Return the result.
```

## 6. Example
`[60000, 25000, 2000, 1500]`

Divide:
`[60000, 25000] [2000, 1500]`

Divide again:
`[60000] [25000] [2000] [1500]`

Sort:
`[25000, 60000] [1500, 2000]`

Merge:
`[1500, 2000, 25000, 60000]`

## 7. Python Implementation
See `merge_sort.py`.

## 8. Output
```text
Original Prices:
[60000, 25000, 2000, 1500, 15000, 5000, 1000, 30000]

Sorted Prices:
[1000, 1500, 2000, 5000, 15000, 25000, 30000, 60000]
```

## 9. Complexity Analysis
| Case | Time |
|---|---|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |

Space Complexity: **O(n)**

## 10. Real-World Applications
- Product price sorting
- Rating sorting
- Discount sorting
- Popularity sorting
- Review-count sorting

## 11. Conclusion
Merge Sort uses Divide and Conquer to efficiently sort large product datasets. Its time complexity is O(n log n), making it suitable for large e-commerce datasets.
