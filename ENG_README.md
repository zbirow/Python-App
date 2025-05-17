Rename File - Bulk Text Replacement Tool for File Names

📌 Description
The application enables bulk replacement of text fragments in file names. Written in Python using tkinter.

✨ Features

Replace any text in file names
Support for Polish characters (UTF-8)
Simple graphical interface
Error and success messages

⚙️ Requirements

Python 3.x
tkinter library

🛠️ Installation
Linux:
sudo apt-get install python3-tk

Windows/macOS:
pip install tk

🚀 Usage
1. Run the program:
python rename_file.py

or download rename_file.exe from releases
2. In the interface:

Click "Select" to choose a folder
Enter the text to replace
Click "Replace Text"

Example:

Old Text: old_
New Text: new_
Before: old_file.txt
After: new_file.txt

💾 Encoding
The program supports file names in UTF-8. If issues occur, add:
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

⚠️ Notes

The program does not modify file contents
Works only on files, not folders
Displays error messages if issues arise

