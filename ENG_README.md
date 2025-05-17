# Rename File - Bulk Text Replacement Tool for File Names

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)  
![Encoding](https://img.shields.io/badge/Encoding-UTF--8-orange)```

## 📌 Description
The application enables bulk replacement of text fragments in file names. Written in Python using `tkinter`.

![Screenshot](https://github.com/zbirow/Rename-file/blob/main/image.png)

## ✨ Features
- Replace any text in file names
- Support for Polish characters (UTF-8)
- Simple graphical interface
- Error and success messages

## ⚙️ Requirements
- Python 3.x
- `tkinter` library

## 🛠️ Installation
# Linux:
```bash
sudo apt-get install python3-tk
```
Windows/macOS:
```bush
pip install tk
```
## 🚀 Usage
**1. Run the program:**
python rename_file.py
or download [rename_file.exe](https://github.com/zbirow/Rename-file/releases "rename_file.exe") from releases

**2.In the interface:**

Click "Select" to choose a folder

Enter the text to replace

Click "Replace Text"

**Example:**
**Old Text:** *old_*

**New Text:** *new_*

**Before:** *old_file.txt*

**After:** *new_file.txt*

##💾 Encoding
The program supports file names in UTF-8. If issues occur, add:
```python
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
```
## ⚠️Notes
- The program does not modify file contents
- Works only on files, not folders
- Displays error messages if issues arise
