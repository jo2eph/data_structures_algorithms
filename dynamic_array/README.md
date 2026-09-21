# Dynamic Array

---

## Motivation

- Arrays
  - Data are placed contiguously in memory
  - Access time $O(1)$
  - The problem with array is that once the array is full and we need to insert new data, we need to find new chunk of memory and then copy values over, which is $O(n)$

- Linked Lists
  - Data are not stored contiguously in memory
  - Nodes are linked and do not need to be next to each other in memory
  - If a linked list has a tail pointer, then appending to end of list is $O(1)$

- Can we get the best of both worlds?
  - $O(1)$ access like an array
  - $O(1)$ append like a linked list
  - Yes (sort of), and that's where **dynamic arrays** come in

---

## Dynamic Arrays: The Idea



---
