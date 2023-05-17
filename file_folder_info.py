import os
import math

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f'{s} {size_name[i]}'

def get_file_info(folder_path, extensions=None):
    file_info = {}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()

            # This line removes leading '.' from the extension
            file_ext = file_ext[1:] if file_ext.startswith('.') else file_ext

            if extensions and file_ext not in extensions:
                continue

            if file_ext not in file_info:
                file_info[file_ext] = {
                    'count': 1,
                    'total_size': os.path.getsize(file_path)
                }
            else:
                file_info[file_ext]['count'] += 1
                file_info[file_ext]['total_size'] += os.path.getsize(file_path)

    return file_info

def print_file_info(file_info):
    for file_ext, info in file_info.items():
        total_size = convert_size(info['total_size'])
        formatted_count = format(info['count'], ',')  # Adds comma as thousand separator
        print(f"{formatted_count} {file_ext} files with total size: {total_size}")

folder_path = input("Please enter the path of the folder: ")
extensions_input = input("Please enter the file extensions to look for, separated by comma (or leave empty to consider all files): ")

if extensions_input:
    extensions = [ext.strip().lower() for ext in extensions_input.split(",")]
else:
    extensions = None

file_info = get_file_info(folder_path, extensions)
print_file_info(file_info)
