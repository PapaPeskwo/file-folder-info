# File Folder Info

This Python script allows you to scan a specified Windows directory and outputs the count and total size of each type of file present in that directory.

## Features

- Specify a folder to scan
- Option to specify file extensions to filter the results
- Outputs the count and total size of each type of file
- Sizes are displayed in a human-readable format (B, KB, MB, GB, TB)
- The count of files is formatted with thousands separators

## Usage

1. Clone or download this repository to your local machine.
2. Open a terminal and navigate to the directory containing `file_folder_info.py`.
3. Run the script using Python by typing `python file_folder_info.py`.
4. When prompted, enter the path of the directory you want to scan.
5. If desired, enter the file extensions you want to filter by, separated by commas. If you want to consider all files, just press Enter without typing anything.

## Dependencies

- Python 3.x
- os module
- math module

## Example
```
$ python file_folder_info.py
Please enter the path of the folder: C:/Users/username/Documents
Please enter the file extensions to look for, separated by comma (or leave empty to consider all files): pdf, docx
2,300 .pdf files with total size: 500 MB
1,500 .docx files with total size: 250 MB
```

