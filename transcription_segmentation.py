from image2text.utils import *
import ast
import re
import json
import os

api_key = get_openai_api_key()
prompt = """
You are an AI assistant designed to help with analyzing lecture transcriptions and aligning them with lecture outlines.

**Your tasks are as follows:**

1. **Segmentation and Alignment**:
   - Divide the transcription text into segments, each corresponding to a section in the provided lecture outline.
   - Align each segment of the transcription with the appropriate section in the outline based on content similarity.

2. **Output Formatting**:
   - For each segment, provide:
     - **Topic**: The title of the section from the outline that the segment corresponds to.
     - **Text**: The corresponding text from the transcription.

3. **Ensure Completeness and Accuracy**:
   - Ensure that all parts of the transcription are assigned to the most appropriate section in the outline.
   - The segments should cover the entire transcription without omission.

**Additional Instructions**:

- Do not include any text from the outline in the "text" fields, only use the transcription text.
- If parts of the transcription do not match any section in the outline, include them under a topic called "Conclusion" or "Other" as appropriate.
- Maintain the original wording and style of the transcription in the "text" fields.

"""

followup_prompt = r'''Now, output the aligned segments in the following JSON format, and include only the JSON data without any additional text. Start with an open bracket "{", your output should be directly parsable as JSON using a JSON parser in Python or any other programming language. Please escape any special characters in the output, like the backslash "\" should be output as "\\".

JSON Format:
{
    "segments": [
        {
            "topic": "<Title from the outline>",
            "text": "<Corresponding transcription text>"
        }
        // Repeat for each segment
    ]
}
'''

def align_transcription_with_outline(transcription_text: str, outline_text: str, context: str = "") -> dict:
    messages = [
        {"role": "system", "content": prompt + context},
        {"role": "user", "content": f"**Input Transcription**:\n{transcription_text}\n\n**Input Note with Outline**:\n{outline_text}"}
    ]
    output = get_default_chat_response(messages, followup_prompt, temperature=0.7, api_key=api_key)
    # Parsing the JSON output
    try:
        json_output = json.loads(output)
    except json.JSONDecodeError as e:
        print(f"A JSONDecodeError occurred: {e}")
        return {}
    return json_output

if __name__ == '__main__':
    # Replace the following strings with your actual transcription and outline texts
    transcription_text = """
    Alright class, let’s get started with today’s topic, which is Binary Search Trees. But before we jump into that, let's first make sure we understand what a Binary Tree is. We talked about what is a tree last time, a binary tree is just a tree structure where each node has at most two children. These children are commonly referred to as the left and right children.
    Now, let me draw an example. Is this a Binary Tree? Who thinks this is a binary tree? Who thinks it's not? Alright so the majority think this is a binary tree. And indeed you are right. As you can see here, we have a tree where every node has either zero, one, or two children. This is a binary tree. What about this one? This is not a binary tree. This node here, the root node has three children. But a binary tree is strictly limited to two children per node.
    Moving on from that, let’s define what a Binary Search Tree is, and more importantly, what makes it different from a regular binary tree. The main distinction is that in a binary search tree, the left child of a node contains values that are less than the parent, and the right child contains values that are greater than the parent. This ordering rule allows binary search trees to be very efficient for operations like search, insertion, and deletion.
    Let me draw a binary search tree now. So, for example here, if you have a node with the value 10, all the nodes in its left subtree will have values smaller than 10, and all the nodes in its right subtree will have values larger than 10. This property helps maintain a sorted order within the tree, which is key for its efficiency. We will see why soon.
    Why do we use binary search trees? Binary search trees are very useful for cases where we need to store data that changes dynamically and still maintain quick lookup times. They allow you to efficiently insert new elements, delete existing ones, and search for values—all while keeping the dataset sorted. If you were using something like an array, inserting or deleting values could involve shifting elements around, which can be slow. In contrast, binary search trees make these operations much faster.
    Moving on to the operations, the first operation we’ll talk about is inserting a new value into the tree. The way you insert a value is by starting at the root and comparing the value to the current node. If the value is smaller, you go left; if it’s larger, you go right. You keep doing this until you find an empty spot, and that’s where the new value goes.
    For example, if we want to insert the value 9 into a binary search tree, we start at the root. If 9 is smaller than the root value, we go left; if it’s larger, we go right. We repeat this process until we find an empty spot. Once we find that empty spot, we insert 9 as a new node. Pretty straightforward.
    Now, for deleting a value, it’s a little more complicated. Step one, you find the node to delete. Step two. If the node you want to delete has no children, it's easy—you just remove it. But if the node has one child, you need to reconnect that child to the parent of the node you’re deleting. If the node has two children, things get more interesting. You replace the node with its in-order successor or predecessor, which is the smallest value in the right subtree or the largest value in the left subtree. After that, you reconnect the tree, making sure to maintain the binary search property.
    Let’s say we want to delete a node with the value 10. If 10 has no children, we can just remove it. If 10 has one child, we replace 10 with that child. If 10 has two children, we find the in-order successor, which is the smallest value in the right subtree, and replace 10 with that value. After that, we make sure everything else in the tree is still correctly connected.
    Now, let’s discuss the time complexity of these operations. For both insertion and deletion, the time it takes is proportional to the height of the tree. Who can tell me what is the relationship between height of tree and the number of node in the tree? Yes, Ryan. You all almost correct. In the best case, when the tree is balanced, the height of the tree is logarithmic with respect to the number of nodes. That means both insert and delete operations take "Big-O of log N" time.
    However, if the tree becomes unbalanced—like if you keep adding values in increasing order—the tree can degrade into a structure more like a linked list, where every node only has one child. In that case, the height of the tree is equal to the number of nodes, and the time complexity degrades to "Big-O of N." That’s why balancing the tree is so important, but we’ll cover balancing techniques like AVL trees and Red-Black trees in a future lecture.
    Let’s talk a little more about Big-O Notation. Big-O notation is a way of describing the upper bound of an algorithm’s time complexity. It gives you an idea of the worst-case scenario for how long an operation will take as the input size grows.
    Intuitively, when we say "Big-O of log N," it means that as the number of nodes in the tree grows, the time it takes to perform an operation increases logarithmically. So, if you double the number of nodes, the time doesn’t double—it increases by a much smaller amount, following a logarithmic pattern.
    Rigorously, we define Big-O notation using limits. We say that a function f of N is Big-O of g N if there exists a constant C and a value N nod such that for all N greater than N nod, the inequality absolute value of f N less than or equal to C times g N holds. In the case of a balanced binary search tree, we would say that the time complexity for insert or delete is "Big-O of log N," because the number of operations needed is proportional to the height of the tree, which is logarithmic in the number of nodes.
    Alright, that’s the overview for today. We’ve covered binary trees, binary search trees, how to insert and delete nodes, and how time complexity works. Make sure to practice these operations on different trees, and we’ll dig deeper into balancing techniques in future lectures. Homework is posted on Canvas and will be due next Friday. Get started on it now and go to TA’s office hours if you encounter any problems. See you next time!
    """

    outline_text = """
    ## Summary
    In this lecture, we covered the fundamentals of Binary Search Trees (BSTs), including their structure, insertion and deletion operations, and the concept of time complexity using Big-O notation. We also discussed the importance of maintaining a balanced tree to ensure efficient operations.

    ## Outline
    1. Introduction to Binary Trees
    2. Definition of Binary Search Trees
    3. Insertion Operation
    4. Deletion Operation
    5. Time Complexity and Big-O Notation

    ## Detailed Notes

    ### 1. Introduction to Binary Trees
    - **Binary Tree**: A tree structure where each node has at most two children, referred to as the left and right children. 
    - **Valid Binary Tree**: Each node has 0, 1, or 2 children.
    - **Invalid Binary Tree**: A node has more than 2 children.

    ### 2. Definition of Binary Search Trees
    - **Binary Search Tree (BST)**: A binary tree where the left child of a node contains values less than the parent, and the right child contains values greater than the parent.
    - **Properties**:
      - Left subtree contains values smaller than the node.
      - Right subtree contains values larger than the node.
      - This ordering allows efficient search, insertion, and deletion operations.

    ### 3. Insertion Operation
    - **Procedure**:
      1. Start at the root.
      2. Compare the value to be inserted with the current node.
      3. If the value is smaller, move to the left child; if larger, move to the right child.
      4. Repeat until an empty spot is found.
      5. Insert the new value at the empty spot.
    - **Example**:
      - Tree with root node 10, and nodes 4 and 9.
      - Inserting node 9:
        - 9 < 10 (Move to the left of 10)
        - 9 > 4 (Move to the right of 4)
        - Insert 9 as the right child of 4.
    - **Height of the Tree**: Denoted as \( O(h) \).

    ### 4. Deletion Operation
    - **Procedure**:
      1. Start from the root and find the node to delete.
      2. If the node has no children, simply remove it.
      3. If the node has one child, reconnect that child to the parent of the node being deleted.
      4. If the node has two children, replace the node with its in-order successor (smallest value in the right subtree) or predecessor (largest value in the left subtree), and reconnect the tree to maintain the BST property.
    - **Example**:
      - Deleting a node with value 10:
        - If 10 has no children, remove it.
        - If 10 has one child, replace 10 with that child.
        - If 10 has two children, find the in-order successor and replace 10 with that value.

    ### 5. Time Complexity and Big-O Notation
    - **Big-O Notation**: Describes the upper bound of the complexity of an algorithm.
      - **Definition**: A function \( f(n) \) is Big-O of \( g(n) \) if:
        \[
        f(n) = O(g(n))
        \]
        \[
        \Leftrightarrow
        \]
        \[
        \exists C, N_0 \in \mathbb{R}, \text{ s.t. } \forall N \geq N_0, |f(N)| \leq C \cdot g(N)
        \]
    - **Time Complexity of BST Operations**:
      - **Insertion and Deletion**: Proportional to the height of the tree.
      - **Balanced Tree**: Height is logarithmic with respect to the number of nodes (\( O(\log N) \)).
      - **Unbalanced Tree**: Height can degrade to the number of nodes (\( O(N) \)).

    ### Conclusion
    - **Key Points**:
      - Binary Search Trees are efficient for dynamic data storage with quick lookup times.
      - Maintaining a balanced tree is crucial for optimal performance.
      - Big-O notation helps in understanding the worst-case time complexity of operations.
    - **Next Steps**: Practice insertion and deletion operations on different trees. Future lectures will cover tree balancing techniques like AVL trees and Red-Black trees.

    **Homework**: Posted on Canvas, due next Friday. Visit TA's office hours for assistance.
    """

    output = align_transcription_with_outline(transcription_text, outline_text)
    print(json.dumps(output, indent=4))
    # Save the output to a JSON file
    with open('aligned_transcription_output.json', 'w') as f:
        json.dump(output, f, indent=4)
