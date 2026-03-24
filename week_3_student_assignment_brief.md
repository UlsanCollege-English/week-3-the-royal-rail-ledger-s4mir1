# Week 3 Assignment: The Royal Rail Ledger

## Summary
This project implements several operations on singly linked lists and doubly linked lists to simulate railway cargo tracking.

The program builds linked lists from Python lists, converts linked lists back into Python lists, detects repeated cargo values, removes banned cargo from doubly linked lists, and checks whether a train forms a palindrome when read from both ends.

All functions are implemented using standard Python libraries and follow the provided class structures.

---

## Approach

### Task 1 — Build Singly Linked List
To build a singly linked list, I:
1. Created an empty `SinglyLinkedList`
2. Iterated through the input Python list
3. Created a new node for each value
4. Connected nodes by updating `next` pointers
5. Set the first node as the head

### Task 2 — Convert Singly Linked List to Python List
To convert the linked list back:
1. Started from the head node
2. Traversed node-by-node using the `next` pointer
3. Added each value to a Python list
4. Returned the final list

### Task 3 — Find First Repeated Value
To find the first repeated cargo code:
1. Traversed the list from head to tail
2. Stored previously seen values in a set
3. If a value appeared again, returned it immediately
4. Returned `None` if no repeats were found

This ensures the *first repeat encountered* is returned rather than the most frequent value.

### Task 4 — Remove All Banned Cargo (DLL)
To remove all nodes with a target value:
1. Traversed the doubly linked list
2. If a node matched the target:
   - Updated the previous node’s `next` pointer
   - Updated the next node’s `prev` pointer
   - Updated `head` if removing the first node
   - Updated `tail` if removing the last node
3. Continued traversal safely using a saved next pointer

### Stretch Task — Palindrome Check
To check if the train is a palindrome:
1. Used two pointers:
   - One starting from the head
   - One starting from the tail
2. Compared values while moving inward
3. If values differed, returned `False`
4. If all matched, returned `True`

---

## Complexity

| Task | Time Complexity | Space Complexity |
|------|-----------------|------------------|
| Build SLL | O(n) | O(n) |
| SLL → List | O(n) | O(n) |
| First Repeat | O(n) | O(n) |
| Remove from DLL | O(n) | O(1) |
| Palindrome DLL | O(n) | O(1) |

*n = number of nodes*

---

## Edge-Case Checklist

This program correctly handles:

- Empty singly linked list
- Empty doubly linked list
- Single-node lists
- Repeated values
- Removing from the head
- Removing from the tail
- Removing consecutive matching values
- Removing all nodes from a list
- Palindromes with even number of nodes
- Palindromes with odd number of nodes

---

## Assistance & Sources

**Course Materials**
- Lecture slides on linked lists
- In-class coding exercises
- Assignment specification

**Python Documentation**
- Official Python documentation for sets and classes

**Debugging Tools**
- pytest
- Print-based debugging
- Drawing pointer diagrams by hand

No external libraries were used beyond the Python standard library.