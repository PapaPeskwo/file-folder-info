import os
import math

# Function to convert size in bytes to KB, MB, GB, etc.
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    # List of size units
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    # Find the index to use for size_name based on the size in bytes
    i = int(math.floor(math.log(size_bytes, 1024)))
    # Convert the size to the appropriate unit
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

# Function to print information about the files
def print_file_info(file_info):
    # Sort the file info dictionary by total size in descending order
    sorted_file_info = sorted(file_info.items(), key=lambda item: item[1]['total_size'], reverse=True)
    # Loop over each file extension and its info
    for extension, info in sorted_file_info:
        # Format count with comma as thousands separator
        count = f"{info['count']:,}"
        # Convert total size to appropriate size unit
        total_size = convert_size(info['total_size'])
        print(f"{count} {extension} files with total size: {total_size}")

def main():
    # Ask for user input for the folder path
    folder_path = input("Please enter the path of the folder: ")
    # Ask for user input for the file extensions to look for
    file_types_input = input("Please enter the file extensions to look for, separated by comma (or leave empty to consider all files): ")
    # Split and strip the user input, convert to lower case
    file_types = [ft.strip().lower() for ft in file_types_input.split(",")] if file_types_input else None

    # Initialize an empty dictionary to store file info
    file_info = {}

    # Walk through all subdirectories of the specified folder
    for foldername, subfolders, filenames in os.walk(folder_path):
        # Check each file in the current directory
        for filename in filenames:
            # If the user did not specify file types or the file has a specified type
            if not file_types or os.path.splitext(filename)[1][1:].lower() in file_types:
                # Extract the extension and convert to lower case
                extension = os.path.splitext(filename)[1].lower()
                # Initialize the extension in the file_info dictionary, if it's not already there
                if extension not in file_info:
                    file_info[extension] = {'count': 0, 'total_size': 0}
                # Update the count and total size for the file's extension
                file_info[extension]['count'] += 1
                file_info[extension]['total_size'] += os.path.getsize(os.path.join(foldername, filename))
                
    # Print the file info
    print_file_info(file_info)

if __name__ == "__main__":
    main()
