import sys
# sys.insert(0, "..")
from image2text.utils import *
# sys.remove("..")
api_key = get_openai_api_key()
def read_syllabus(syllabus_file_name, course_name): #should return text
    syllabus_path = f"../data/{course_name}/{syllabus_file_name}"
    if ".txt" in syllabus_file_name:
        with open(syllabus_path, "r") as file:
            return file.read()
    elif ".pdf" in syllabus_file_name:
        return read_pdf(syllabus_path)
    elif ".docx" in syllabus_file_name: #doc file
        return read_docx(syllabus_path)
    else:
        raise Exception("Unsupported file format for syllabus. Please upload .txt, .docx or .pdf")

def read_blackboard(blackboard_file_name, course_name, note_name):
    blackboard_file_path = f"../data/{course_name}/{note_name}/{blackboard_file_name}"
    if ".zip" in blackboard_file_name:
        return read_zip_images(blackboard_file_path, f"../data/{course_name}/{note_name}")
    elif (blackboard_file_name.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))):
        return [blackboard_file_path]
    else:
        raise Exception("Please upload images files or zipped image files")
    
def read_handnote(handnote_file_name, course_name, note_name):
    handnote_file_path = f"../data/{course_name}/{note_name}/{handnote_file_name}"
    if "pdf" in handnote_file_name:
        return read_pdf_images(handnote_file_path, f"../data/{course_name}/{note_name}")
    else:
        raise Exception("Please upload a pdf file")

import streamlit as st
# @st.cache_data
def note2dict(note, course_name, note_name):
    # if file exists, return the content of the file
    if os.path.exists(f"data/{course_name}/{note_name}/detailed_note_partition.json"):
        with open(f"data/{course_name}/{note_name}/detailed_note_partition.json", "r") as file:
            return json.load(file)
    # create the path
    if not os.path.exists(f"data/{course_name}/{note_name}"):
        os.makedirs(f"data/{course_name}/{note_name}")

    prompt = r"""
        You are a helpful AI assistant helping people processing information in a markdown format. In the markdown format, there will be sections and subsection titles. Your job is to convert the mark down into a JSON format like the following:
        {
            "Title" : [note title],
            "[secion 1 name]" : {
               "[subsection 1 name]" : "content",
               "[subsection 2 name]" : "content"
            },
            "[section 2 name]" : {
                "[subsection 1 name]" : ...,
                ...
            },
            ...
        }
        Make sure you do not modify any of the original contents in the notes but just reorganizing them strictly following the style guide. Do not give any extra inforamtion.
    """
    prompt += f"Input note: {note}"
    messages = prepare_messages(prompt)
    response = gpt_api_call(messages, 0.0, api_key,json_mode=True)
    temp = json.loads(response)
    with open(f"data/{course_name}/{note_name}/note_partition.json", "w") as file:
        json.dump(temp, file, indent=4)
    detailed_note = temp["Detailed Notes"]
    prompt = r"""
        You are a helpful AI assistant helping people processing information in a markdown format. In the markdown format, there will be sections and subsection titles. You will also read summary of the note content and an outline for the nodtes. Based on these information, your job is to convert the markdown following the outline into a JSON format like the following:
        {
            "[secion 1 name]" : {
               "[subsection 1 name]" : "content",
               "[subsection 2 name]" : "content"
            },
            "[section 2 name]" : {
                "[subsection 1 name]" : ...,
                ...
            },
            ...
        }
        Remove the sequence number if there is any in section or subsection titles and just keep the raw contents. Make sure you do not modify any of the original contents in the notes but just reorganizing them strictly following the style guide. Do not give any extra inforamtion.
    """
    prompt += f"""
        Input note: {detailed_note}
        Summary: {temp["Summary"]}
        Outline: {temp["Outline"]}
    """
    messages = prepare_messages(prompt)
    response = gpt_api_call(messages, 0.0, api_key, json_mode=True)
    temp = json.loads(response)
    with open(f"data/{course_name}/{note_name}/detailed_note_partition.json", "w") as file:
        json.dump(temp, file, indent=4)
    return temp

if __name__ == "__main__":
    note = r"""
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
    print(note2dict(note, "default_course", "default_lecture"))