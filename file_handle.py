import sys
# sys.insert(0, "..")
from image2text.utils import *
# sys.remove("..")
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