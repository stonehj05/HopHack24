import streamlit as st
import os

### Example data###
st.session_state.note_text_raw=r"""
# Binary Search Tree

## Summary
This lecture covers the fundamental concepts of binary search trees (BSTs) in data structures. It begins with an overview of binary trees, followed by a detailed explanation of BSTs, including their properties, insertion, and deletion operations. The lecture also touches on the time complexity of these operations and introduces Big-O notation.

## Outline
1. Introduction to Binary Trees
   - Definition and properties
   - Valid and invalid binary trees
2. Binary Search Trees (BST)
   - Definition and properties
   - Use cases and advantages
3. Operations on BST
   - Insertion
   - Deletion
4. Time Complexity
   - Height of the tree
   - Best and worst-case scenarios
5. Big-O Notation
   - Definition and explanation
   - Application to BST operations

## Detailed Notes

### 1. Introduction to Binary Trees
- **Definition**: A binary tree is a tree data structure where each node has at most two children, referred to as the left and right children.
- **Properties**:
  - Each node can have 0, 1, or 2 children.
  - A tree with more than two children per node is not a binary tree.

**Diagram**: [Binary Tree Diagram](https://en.wikipedia.org/wiki/Binary_tree)
- **Description**: Illustrates the structure of two binary trees. The first tree has a root node with two children, each of which has one child. The second tree has a root node with three children, each of which has its own children.
- **Interpretation**: A binary tree is a data structure in which each node has at most two children. The diagrams show examples of binary trees with varying structures.

### 2. Binary Search Trees (BST)
- **Definition**: A binary search tree is a binary tree where the left child of a node contains values less than the parent, and the right child contains values greater than the parent.
- **Properties**:
  - Maintains a sorted order within the tree.
  - Efficient for search, insertion, and deletion operations.

**Diagram**: [Binary Search Tree Diagram](https://en.wikipedia.org/wiki/Binary_search_tree)
- **Description**: Depicts a binary search tree with nodes labeled by numbers. The root node is '9', with its left child '4' and right child '10'. The tree follows the BST property where left children are smaller and right children are larger.
- **Interpretation**: A BST is a binary tree where each node's left child is less than the node and the right child is greater. The diagram shows the comparisons and structure of the BST.

### 3. Operations on BST
#### Insertion
- **Process**:
  1. Start at the root.
  2. Compare the value to be inserted with the current node.
  3. If the value is smaller, go left; if larger, go right.
  4. Repeat until an empty spot is found.
  5. Insert the new value at the empty spot.

**Example**: Inserting 9 into the tree
- 9 < 10 (move to the left child)
- 9 > 4 (move to the right child of 4)
- Inserted at the right child of 4

**Diagram**: [Insertion Process Diagram](https://en.wikipedia.org/wiki/Binary_search_tree)
- **Description**: A diagram showing the process of inserting 9 into a binary search tree.
- **Interpretation**: The insertion process involves comparing the value to be inserted with the current node values and moving left or right accordingly until the correct position is found.

#### Deletion
- **Process**:
  1. Find the node to delete.
  2. If the node has no children, remove it.
  3. If the node has one child, reconnect that child to the parent of the node being deleted.
  4. If the node has two children, replace the node with its in-order successor or predecessor and reconnect the tree.

**Example**: Deleting a node with value 10
- If 10 has no children, remove it.
- If 10 has one child, replace 10 with that child.
- If 10 has two children, find the in-order successor (smallest value in the right subtree) and replace 10 with that value.

### 4. Time Complexity
- **Height of the Tree**: The time complexity of insertion and deletion operations is proportional to the height of the tree.
- **Best Case**: When the tree is balanced, the height is logarithmic with respect to the number of nodes, i.e., \( O(\log n) \).
- **Worst Case**: When the tree is unbalanced (e.g., a linked list structure), the height is equal to the number of nodes, i.e., \( O(n) \).

### 5. Big-O Notation
- **Definition**: Big-O notation describes the upper bound of an algorithm's time complexity, indicating the worst-case scenario for how long an operation will take as the input set grows.
- **Mathematical Formulation**:
  \[
  f(n) = O(g(n)) \iff \exists C, N_0 \in \mathbb{R}, \text{ s.t. } \forall N \geq N_0, |f(N)| \leq C \cdot g(N)
  \]
- **Application to BST Operations**: For a balanced BST, the time complexity for insert or delete operations is \( O(\log n) \), as the number of operations needed is proportional to the height of the tree.

**Diagram**: [Big-O Notation Diagram](https://en.wikipedia.org/wiki/Big_O_notation)
- **Description**: Provides a formal definition of Big-O notation, stating that a function \( f(n) \) is \( O(g(n)) \) if there exist constants \( C \) and \( N_0 \) such that for all \( N \geq N_0 \), the absolute value of \( f(N) \) is at most \( C \) times \( g(N) \).
- **Interpretation**: Big-O notation is used to describe the upper bound of an algorithm's runtime or space requirements. The definition provides the mathematical formulation for this concept.

## Diagrams & Related Resources
- [Binary Tree Diagram](https://en.wikipedia.org/wiki/Binary_tree)
- [Binary Search Tree Diagram](https://en.wikipedia.org/wiki/Binary_search_tree)
- [Big-O Notation Diagram](https://en.wikipedia.org/wiki/Big_O_notation)
"""

st.session_state.question_list=[
        {
            "topic": "Introduction to Binary Trees@Definition and properties",
            "tag": "Conceptual",
            "question": "What is a binary tree?",
            "answer": "A binary tree is a tree structure where each node has at most two children, commonly referred to as the left and right children."
        },
        {
            "topic": "Introduction to Binary Trees@Definition and properties",
            "tag": "Easy",
            "question": "Can a binary tree have a node with three children?",
            "answer": "No, a binary tree cannot have a node with three children. Each node can have at most two children."
        },
        {
            "topic": "Introduction to Binary Trees@Definition and properties",
            "tag": "Challenging",
            "question": "Why is it incorrect to classify a tree with a root node having three children as a binary tree?",
            "hint": "Consider the definition of a binary tree and the constraints on the number of children each node can have.",
            "answer": "It is incorrect to classify such a tree as a binary tree because, by definition, a binary tree is limited to having each node with at most two children. A node with three children violates this property."
        },
        {
            "topic": "Binary Search Trees (BST)@Definition and properties",
            "tag": "Conceptual",
            "question": "What is the main distinction between a binary tree and a binary search tree?",
            "answer": "The main distinction is that in a binary search tree, the left child of a node contains values that are less than the parent, and the right child contains values that are greater than the parent."
        },
        {
            "topic": "Binary Search Trees (BST)@Definition and properties",
            "tag": "Easy",
            "question": "Why are binary search trees efficient for search operations?",
            "answer": "Binary search trees are efficient for search operations because their structure maintains a sorted order, allowing for quick lookups by navigating left or right based on value comparisons."
        },
        {
            "topic": "Binary Search Trees (BST)@Definition and properties",
            "tag": "Challenging",
            "question": "How does the property of binary search trees contribute to their efficiency in dynamic data operations?",
            "hint": "Think about how the ordering of nodes affects the ease of insertion, deletion, and search operations.",
            "answer": "The property of binary search trees ensures that for any node, all values in the left subtree are smaller and all values in the right subtree are larger. This sorted order allows for efficient insertion, deletion, and search operations, as it reduces the number of comparisons needed to find the appropriate location for any operation."
        },
        {
            "topic": "Operations on BST@Insertion",
            "tag": "Conceptual",
            "question": "What is the basic process for inserting a value into a binary search tree?",
            "answer": "The basic process for inserting a value into a binary search tree involves starting at the root, comparing the value to the current node, and moving left if the value is smaller or right if it is larger. This process is repeated until an empty spot is found, where the new value is then inserted."
        },
        {
            "topic": "Operations on BST@Insertion",
            "tag": "Easy",
            "question": "Where would you insert the value 9 if the root of the binary search tree has a value of 15?",
            "answer": "Since 9 is smaller than 15, you would move to the left child of the root to continue the insertion process."
        },
        {
            "topic": "Operations on BST@Insertion",
            "tag": "Challenging",
            "question": "What are the potential issues if the values are always inserted in increasing order in a binary search tree, and how might this affect performance?",
            "hint": "Consider the structure of the tree if each new value is larger than the previous ones.",
            "answer": "If values are always inserted in increasing order, the binary search tree can degrade into a structure similar to a linked list, where each node has only a right child. This leads to an unbalanced tree with a height equal to the number of nodes, significantly affecting performance by increasing the time complexity of operations to O(n)."
        },
        {
            "topic": "Operations on BST@Deletion",
            "tag": "Conceptual",
            "question": "What are the steps involved in deleting a node with two children in a binary search tree?",
            "answer": "When deleting a node with two children, you replace the node with its in-order successor (the smallest value in the right subtree) or predecessor (the largest value in the left subtree), and then reconnect the tree to maintain the binary search property."
        },
        {
            "topic": "Operations on BST@Deletion",
            "tag": "Easy",
            "question": "What is the in-order successor of a node in a binary search tree?",
            "answer": "The in-order successor of a node is the smallest value in its right subtree."
        },
        {
            "topic": "Operations on BST@Deletion",
            "tag": "Challenging",
            "question": "Why is it necessary to use the in-order successor or predecessor when deleting a node with two children in a binary search tree?",
            "hint": "Think about maintaining the binary search tree properties after deletion.",
            "answer": "Using the in-order successor or predecessor when deleting a node with two children ensures that the tree remains correctly ordered. This replacement maintains the binary search tree property that all values in the left subtree are less than the parent node and all values in the right subtree are greater."
        },
        {
            "topic": "Time Complexity@Height of the tree",
            "tag": "Conceptual",
            "question": "How is the height of a binary search tree related to its time complexity for insertion and deletion operations?",
            "answer": "The height of a binary search tree is directly related to its time complexity for insertion and deletion operations. In the best case, when the tree is balanced, the height is logarithmic in the number of nodes, resulting in O(log n) time complexity. However, if the tree is unbalanced, the height can be linear in the number of nodes, leading to O(n) time complexity."
        },
        {
            "topic": "Time Complexity@Height of the tree",
            "tag": "Easy",
            "question": "What is the time complexity for insertion in a balanced binary search tree?",
            "answer": "The time complexity for insertion in a balanced binary search tree is O(log n)."
        },
        {
            "topic": "Time Complexity@Height of the tree",
            "tag": "Challenging",
            "question": "What might cause the time complexity of operations in a binary search tree to degrade from O(log n) to O(n), and how can this issue be addressed?",
            "hint": "Consider the tree structure when values are inserted in a specific order.",
            "answer": "The time complexity degrades from O(log n) to O(n) when the binary search tree becomes unbalanced, such as when values are inserted in strictly increasing or decreasing order, causing the tree to resemble a linked list. This issue can be addressed by using balancing techniques, such as AVL trees or red-black trees, which ensure the tree remains balanced and maintains O(log n) time complexity for operations."
        },
        {
            "topic": "Big-O Notation@Definition and explanation",
            "tag": "Conceptual",
            "question": "What does Big-O notation describe in terms of algorithm performance?",
            "answer": "Big-O notation describes the upper bound of an algorithm's time complexity, giving an idea of the worst-case scenario for how long an operation will take as the input set grows."
        },
        {
            "topic": "Big-O Notation@Definition and explanation",
            "tag": "Easy",
            "question": "What does O(log n) time complexity indicate about the growth rate of an algorithm's running time?",
            "answer": "O(log n) time complexity indicates that the running time of the algorithm increases logarithmically as the input size grows, meaning it increases more slowly compared to linear growth."
        },
        {
            "topic": "Big-O Notation@Definition and explanation",
            "tag": "Challenging",
            "question": "Explain why the time complexity for operations in a balanced binary search tree is O(log n) using Big-O notation and the concept of tree height.",
            "hint": "Consider the relationship between tree height and the number of nodes in a balanced binary search tree.",
            "answer": "In a balanced binary search tree, the height of the tree is logarithmic with respect to the number of nodes, meaning the height is approximately log2(n). Since operations like insertion, deletion, and search depend on the height of the tree, the time complexity for these operations is proportional to the height. Therefore, using Big-O notation, the time complexity is described as O(log n), reflecting that the number of operations needed grows logarithmically with the number of nodes."
        }
    ]



# Set page configuration
st.set_page_config(page_title="Notebook Page", layout="wide")

# Title stored in session state
if 'lecture_name' not in st.session_state:
    st.session_state.lecture_name = "STUB NAME"
st.title(st.session_state.lecture_name)

# Create columns for diagrams and questions
col1, col2 = st.columns([2, 1])

# LEFT COLUMN (Notebook content)
with col1:
    st.header("Notebook Content")
    if 'note_text_raw' in st.session_state:
        st.markdown(st.session_state.note_text_raw)
        #TODO: Add Diagrams picture inside the notes under appropiate section.
        # if 'diagram_list' in st.session_state:
        #     for diagram in st.session_state['diagram_list']:
        #         st.image(diagram['image_path'], caption=f"Diagram for {diagram['topic']}")
        #     else:
        #         st.info("No diagrams available.")
    else:
        st.write("No notes available. Please upload the markdown file.")

# RIGHT COLUMN (Diagrams and Questions)
with col2:
    st.header("Self-Quiz")

    # Display diagrams (images) if available


    # Display questions in tabs if available
    if 'question_list' in st.session_state:
        st.header("Interactive Questions")
        
        for question_data in st.session_state.question_list:
            topic = question_data['topic']
            st.subheader(f"Questions for {topic}")

            # Create tabs for Conceptual, Easy, and Challenging questions
            tab1, tab2, tab3 = st.tabs(["Conceptual", "Easy", "Challenging"])
            
            with tab1:
                for question in question_data['question']:
                    if question['tag'] == "Conceptual":
                        st.write(f"**Question**: {question['question']}")
                        st.text_input("Your answer:", key=f"{topic}_conceptual")
                        if 'hint' in question and question['hint']:
                            st.write(f"**Hint**: {question['hint']}")

            with tab2:
                for question in question_data['question']:
                    if question['tag'] == "Easy":
                        st.write(f"**Question**: {question['question']}")
                        st.text_input("Your answer:", key=f"{topic}_easy")
                        if 'hint' in question and question['hint']:
                            st.write(f"**Hint**: {question['hint']}")

            with tab3:
                for question in question_data['question']:
                    if question['tag'] == "Challenging":
                        st.write(f"**Question**: {question['question']}")
                        st.text_input("Your answer:", key=f"{topic}_challenging")
                        if 'hint' in question and question['hint']:
                            st.write(f"**Hint**: {question['hint']}")

    else:
        st.info("No questions available.")

# Footer
st.markdown("---")
st.metric(label="Progress", value="50%", delta="5%")

# Add some interactivity to stop the execution
if st.button("Stop the process"):
    st.stop()

st.success('Page Loaded Successfully!')

# Function to process notes and get variables into session state
def generate_new_notes():
    pass  # Replace with logic for loading new notes
