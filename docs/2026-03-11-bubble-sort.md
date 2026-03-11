---
title: "Bubble Sort"
description: "Bubble sort repeatedly swaps adjacent out-of-order elements until a full pass finishes with no swaps."
tags: ["algorithms", "sorting", "comparison-sort"]
source: "https://www.nist.gov/dads/HTML/bubblesort.html"
source_type: "url"
---
# Bubble Sort

## Summary
Bubble sort is a simple comparison-based sorting algorithm. It repeatedly scans a list, compares neighboring elements, and swaps them when they are in the wrong order. It is easy to understand, but it is usually too slow for large inputs, so it is mainly useful for teaching and small toy examples.

## Content
### How it works
Think of the algorithm as making passes from left to right through the array:

1. Compare each adjacent pair.
2. Swap the pair if they are out of order.
3. Continue until the end of the array.
4. Repeat the whole pass until a pass makes no swaps.

After each pass, at least one element reaches its final position. In the common ascending-order version, larger values tend to move toward the end of the array, which is where the "bubble" intuition comes from.

### Complexity and properties
- General running time is `O(n^2)`.
- If the data is already almost sorted and the implementation stops early when no swaps occur, performance can approach linear time.
- Bubble sort is in-place, so it does not need much extra memory.
- Bubble sort is stable, so equal items can keep their relative order.

### When to use it
Bubble sort is mostly a learning algorithm. It helps explain ideas like comparisons, swaps, passes, and stability, but it is rarely the right production choice when the input can be even moderately large. If you need a simple algorithm that performs better on small or nearly sorted data, insertion sort is usually more useful.

## Related
- [Insertion Sort](./2026-03-11-insertion-sort.md)
- [Quicksort](./2026-03-11-quicksort.md)
- [algorithms tag](./tags/algorithms.md)
- [sorting tag](./tags/sorting.md)
