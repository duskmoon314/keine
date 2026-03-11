---
title: "Quicksort"
description: "Quicksort partitions data around a pivot and recursively sorts the resulting subarrays."
tags: ["algorithms", "sorting", "comparison-sort", "divide-and-conquer"]
source: "https://www.nist.gov/dads/HTML/quicksort.html"
source_type: "url"
---
# Quicksort

## Summary
Quicksort is a divide-and-conquer sorting algorithm. It chooses a pivot, partitions the remaining elements into values smaller and larger than that pivot, and then recursively sorts the two sides. Its worst case is quadratic, but well-engineered versions are usually very fast in practice and are among the most important general-purpose sorting techniques.

## Content
### How it works
At a high level, quicksort repeats the same pattern:

1. Choose a pivot element.
2. Rearrange the array so elements smaller than the pivot go to one side and larger elements go to the other side.
3. Recursively sort the left partition.
4. Recursively sort the right partition.

The partition step is the key idea. Once partitioning finishes, the pivot is in its final position, so the algorithm only needs to sort the two smaller subproblems.

### Complexity and properties
- Typical running time is `O(n log n)`.
- Worst-case running time is `Theta(n^2)` if the partitions are repeatedly very unbalanced.
- Many practical implementations are in place or nearly in place.
- Real performance depends heavily on pivot choice, partition strategy, and when the implementation switches to a simpler algorithm for tiny subarrays.

### When to use it
Quicksort is often the fastest of these three algorithms on larger unsorted arrays. It is a strong default when average-case speed matters and the implementation is tuned carefully, for example by choosing pivots well or randomizing them. In practice, many library or textbook implementations combine quicksort with insertion sort so that tiny partitions are handled by the simpler algorithm.

## Related
- [Bubble Sort](./2026-03-11-bubble-sort.md)
- [Insertion Sort](./2026-03-11-insertion-sort.md)
- [algorithms tag](./tags/algorithms.md)
- [sorting tag](./tags/sorting.md)
- [divide-and-conquer tag](./tags/divide-and-conquer.md)
