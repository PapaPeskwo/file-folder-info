import os
import math

def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def print_file_info(file_info):
    sorted_file_info = sorted(file_info.items(), key=lambda item: item[1]['total_size'], reverse=True)
    for extension, info in sorted_file_info:
        count = f"{info['count']:,}"
        total_size = convert_size(info['total_size'])
        print(f"{count} {extension} files with total size: {total_size}")

def main():
    folder_path = input("Please enter the path of the folder: ")
    file_types_input = input("Please enter the file extensions to look for, separated by comma (or leave empty to consider all files): ")
    file_types = [ft.strip().lower() for ft in file_types_input.split(",")] if file_types_input else None
    file_info = {}
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if not file_types or any(filename.lower().endswith(ft) for ft in file_types):
                extension = os.path.splitext(filename)[1].lower()
                file_size = os.path.getsize(os.path.join(foldername, filename))
                if extension in file_info:
                    file_info[extension]['count'] += 1
                    file_info[extension]['total_size'] += file_size
                else:
                    file_info[extension] = {'count': 1, 'total_size': file_size}
    print_file_info(file_info)

if __name__ == "__main__":
    main()
