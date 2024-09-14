```markdown
# Binary Search Tree

## Summary
This lecture covers the fundamental concepts of binary trees and binary search trees (BSTs), including their structure, properties, and operations such as insertion and deletion. Additionally, the lecture delves into the time complexity of these operations using Big O notation.

## Outline
1. Introduction to Binary Trees
2. Binary Search Trees (BSTs)
3. Insert Operation in BSTs
4. Delete Operation in BSTs
5. Time Complexity and Big O Notation

## Detailed Notes

### 1. Introduction to Binary Trees
- **Definition**: A binary tree is a type of data structure in which each node has at most two children. These children are referred to as the left child and the right child.
- **Valid Binary Tree**:
  ```
      O
     / \
    O   O
  ```
  This diagram represents a valid binary tree where each node has at most two children.
- **Invalid Binary Tree**:
  ```
      O
     /|\
    O O O
  ```
  This diagram represents an invalid binary tree where a node has more than two children.

### 2. Binary Search Trees (BSTs)
- **Definition**: A binary search tree is a binary tree where each node follows the left < root < right property. The left child of a node contains values that are less than the parent, and the right child contains values that are greater than the parent.
- **Example**:
  ```
      10
     /  \
    4    20
   / \   / \
  2   9 15  25
  ```
  In this example, all nodes in the left subtree of 10 have values smaller than 10, and all nodes in the right subtree have values larger than 10.

### 3. Insert Operation in BSTs
- **Steps to Insert a Node**:
  1. Start at the root.
  2. Compare the value to be inserted with the current node's value.
     - If it is less, go to the left child.
     - If it is greater, go to the right child.
  3. Repeat the process until you find the correct position, and insert the node there.
- **Example**: Inserting 9 into the tree:
  ```
      10
     /  \
    4    O
   / \  / \
  O  9 O  O
  ```
  This diagram shows the process of inserting the value 9 into a binary search tree.

### 4. Delete Operation in BSTs
- **Steps to Delete a Node**:
  1. **Step 1**: Start at the root and find the node to delete.
     - Use the same process as the insertion to locate the node.
  2. **Step 2**:
     - If the node has no children, simply remove it.
     - If the node has one child, reconnect that child to the parent of the node you are deleting.
     - If the node has two children, find the in-order successor (smallest node in the right subtree), replace the node with the in-order successor, and delete the in-order successor from its original position.

### 5. Time Complexity and Big O Notation
- **Big O Notation**: Used to describe the upper bound of the time complexity of an algorithm. It provides an asymptotic analysis of the algorithm's performance.
  - **Definition**:
    \[
    f(n) = O(g(n)) \Leftrightarrow \exists C, N_0 \in \mathbb{R}, \text{ s.t. } \forall N \geq N_0, |f(N)| \leq C \cdot g(N)
    \]
- **Time Complexity of BST Operations**:
  - **Insertion and Deletion**: The time it takes is proportional to the height of the tree.
    - **Best Case**: When the tree is balanced, the height of the tree is logarithmic with respect to the number of nodes, i.e., \( O(\log n) \).
    - **Worst Case**: If the tree becomes unbalanced, the height of the tree can be equal to the number of nodes, i.e., \( O(n) \).

### Diagrams
1. **Binary Tree**:
   - [Binary tree with nodes having up to two children](https://en.wikipedia.org/wiki/Binary_tree)
2. **Binary Search Tree**:
   - [Binary search tree with numerical values as nodes](https://en.wikipedia.org/wiki/Binary_search_tree)
3. **Big O Notation**:
   - [Definition and explanation of Big-O notation](https://en.wikipedia.org/wiki/Big_O_notation)

## Summary
A binary search tree is a binary tree where each node follows the left < root < right property. Insertion and deletion operations involve traversing the tree to find the correct position or node. Understanding the time complexity using Big O notation is crucial for analyzing the efficiency of these operations.
```