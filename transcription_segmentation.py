from image2text.utils import *
import json
import os

api_key = get_openai_api_key()

def align_transcription_with_outline(transcription_text: str, outline_text: str, context: str = "") -> dict:
    prompt = r"""
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
    - Special Symbols should be escaped correctly. For example, the backslash "\" should be output as "\\".

    """
    followup_prompt = r'''Now, output the aligned segments in the following JSON format, and include only the JSON data without any additional text. Start with an open bracket "{", your output should be directly parsable as JSON using a JSON parser in Python or any other programming language. Please escape any special characters in the output, like the backslash "\" should be output as "\\".

    {
        "segments": [
            {
                "topic": "<Title from the outline in the form of section_title@subsection_title>",
                "text": "<Corresponding transcription text>"
            }
            // Repeat for each segment
        ]
    }
    '''

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

def generate_flashcards(segments: list) -> dict:
    prompt = """
    You are an AI assistant designed to generate educational flashcards based on lecture segments.

    **Your tasks are as follows:**

    1. **Flashcard Generation**:
       - For each segment provided, create several flashcards.
       - Each flashcard should be based on key concepts or important details from the segment.

    2. **Flashcard Structure**:
       - **Topic**: Use the topic of the segment as the title of the flashcard.
       - **Question**: Formulate a question that tests understanding of a part of the topic.
       - **Answer**: Provide a concise and accurate answer to the question.

    3. **Output Formatting**:
       - Organize the flashcards in a JSON format as specified.

    **Additional Instructions**:

    - Ensure questions are clear and directly related to the content.
    - Avoid overly complex language; keep it appropriate for the target audience.
    - Do not include any additional text outside of the JSON structure.
    - Special Symbols should be escaped correctly. For example, the backslash "\" should be output as "\\".
    - If the segment is about logistic or example, you can omit the flashcard generation for that segment. Most segments should have flashcards generated.

    """
    followup_prompt = r'''Now, output the flashcards in the following JSON format, and include only the JSON data without any additional text. Start with an open bracket "{", your output should be directly parsable as JSON using a JSON parser in Python or any other programming language.

    {
        "flashcards": [
            {
                "topic": "<Topic of the segment>",
                "question": "<Flashcard question>",
                "answer": "<Answer to the question>"
            }
            // Repeat for each flashcard
        ]
    }
    '''

    # Prepare the content for GPT
    segments_text = ""
    for segment in segments:
        segments_text += f"### Segment Topic: {segment['topic']}\n{segment['text']}\n\n"

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"**Segments**:\n{segments_text}"}
    ]
    output = get_default_chat_response(messages, followup_prompt, temperature=0.7, api_key=api_key)
    # Parsing the JSON output
    try:
        json_output = json.loads(output)
    except json.JSONDecodeError as e:
        print(f"A JSONDecodeError occurred: {e}")
        return {}
    return json_output

def generate_questions(segments: list) -> dict:
    prompt = """
    You are an AI assistant designed to generate educational questions based on lecture segments.

    **Your tasks are as follows:**

    1. **Question Generation**:
       - For each segment provided, compose 3 questions:
         - **Conceptual Question**: Tests understanding of key concepts.
         - **Easy Question**: A straightforward question that reinforces basic knowledge.
         - **Challenging Question**: A more complex question that encourages deeper thinking or connects to other materials.

    2. **Question Structure**:
       - **Topic**: Use the topic of the segment.
       - **Tag**: Label each question as "Conceptual", "Easy", or "Challenging".
       - **Question**: The question itself.
       - **Hint** (optional): Provide a hint for challenging questions.
       - **Answer**: Provide a detailed answer to the question.

    3. **Output Formatting**:
       - Organize the questions in a JSON format as specified.

    **Additional Instructions**:

    - Ensure questions are clear and directly related to the content.
    - Avoid overly complex language; keep it appropriate for the target audience.
    - Do not include any additional text outside of the JSON structure.
    - If a topic is relatively easy or special (course logistic, specific examples), you can omit the "Challenging" question or omit all question if appropriate. Most topic should contain all three types of questions.
    - Special Symbols should be escaped correctly. For example, the backslash "\" should be output as "\\".

    """
    followup_prompt = r'''Now, output the questions in the following JSON format, and include only the JSON data without any additional text. Start with an open bracket "{", your output should be directly parsable as JSON using a JSON parser in Python or any other programming language.


    {
        "questions": [
            {
                "topic": "<Topic of the segment>",
                "levels": [
                    {
                        "tag": "<Conceptual/Easy/Challenging>",
                        "question": "<The question>",
                        "hint": "<Hint (optional)>",
                        "answer": "<Answer to the question>"
                    }
            }
            // Repeat for each question
        ]
    }
    '''

    # Prepare the content for GPT
    segments_text = ""
    for segment in segments:
        segments_text += f"### Segment Topic: {segment['topic']}\n{segment['text']}\n\n"

    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": f"**Segments**:\n{segments_text}"}
    ]
    output = get_default_chat_response(messages, followup_prompt, temperature=0.7, api_key=api_key)
    # Parsing the JSON output
    try:
        json_output = json.loads(output)
    except json.JSONDecodeError as e:
        print(f"A JSONDecodeError occurred: {e}")
        return {}
    return json_output

def post_process_transcription_data(transcription_text: str, note_text: str, course_name="default_course", lecture_name="default_lecture") -> None:
    # Create the directory structure /data/<course_name>/<lecture_name> if it doesn't exist
    lecture_dir = os.path.join("data", course_name, lecture_name)
    os.makedirs(lecture_dir, exist_ok=True)

    # Step 1: Align transcription with outline
    aligned_output = align_transcription_with_outline(transcription_text, note_text)
    # save the aligned_output to a JSON file
    with open(os.path.join(lecture_dir, "segments.json"), "w") as f:
        json.dump(aligned_output, f, indent=4)
    segments = aligned_output.get('segments', [])

    # Step 2: Generate flashcards
    flashcards_output = generate_flashcards(segments)
    print(json.dumps(flashcards_output, indent=4))
    # Save the flashcards to a JSON file
    with open(os.path.join(lecture_dir, "flashcards.json"), "w") as f:
        json.dump(flashcards_output, f, indent=4)

    # Step 3: Generate questions
    questions_output = generate_questions(segments)
    print(json.dumps(questions_output, indent=4))
    # Save the questions to a JSON file
    with open(os.path.join(lecture_dir, "questions.json"), "w") as f:
        json.dump(questions_output, f, indent=4)

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
       # Binary Search Tree

## Summary
This lecture covers the fundamental concepts of binary search trees (BSTs), including their structure, operations (insertion and deletion), and time complexity analysis using Big-O notation. The lecture also differentiates between binary trees and binary search trees, emphasizing the importance of maintaining a balanced tree for efficient operations.

## Outline
1. Introduction to Binary Trees
   1. Definition
   2. Example of a Binary Tree
2. Binary Search Trees (BST)
   1. Definition and Properties
   2. Example of a BST
3. Operations on BST
   1. Insert Operation
   2. Delete Operation
4. Time Complexity and Big-O Notation
   1. Definition of Big-O Notation
   2. Time Complexity of BST Operations

## Detailed Notes

### 1. Introduction to Binary Trees
#### 1.1 Definition
- A binary tree is a data structure where each node has 0, 1, or 2 children.
- These children are commonly referred to as the left and right children.

#### 1.2 Example of a Binary Tree
- **Valid Binary Tree**: Each node has at most two children.
- **Invalid Binary Tree**: A node with more than two children is not a binary tree.

![Binary Tree](https://en.wikipedia.org/wiki/Binary_tree)

### 2. Binary Search Trees (BST)
#### 2.1 Definition and Properties
- A binary search tree is a binary tree with an additional property: for any given node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater.
- This property allows for efficient search, insertion, and deletion operations.

#### 2.2 Example of a BST
- Example: A BST with nodes labeled as 10, 4, 13, 15, 1, 7, 6, and 9.
- Comparisons: 9 is greater than 4 and less than 10; 7 is less than 9.

![Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree)

### 3. Operations on BST
#### 3.1 Insert Operation
- To insert a value in a BST:
  1. Compare the value with the root.
  2. If the value is less than the root, move to the left child; if greater, move to the right child.
  3. Repeat the process until you find a suitable position.
- Example: Inserting 9 into the tree:
  - 9 is less than 10, so move left.
  - 9 is greater than 4, so move right.
  - 9 is inserted as the right child of 4.

#### 3.2 Delete Operation
- To delete a node from a BST:
  1. **Step 1**: Start from the root and find the node to delete.
  2. **Step 2**: Handle different cases for node deletion:
     - If the node has no children, simply remove it.
     - If the node has one child, reconnect the child to the parent of the node.
     - If the node has two children, find the in-order successor (smallest node in the right subtree) and replace the node's value with it, then delete the in-order successor.

### 4. Time Complexity and Big-O Notation
#### 4.1 Definition of Big-O Notation
- Big-O notation describes the upper bound of the time complexity of an algorithm.
- It provides an idea of the worst-case scenario for how long an operation will take as the input size grows.

#### 4.2 Time Complexity of BST Operations
- For both insertion and deletion, the time complexity is proportional to the height of the tree.
- **Best Case**: When the tree is balanced, the height is logarithmic with respect to the number of nodes, making the time complexity \( O(\log n) \).
- **Worst Case**: If the tree is unbalanced (e.g., a linked list structure), the height is equal to the number of nodes, making the time complexity \( O(n) \).

![Big-O Notation](https://en.wikipedia.org/wiki/Big_O_notation)

## Diagrams & Related Resources
- [Binary Tree Diagram](https://en.wikipedia.org/wiki/Binary_tree): Binary tree with at most two children per node; Incorrect structure with more than two children on the right.
- [Binary Search Tree Diagram](https://en.wikipedia.org/wiki/Binary_search_tree): Binary search tree with comparisons between nodes.
- [Big-O Notation Diagram](https://en.wikipedia.org/wiki/Big_O_notation): Definition and formal mathematical expression of Big-O notation. 
        """

    # Step 1: Align transcription with outline
    aligned_output = align_transcription_with_outline(transcription_text, outline_text)
    # save the aligned_output to a JSON file
    with open('./tmp/aligned_transcription_output.json', 'w') as f:
        json.dump(aligned_output, f, indent=4)
    segments = aligned_output.get('segments', [])

    # Step 2: Generate flashcards
    flashcards_output = generate_flashcards(segments)
    print(json.dumps(flashcards_output, indent=4))
    # Save the flashcards to a JSON file
    with open('./tmp/flashcards_output.json', 'w') as f:
        json.dump(flashcards_output, f, indent=4)

    # Step 3: Generate questions
    questions_output = generate_questions(segments)
    print(json.dumps(questions_output, indent=4))
    # Save the questions to a JSON file
    with open('./tmp/questions_output.json', 'w') as f:
        json.dump(questions_output, f, indent=4)
