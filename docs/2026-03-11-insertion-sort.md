---
title: "Insertion Sort"
description: "Insertion sort grows a sorted prefix by inserting each new element into the correct position."
tags: ["algorithms", "sorting", "comparison-sort"]
source: "https://www.nist.gov/dads/HTML/insertionSort.html"
source_type: "url"
---
# Insertion Sort

## Summary
Insertion sort builds a sorted region one element at a time. For each new element, it finds where that element belongs among the items already seen, shifts larger items to the right, and inserts the element into the gap. People sometimes say "insert sort" informally, but the standard name is insertion sort.

## Content
### How it works
The algorithm treats the left side of the array as already sorted:

1. Start with the first element as a sorted prefix of length one.
2. Take the next element.
3. Scan left through the sorted prefix until you find the correct position.
4. Shift larger elements right and insert the element.
5. Repeat until all elements have been inserted.

This makes insertion sort feel natural if you imagine sorting playing cards in your hand: each new card is inserted into the right spot among the cards already ordered.

### Complexity and properties
- Running time is `O(n^2)` in the general case because elements may need many moves.
- It performs well on small inputs.
- It is also a good fit when the data is already nearly sorted, because each element only needs a short move.
- A common implementation works in place with very little extra memory.

### When to use it
Insertion sort is much more practical than bubble sort for tiny collections or nearly sorted data. It also appears inside hybrid sorting implementations: a faster large-input algorithm handles big partitions, then insertion sort finishes the small ones because its constant factors are low and the code is simple.

## Related
- [Bubble Sort](./2026-03-11-bubble-sort.md)
- [Quicksort](./2026-03-11-quicksort.md)
- [algorithms tag](./tags/algorithms.md)
- [sorting tag](./tags/sorting.md)
