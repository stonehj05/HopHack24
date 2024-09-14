# HopHack24
put a `.env` file in the root directory with the following content:
```
OPENAI_API_KEY=your_openai_api_key
```

The official repo for Hopkins Hackathon 2024 integrative learning-helper project.
AI-powered Note Taking for Disability Student

Overall Summarize
Disability - ADHD, Visual, Hearing Disability, Mental Issue.
The Value we provide: easier class.
General Efficiency Improvement for student and Professor.
Student: Have more involvement in the lecture other than the dirty work of copy the note from the board.
Professor: Track student progress, 
Features
Core Features
(MUST HAVE)
Augment note taking with audio input and picture of the board.
Voice recording and translation. (THird party API)
Handwriting conversion (mathematical formulas in particular).
Context quizzes & syllabus (GPT power)
Syllabus as context for everything
Retrieve from web or generate new problems
AI Flashcard
Practice Exams from all notes.
Audio segmentation - alignment. (HARD)
Based on time sequence or context
Math Equation & Graphs (GPT power)
GPT recognizes & guesses the context (what the theorem//graph is).
From Theorem name to get relative equation.
Not necessarily directly translate, can search for context (like theorem) based on information	
Ask AI Questions. Ask ai for anything. Input method should accept voice (talking) - Whisper.

Other Features
(Good-to-have)
A communication platform
Allow for feedback and question
Interactive Syllabus - point title to link to the portion of the note.
Link to relevant resources
Additional Reading (paper, relative textbook section, …) 
Link to Youtube Video
Personalized Study Plan
Smart Highlighter: highlight important text in the whole note.


Create Mind Map for a lecture.

Tech
(Some tricks, methodology to implement things)
In text, where to put links and questions?
- Add some special token e.g. [[theorem]], [[definition]].
Syllabus as context.
Alignment of notebook and blackboard writing and audio input
Audio record: google model
Text recognition: GPT 4o can understand formulas and graphs based on context
Extra problem generation: searching quizlet for existing problem, let GPT generate some understanding problems
Additional material: ask GPT / create a set of potential resources, search for those when needed.


Demo
A live lecture that involve blackboard writing and presenting
A note taking for the lecture we give with corresponding questions and additional information
A syllabus that summarize the information we have
A comprehensive notebook based on previous lecture recording

TODO


