import os
from pathlib import Path

def get_files_and_folders(folder_path):
    entries = os.listdir(folder_path)
    files = []
    folders = []
    for entry in entries:
        path = os.path.join(folder_path, entry)
        if os.path.isfile(path):
            files.append(path)
        elif os.path.isdir(path):
            folders.append(path)
    return files, folders

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        print('file_path' ,file_path)
        content = file.read()
    return content

def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def combine_files(folder_path):
    combined_content = ''

    def traverse_and_combine(current_path):
        nonlocal combined_content
        files, folders = get_files_and_folders(current_path)
        for file_path in files:
            file_content = read_file_content(file_path)
            combined_content += f"File: {file_path}\n\n{file_content}\n\n"        
        for folder_path in folders:
            traverse_and_combine(folder_path)

    traverse_and_combine(folder_path)
    return combined_content

# Get the current working directory (where the script is located)
current_dir = os.getcwd()

# Combine files in the current directory and its subdirectories
combined_content = combine_files(current_dir)

# Write the combined content to a new file
output_file_path = os.path.join(current_dir, 'combined_files.txt')
write_to_file(output_file_path, combined_content)

print(f"Combined content has been written to {output_file_path}")
