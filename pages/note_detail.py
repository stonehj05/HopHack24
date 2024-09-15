import streamlit as st
import os
from file_handle import *
import json
from generate_note import generate_note

### LOAD DATA ###
blackboard_file = st.session_state.blackboard_file
course_name = st.session_state.currentCourse
note_name = st.session_state.menu[st.session_state.currentCourse][st.session_state.currentNodeIndex]
syllabus_file = st.session_state.syllabusList[course_name]
audio_file = st.session_state.audio_file
personal_file = st.session_state.personal_file
note_name = "1" #for test purposes
note_path = f"../data/{course_name}/{note_name}"
if not os.path.exists(os.path.join(note_path, "note.md")):
    syllabus_content = read_syllabus(syllabus_file.name, course_name)
    blackboard_images = read_blackboard(blackboard_file.name, course_name, note_name)
    handnote_images = read_handnote(personal_file.name, course_name, note_name)
    audio_file_path = os.path.join(os.getcwd(), "data", course_name, note_name, audio_file.name)
    generate_note(blackboard_images, audio_file_path, handnote_images, context=syllabus_content, course_name=course_name, lecture_name=note_name)
with open(f"./data/{course_name}/{note_name}/questions.json", "r") as file:
    questions = json.load(file)
with open(f"./data/{course_name}/{note_name}/note.md", "r") as file:
    note = file.read()

st.session_state.note_text_raw=note

st.session_state.question_list=questions

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
- **Best Case**: When the tree is balanced, the height is logarithmic with respect to the number of nodes, i.e., $\( O(\log n) \)$.
- **Worst Case**: When the tree is unbalanced (e.g., a linked list structure), the height is equal to the number of nodes, i.e., $\( O(n) \)$.

### 5. Big-O Notation
- **Definition**: Big-O notation describes the upper bound of an algorithm's time complexity, indicating the worst-case scenario for how long an operation will take as the input set grows.
- **Mathematical Formulation**: $\iff 1+1=2$
  $[ f(n) = O(g(n)) \iff \exists C, N_0 \in \mathbb{R}, \text{ s.t. } \forall N \geq N_0, |f(N)| \leq C \cdot g(N) ]$
  
- **Application to BST Operations**: For a balanced BST, the time complexity for insert or delete operations is $\( O(\log n) \)$, as the number of operations needed is proportional to the height of the tree.

**Diagram**: [Big-O Notation Diagram](https://en.wikipedia.org/wiki/Big_O_notation)
- **Description**: Provides a formal definition of Big-O notation, stating that a function $( f(n) )$ is $( O(g(n)) )$ if there exist constants $\( C \)$ and $\( N_0 \)$ such that for all $\( N \geq N_0 \)$, the absolute value of $\( f(N) \)$ is at most $\( C \)$ times $\( g(N) \)$.
- **Interpretation**: Big-O notation is used to describe the upper bound of an algorithm's runtime or space requirements. The definition provides the mathematical formulation for this concept.

## Diagrams & Related Resources
- [Binary Tree Diagram](https://en.wikipedia.org/wiki/Binary_tree)
- [Binary Search Tree Diagram](https://en.wikipedia.org/wiki/Binary_search_tree)
- [Big-O Notation Diagram](https://en.wikipedia.org/wiki/Big_O_notation)
"""
st.session_state.note_partition_dict = {
    "Introduction to Binary Trees": {
        "Definition and properties": "- **Definition**: A binary tree is a tree data structure where each node has at most two children, referred to as the left and right children.\n- **Properties**:\n- Each node can have 0, 1, or 2 children.\n- A tree with more than two children per node is not a binary tree.\n\n**Diagram**: [Binary Tree Diagram](https://en.wikipedia.org/wiki/Binary_tree)\n- **Description**: Illustrates the structure of two binary trees. The first tree has a root node with two children, each of which has one child. The second tree has a root node with three children, each of which has its own children.\n- **Interpretation**: A binary tree is a data structure in which each node has at most two children. The diagrams show examples of binary trees with varying structures."
    },
    "Binary Search Trees (BST)": {
        "Definition and properties": "- **Definition**: A binary search tree is a binary tree where the left child of a node contains values less than the parent, and the right child contains values greater than the parent.\n- **Properties**:\n- Maintains a sorted order within the tree.\n- Efficient for search, insertion, and deletion operations.\n\n**Diagram**: [Binary Search Tree Diagram](https://en.wikipedia.org/wiki/Binary_search_tree)\n- **Description**: Depicts a binary search tree with nodes labeled by numbers. The root node is '9', with its left child '4' and right child '10'. The tree follows the BST property where left children are smaller and right children are larger.\n- **Interpretation**: A BST is a binary tree where each node's left child is less than the node and the right child is greater. The diagram shows the comparisons and structure of the BST."
    },
    "Operations on BST": {
        "Insertion": "- **Process**:\n1. Start at the root.\n2. Compare the value to be inserted with the current node.\n3. If the value is smaller, go left; if larger, go right.\n4. Repeat until an empty spot is found.\n5. Insert the new value at the empty spot.\n\n**Example**: Inserting 9 into the tree\n- 9 < 10 (move to the left child)\n- 9 > 4 (move to the right child of 4)\n- Inserted at the right child of 4\n\n**Diagram**: [Insertion Process Diagram](https://en.wikipedia.org/wiki/Binary_search_tree)\n- **Description**: A diagram showing the process of inserting 9 into a binary search tree.\n- **Interpretation**: The insertion process involves comparing the value to be inserted with the current node values and moving left or right accordingly until the correct position is found.",
        "Deletion": "- **Process**:\n1. Find the node to delete.\n2. If the node has no children, remove it.\n3. If the node has one child, reconnect that child to the parent of the node being deleted.\n4. If the node has two children, replace the node with its in-order successor or predecessor and reconnect the tree.\n\n**Example**: Deleting a node with value 10\n- If 10 has no children, remove it.\n- If 10 has one child, replace 10 with that child.\n- If 10 has two children, find the in-order successor (smallest value in the right subtree) and replace 10 with that value."
    },
    "Time Complexity": {
        "Height of the tree": "- **Height of the Tree**: The time complexity of insertion and deletion operations is proportional to the height of the tree.\n- **Best Case**: When the tree is balanced, the height is logarithmic with respect to the number of nodes, i.e., \\( O(\\log n) \\).\n- **Worst Case**: When the tree is unbalanced (e.g., a linked list structure), the height is equal to the number of nodes, i.e., \\( O(n) \\)."
    },
    "Big-O Notation": {
        "Definition and explanation": "- **Definition**: Big-O notation describes the upper bound of an algorithm's time complexity, indicating the worst-case scenario for how long an operation will take as the input set grows.\n- **Mathematical Formulation**:\n\\[\n    f(n) = O(g(n)) \\iff \\exists C, N_0 \\in \\mathbb{R}, \\text{ s.t. } \\forall N \\geq N_0, |f(N)| \\leq C \\cdot g(N)\n\\]\n- **Application to BST Operations**: For a balanced BST, the time complexity for insert or delete operations is \\( O(\\log n) \\), as the number of operations needed is proportional to the height of the tree.\n\n**Diagram**: [Big-O Notation Diagram](https://en.wikipedia.org/wiki/Big_O_notation)\n- **Description**: Provides a formal definition of Big-O notation, stating that a function \\( f(n) \\) is \\( O(g(n)) \\) if there exist constants \\( C \\) and \\( N_0 \\) such that for all \\( N \\geq N_0 \\), the absolute value of \\( f(N) \\) is at most \\( C \\) times \\( g(N) \\).\n- **Interpretation**: Big-O notation is used to describe the upper bound of an algorithm's runtime or space requirements. The definition provides the mathematical formulation for this concept."
    }
}
st.session_state.question_list=[
        {
            "topic": "Introduction to Binary Trees",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What is a binary tree?",
                    "answer": "A binary tree is a tree structure where each node has at most two children, commonly referred to as the left and right children."
                },
                {
                    "tag": "Easy",
                    "question": "How many children can a node in a binary tree have at most?",
                    "answer": "A node in a binary tree can have at most two children."
                },
                {
                    "tag": "Challenging",
                    "question": "Provide an example of a tree structure that is not a binary tree and explain why.",
                    "hint": "Consider the maximum number of children any node can have.",
                    "answer": "A tree where any node has more than two children is not a binary tree. For instance, a tree with a root node having three children is not a binary tree because a binary tree is strictly limited to at most two children per node."
                }
            ]
        },
        {
            "topic": "Binary Search Trees (BST)",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What distinguishes a binary search tree from a regular binary tree?",
                    "answer": "In a binary search tree, the left child of a node contains values that are less than the parent, and the right child contains values that are greater than the parent, maintaining a sorted order within the tree."
                },
                {
                    "tag": "Easy",
                    "question": "In a binary search tree, where are the values greater than the parent node located?",
                    "answer": "In a binary search tree, values greater than the parent node are located in the right subtree."
                },
                {
                    "tag": "Challenging",
                    "question": "Explain how the ordering rule of a binary search tree contributes to its efficiency in search operations.",
                    "hint": "Think about how the sorted order helps in reducing the number of comparisons needed.",
                    "answer": "The ordering rule in a binary search tree ensures that each comparison eliminates half of the remaining nodes from consideration. This makes search operations much faster, as you can quickly determine whether to move left or right based on the value you are looking for, leading to a logarithmic time complexity in the best case."
                }
            ]
        },
        {
            "topic": "Operations on BST - Insertion",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "How do you insert a new value into a binary search tree?",
                    "answer": "To insert a new value into a binary search tree, you start at the root and compare the value to the current node. If the value is smaller, you go left; if it's larger, you go right. You repeat this process until you find an empty spot, and that's where the new value is inserted."
                },
                {
                    "tag": "Easy",
                    "question": "If you want to insert the value 9 into a binary search tree and the root value is 10, which direction do you move?",
                    "answer": "You move to the left subtree because 9 is smaller than 10."
                },
                {
                    "tag": "Challenging",
                    "question": "What will be the position of the value 9 if you insert it into a binary search tree with the following structure: Root(15), Left Child(10), Right Child(20)?",
                    "hint": "Follow the insertion rules of comparing values at each node.",
                    "answer": "Starting at the root (15), since 9 is smaller, you move to the left child (10). Since 9 is also smaller than 10, you move to the left again, and since the left child of 10 is empty, 9 will be inserted as the left child of 10."
                }
            ]
        },
        {
            "topic": "Operations on BST - Deletion",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What are the three different cases to consider when deleting a node from a binary search tree?",
                    "answer": "The three cases are: 1) The node has no children, 2) The node has one child, and 3) The node has two children."
                },
                {
                    "tag": "Easy",
                    "question": "If a node to be deleted has no children, what is the deletion procedure?",
                    "answer": "If a node to be deleted has no children, you simply remove it from the tree."
                },
                {
                    "tag": "Challenging",
                    "question": "Explain the process of deleting a node with two children in a binary search tree.",
                    "hint": "Consider the role of the in-order successor or predecessor.",
                    "answer": "When deleting a node with two children, you replace the node with its in-order successor or predecessor. This is typically the smallest value in the right subtree (in-order successor) or the largest value in the left subtree (in-order predecessor). After replacing, you reconnect the tree to maintain the binary search property."
                }
            ]
        },
        {
            "topic": "Time Complexity",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "How does the height of a binary search tree affect the time complexity of insertion and deletion operations?",
                    "answer": "The time complexity of insertion and deletion operations in a binary search tree is proportional to the height of the tree. In a balanced tree, the height is logarithmic with respect to the number of nodes, resulting in O(log n) time complexity. In an unbalanced tree, the height can be linear with respect to the number of nodes, resulting in O(n) time complexity."
                },
                {
                    "tag": "Easy",
                    "question": "What is the time complexity of insertion in a balanced binary search tree?",
                    "answer": "The time complexity of insertion in a balanced binary search tree is O(log n)."
                },
                {
                    "tag": "Challenging",
                    "question": "Describe a scenario where the time complexity for insertion in a binary search tree degrades to O(n).",
                    "hint": "Consider the structure of the tree when nodes are inserted in a specific order.",
                    "answer": "The time complexity for insertion in a binary search tree degrades to O(n) when the tree becomes unbalanced, such as when nodes are inserted in strictly increasing or decreasing order. In this case, the tree resembles a linked list where each node has only one child, making the height of the tree equal to the number of nodes."
                }
            ]
        },
        {
            "topic": "Big-O Notation",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What does Big-O notation describe?",
                    "answer": "Big-O notation describes the upper bound of an algorithm's time complexity, giving an idea of the worst-case scenario for how long an operation will take as the input set grows."
                },
                {
                    "tag": "Easy",
                    "question": "If an algorithm has a time complexity of O(log n), how does the time to perform an operation change as the number of inputs doubles?",
                    "answer": "If an algorithm has a time complexity of O(log n), the time to perform an operation increases logarithmically. Thus, if the number of inputs doubles, the time increases by a much smaller amount, following a logarithmic pattern."
                },
                {
                    "tag": "Challenging",
                    "question": "Explain why the time complexity for insert or delete in a balanced binary search tree is O(log n).",
                    "hint": "Consider the relationship between the height of the tree and the number of nodes.",
                    "answer": "In a balanced binary search tree, the height of the tree is logarithmic with respect to the number of nodes. This is because a balanced tree maintains a structure where the number of levels grows logarithmically as nodes are added. Since the number of operations needed for insert or delete is proportional to the height of the tree, the time complexity is O(log n)."
                }
            ]
        }
    ]

# Set page configuration
st.set_page_config(page_title="Notebook Page", layout="wide")

st.title(note_name)

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
                for question in question_data['levels']:
                    if question['tag'] == "Conceptual":
                        st.write(f"**Question**: {question['question']}")
                        st.text_input("Your answer:", key=f"{topic}_conceptual")
                        if 'hint' in question and question['hint']:
                            st.write(f"**Hint**: {question['hint']}")

            with tab2:
                for question in question_data['levels']:
                    if question['tag'] == "Easy":
                        st.write(f"**Question**: {question['question']}")
                        st.text_input("Your answer:", key=f"{topic}_easy")
                        if 'hint' in question and question['hint']:
                            st.write(f"**Hint**: {question['hint']}")

            with tab3:
                for question in question_data['levels']:
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



