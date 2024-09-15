# import streamlit as st
# import os
# import copy
# from pathlib import Path

# def previousNoteReader():
#     # Specify the path to the larger folder
#     data_folder_path = Path('data')  # Using Path object for better handling
    
#     # Check if the folder exists
#     if not data_folder_path.exists():
#         st.error(f"The specified folder '{data_folder_path}' does not exist.")
#         return  # Stop the function if the folder doesn't exist

#     # Create the dictionary in session state if not exists
#     if 'courseDictionary' not in st.session_state:
#         st.session_state.courseDictionary = {}
    
#     if 'menu' not in st.session_state:
#         st.session_state.menu = {}
    
#     # Initialize courseIndex if it doesn't exist
#     if 'courseIndex' not in st.session_state:
#         st.session_state.courseIndex = 0
    
#     # Get the subfolders with their paths
#     subfolders_with_paths = [(f.name, f.path) for f in os.scandir(data_folder_path) if f.is_dir()]
    
#     CourseIndex = 1
#     for subfolder, subpath in subfolders_with_paths:
#         st.session_state.courseDictionary[CourseIndex] = str(subfolder)
#         CourseIndex += 1
#         st.session_state.courseIndex += 1  # Increment the global courseIndex
        
#         NotebookIndex = 1
#         temp = {}
        
#         # Convert subpath to a Path object and get all subdirectories (notebooks)
#         note_folder_path = Path(subpath)
#         noteFolders = [f.name for f in note_folder_path.iterdir() if f.is_dir()]
        
#         # Add each notebook to the temp dictionary
#         for notepage in noteFolders:
#             temp[NotebookIndex] = notepage
#             NotebookIndex += 1
        
#         # Update the session state menu with the current course's notebooks
#         st.session_state.menu[subfolder] = copy.deepcopy(temp)
