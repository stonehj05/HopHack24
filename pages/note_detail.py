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

# st.session_state.note_text_raw=note

# st.session_state.question_list=questions

### Example data###
st.session_state.note_text_raw=r"""
# Binary Search Tree

## Summary
This lecture covers the fundamentals of binary search trees (BSTs), including their structure, operations (insertion and deletion), and the importance of tree height in determining the time complexity of these operations. The lecture also introduces Big O notation for analyzing algorithm efficiency.

## Outline
1. Binary Tree
   - Definition
   - Valid and Invalid Examples
2. Binary Search Tree (BST)
   - Definition and Properties
   - Use Cases
3. Insert Operation
   - Steps for Insertion
   - Example
4. Delete Operation
   - Steps for Deletion
   - Example
5. Height of the Tree
   - Definition and Impact on Complexity
6. Big O Notation
   - Definition
   - Application to BST Operations

## Detailed Notes

### 1. Binary Tree
- **Definition**: A binary tree is a tree data structure where each node has at most two children, referred to as the left child and the right child. Binary trees can have 0, 1, or 2 children.
- **Valid Example**:
  ```
      o
     / \
    o   o
  ```
  - Interpretation: An example of a valid binary tree where each node has at most 2 children.
- **Invalid Example**:
  ```
      o
     /|\
    o o o
  ```
  - Interpretation: An example of an invalid binary tree where a node has more than 2 children.

### 2. Binary Search Tree (BST)
- **Definition**: A binary search tree is a binary tree where each node follows the property: the left child contains values less than the parent, and the right child contains values greater than the parent.
- **Properties**:
  - Efficient for search, insertion, and deletion operations.
  - Maintains a sorted order within the tree.
- **Use Cases**: Useful for storing data that changes dynamically while maintaining quick lookup times.

### 3. Insert Operation
- **Steps for Insertion**:
  1. Start at the root.
  2. Compare the value to be inserted with the current node's value:
     - If less, go to the left child.
     - If greater, go to the right child.
  3. Repeat until finding an empty spot to insert the new node.
- **Example**:
  ```
      10
     /  \
    4    o
   / \
  o   9  (inserted here)
  ```
  - Interpretation: Inserting the value 9 into a binary search tree. The value 9 is compared with the nodes and inserted in the correct position.

### 4. Delete Operation
- **Steps for Deletion**:
  1. Start at the root and search for the node to delete.
  2. After finding the node:
     - If the node has no children, remove it.
     - If the node has one child, reconnect that child to the parent of the node to be deleted.
     - If the node has two children, replace the node with its in-order successor or predecessor, then reconnect the tree to maintain the BST property.

### 5. Height of the Tree
- **Definition**: The height of the tree is the length of the longest path from the root to a leaf.
- **Impact on Complexity**: The height impacts the complexity of operations in the tree, which is generally $O(\text{height})$.

### 6. Big O Notation
- **Definition**: Describes the upper bound of the time complexity of an algorithm. If $f(n) \leq C \cdot g(n)$, where $C$ is a constant, then $f(n)$ is $O(g(n))$.
- **Application to BST Operations**:
  - For a balanced BST, the height is logarithmic with respect to the number of nodes, making the time complexity for insert and delete operations $O(\log n)$.
  - If the tree becomes unbalanced, the height can be equal to the number of nodes, degrading the time complexity to $O(n)$.

## Diagrams & Related Resources
1. [Binary tree with nodes having at most two children](https://en.wikipedia.org/wiki/Binary_tree)
2. [Binary search tree with node comparisons and highlighted paths](https://en.wikipedia.org/wiki/Binary_search_tree)
3. [Definition of Big-O notation and its formal mathematical description](https://en.wikipedia.org/wiki/Big_O_notation)
"""
# Set page configuration
st.set_page_config(page_title="Notebook Page", layout="wide")


st.session_state.note_partition_dict = note2dict(st.session_state.note_text_raw, "default_course", "default_lecture")
st.session_state.question_list=[
        {
            "topic": "Binary_Tree@Definition",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What is a binary tree and how does it differ from a general tree structure?",
                    "answer": "A binary tree is a tree structure where each node has at most two children. These children are commonly referred to as the left and right children. In contrast, a general tree can have any number of children."
                },
                {
                    "tag": "Easy",
                    "question": "How many children can a node in a binary tree have?",
                    "answer": "A node in a binary tree can have at most two children."
                },
                {
                    "tag": "Challenging",
                    "question": "Explain why the restriction of having at most two children per node makes binary trees particularly useful in computer science.",
                    "hint": "Consider how this restriction might affect the complexity of operations like search, insert, and delete.",
                    "answer": "The restriction of having at most two children per node simplifies the structure, allowing for more efficient algorithms for searching, inserting, and deleting nodes. This makes binary trees particularly useful for data structures like binary search trees, where such operations need to be performed quickly and efficiently."
                }
            ]
        },
        {
            "topic": "Binary_Tree@Valid and Invalid Examples",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What is the criterion for a tree to be considered a binary tree?",
                    "answer": "A tree is considered a binary tree if every node has at most two children."
                },
                {
                    "tag": "Easy",
                    "question": "Is a tree with a node having three children a binary tree?",
                    "answer": "No, a tree with a node having three children is not a binary tree."
                },
                {
                    "tag": "Challenging",
                    "question": "Given a tree with nodes having varying numbers of children, describe an algorithm to determine if it is a binary tree.",
                    "hint": "Think about traversing the tree and checking the number of children for each node.",
                    "answer": "An algorithm to determine if a tree is a binary tree would involve a tree traversal (such as depth-first or breadth-first traversal). During traversal, for each node, you check the number of children it has. If any node is found to have more than two children, the tree is not a binary tree. Otherwise, it is a binary tree."
                }
            ]
        },
        {
            "topic": "Binary_Search_Tree_(BST)@Definition and Properties",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What is the defining property of a binary search tree (BST)?",
                    "answer": "The defining property of a BST is that for each node, the left child contains values less than the parent, and the right child contains values greater than the parent."
                },
                {
                    "tag": "Easy",
                    "question": "In a binary search tree, where are the values smaller than the root node found?",
                    "answer": "In a binary search tree, values smaller than the root node are found in the left subtree."
                },
                {
                    "tag": "Challenging",
                    "question": "Explain how the ordering rule in a binary search tree contributes to the efficiency of search operations.",
                    "hint": "Consider how the structure allows for a reduction in the number of comparisons needed.",
                    "answer": "The ordering rule in a binary search tree allows for a binary search-like approach where each comparison can eliminate half of the remaining nodes from consideration. This reduces the number of comparisons needed to find a value, making search operations efficient with a time complexity of O(log n) in a balanced tree."
                }
            ]
        },
        {
            "topic": "Binary_Search_Tree_(BST)@Use Cases",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "Why are binary search trees useful for dynamic data storage?",
                    "answer": "Binary search trees are useful for dynamic data storage because they allow for efficient insertion, deletion, and search operations while maintaining a sorted order of the data."
                },
                {
                    "tag": "Easy",
                    "question": "What advantage do binary search trees have over arrays for insertion and deletion operations?",
                    "answer": "Binary search trees allow for more efficient insertion and deletion operations compared to arrays, which may require shifting elements."
                },
                {
                    "tag": "Challenging",
                    "question": "Compare the performance of binary search trees and hash tables for search operations in terms of time complexity.",
                    "hint": "Consider the average and worst-case scenarios for both data structures.",
                    "answer": "In the average case, both binary search trees and hash tables offer efficient search operations with O(log n) and O(1) time complexity, respectively. However, in the worst case, a binary search tree can degrade to O(n) if it becomes unbalanced, while a hash table can also degrade to O(n) due to collisions. Balanced binary trees like AVL or Red-Black trees can mitigate the worst-case scenario, maintaining O(log n) complexity."
                }
            ]
        },
        {
            "topic": "Insert_Operation@Steps for Insertion",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "How is a value inserted into a binary search tree?",
                    "answer": "To insert a value into a binary search tree, you start at the root and compare the value to the current node. If the value is smaller, you go left; if it's larger, you go right. You continue this process until you find an empty spot, where the new value is inserted."
                },
                {
                    "tag": "Easy",
                    "question": "If a value is larger than the root node, which direction do you go to insert it in a binary search tree?",
                    "answer": "If a value is larger than the root node, you go to the right to insert it in a binary search tree."
                },
                {
                    "tag": "Challenging",
                    "question": "Describe how the structure of a binary search tree affects the complexity of the insert operation.",
                    "hint": "Consider the height of the tree and how it impacts the number of comparisons needed for insertion.",
                    "answer": "The complexity of the insert operation in a binary search tree is affected by the height of the tree. In a balanced tree, the height is logarithmic with respect to the number of nodes, making the insertion time complexity O(log n). However, in an unbalanced tree, where nodes are inserted in a sorted manner, the tree can become skewed, increasing the height to O(n) and thus the insertion time complexity to O(n)."
                }
            ]
        },
        {
            "topic": "Insert_Operation@Example",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What steps are involved in inserting the value 9 into a binary search tree?",
                    "answer": "To insert the value 9 into a binary search tree, you start at the root. Compare 9 to the root value; if 9 is smaller, go left; if larger, go right. Continue this process until you find an empty spot, where you insert 9 as a new node."
                },
                {
                    "tag": "Easy",
                    "question": "If the root value is 15 and you want to insert the value 9, do you move to the left or right subtree?",
                    "answer": "You move to the left subtree because 9 is smaller than 15."
                }
            ]
        },
        {
            "topic": "Delete_Operation@Steps for Deletion",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What are the steps for deleting a node with two children from a binary search tree?",
                    "answer": "To delete a node with two children from a binary search tree, you find the in-order successor or predecessor (the smallest value in the right subtree or the largest value in the left subtree), replace the node with that value, and then reconnect the tree while maintaining the binary search property."
                },
                {
                    "tag": "Easy",
                    "question": "What do you do if the node to delete has no children?",
                    "answer": "If the node to delete has no children, you simply remove it."
                },
                {
                    "tag": "Challenging",
                    "question": "Explain why deleting a node with two children requires finding the in-order successor or predecessor.",
                    "hint": "Consider the properties that need to be maintained in a binary search tree.",
                    "answer": "Deleting a node with two children requires finding the in-order successor or predecessor to maintain the binary search tree property. The in-order successor (smallest value in the right subtree) or predecessor (largest value in the left subtree) ensures that the replacement value maintains the correct ordering within the tree, preserving the binary search property."
                }
            ]
        },
        {
            "topic": "Height_of_the_Tree@Definition and Impact on Complexity",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "Why is the height of a binary search tree important for its time complexity?",
                    "answer": "The height of a binary search tree is important for its time complexity because the time it takes to perform operations like insertion and deletion is proportional to the height of the tree."
                },
                {
                    "tag": "Easy",
                    "question": "What is the best-case height of a binary search tree with n nodes?",
                    "answer": "The best-case height of a binary search tree with n nodes is O(log n) when the tree is balanced."
                },
                {
                    "tag": "Challenging",
                    "question": "Discuss how the height of a binary search tree can degrade and the impact it has on time complexity.",
                    "hint": "Consider what happens if nodes are inserted in a sorted order.",
                    "answer": "The height of a binary search tree can degrade if nodes are inserted in a sorted order, causing the tree to become unbalanced and take on a linear structure similar to a linked list. In this case, the height of the tree becomes O(n), and the time complexity for operations like insertion and deletion degrades to O(n) as well, making the tree inefficient."
                }
            ]
        },
        {
            "topic": "Big_O_Notation@Definition",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What is Big O notation and why is it used?",
                    "answer": "Big O notation is a way of describing the upper bound of an algorithm's time complexity. It is used to provide an idea of the worst-case scenario for how long an operation will take as the input set grows."
                },
                {
                    "tag": "Easy",
                    "question": "What does Big O of log n mean?",
                    "answer": "Big O of log n means that as the number of elements increases, the time it takes to perform the operation increases logarithmically."
                },
                {
                    "tag": "Challenging",
                    "question": "Explain why Big O notation is more useful for understanding algorithm efficiency than just measuring time in seconds.",
                    "hint": "Think about how Big O notation generalizes performance across different machines and input sizes.",
                    "answer": "Big O notation is more useful for understanding algorithm efficiency because it abstracts away machine-specific details and focuses on how the algorithm scales with input size. It provides a generalized way to compare the efficiency of different algorithms regardless of the specific hardware or environment, allowing for a more meaningful assessment of their performance in different scenarios."
                }
            ]
        },
        {
            "topic": "Big_O_Notation@Application to BST Operations",
            "levels": [
                {
                    "tag": "Conceptual",
                    "question": "What is the time complexity of insert and delete operations in a balanced binary search tree?",
                    "answer": "The time complexity of insert and delete operations in a balanced binary search tree is O(log n)."
                },
                {
                    "tag": "Easy",
                    "question": "In a balanced binary search tree, what is the time complexity for search operations?",
                    "answer": "In a balanced binary search tree, the time complexity for search operations is O(log n)."
                },
                {
                    "tag": "Challenging",
                    "question": "Describe how the time complexity of BST operations can degrade and provide an example of when this might happen.",
                    "hint": "Think about the structure of the tree when nodes are inserted in a particular order.",
                    "answer": "The time complexity of BST operations can degrade from O(log n) to O(n) if the tree becomes unbalanced. For example, if nodes are inserted in a strictly increasing or decreasing order, the tree can take on a linear structure similar to a linked list, where each node only has one child. In this case, the height of the tree becomes equal to the number of nodes, making operations like search, insert, and delete take linear time."
                }
            ]
        },
        {
            "topic": "Conclusion@Overview and Next Steps",
            "levels": []
        }
    ]
def blur_match(topic,section,subsection):
    # topic_parts = topic.split("@")
    # if len(topic_parts) == 2:
    #     topic_section, topic_subsection = topic_parts
    #     return topic_section == section and topic_subsection == subsection
    # return False
    # Create a blurred matching function, allowing for partial matches between section and subsection to topic where all special characters are ignored
    topic = topic.replace("_", " ").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
    section = section.replace("_", " ").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
    subsection = subsection.replace("_", " ").replace("(", "").replace(")", "").replace("[", "").replace("]", "").replace("{", "").replace("}", "")
    return section.lower() in topic.lower() and subsection.lower() in topic.lower()



# Title stored in session state
if 'lecture_name' not in st.session_state:
    st.session_state.lecture_name = "POWER NOTES"
st.title(st.session_state.lecture_name)

# Iterate through sections and subsections in the note_partition_dict
for section, subsections in st.session_state.note_partition_dict.items():
    st.header(section)
    print("section",section)
    print("subsections",subsections)
    for subsection, content in subsections.items():
        st.subheader(subsection)
        
        # Create a container for each subsection with columns inside
        with st.container():
            col1, col2 = st.columns([2, 1])
            
            # LEFT COLUMN: Display the subsection content (text)
            with col1:
                st.markdown(content)
            
            # RIGHT COLUMN: Display related questions (if any) from question_list
            with col2:
                print("st.session_state.question_list",st.session_state.question_list)
                related_questions = [
                    q for q in st.session_state.question_list 
                    if blur_match(q['topic'], f"{section}",f"{subsection}")
                ]
                print("related_questions",related_questions)
                if related_questions:
                    for question_data in related_questions:
                        st.write(f"Questions for **{section} : {subsection}**")
                        # Create tabs for different question difficulty levels
                        tab1, tab2, tab3 = st.tabs(["Conceptual", "Moderate", "Challenging"])
                        
                        # Conceptual questions
                        with tab1:
                            for question in question_data['levels']:
                                if question['tag'] == "Conceptual":
                                    st.write(f"**Question**: {question['question']}")
                                    st.text_input("Your answer:", key=f"{section}_{subsection}_conceptual")
                                    if 'hint' in question:
                                        with st.expander("Hint (Click to expand)"):
                                            st.write(question['hint'])
                        
                        # Easy questions
                        with tab2:
                            for question in question_data['levels']:
                                if question['tag'] == "Easy":
                                    st.write(f"**Question**: {question['question']}")
                                    st.text_input("Your answer:", key=f"{section}_{subsection}_easy")
                                    if 'hint' in question:
                                        with st.expander("Hint (Click to expand)"):
                                            st.write(question['hint'])
                        
                        # Challenging questions
                        with tab3:
                            for question in question_data['levels']:
                                if question['tag'] == "Challenging":
                                    st.write(f"**Question**: {question['question']}")
                                    st.text_input("Your answer:", key=f"{section}_{subsection}_challenging")
                                    if 'hint' in question:
                                        with st.expander("Hint (Click to expand)"):
                                            st.write(question['hint'])
                else:
                    st.write("No questions available for this section.")

# Footer with progress metric
st.markdown("---")
st.metric(label="Progress", value="50%", delta="5%")

# Add a button to stop execution
if st.button("Stop the process"):
    st.stop()

st.success('Page Loaded Successfully!')