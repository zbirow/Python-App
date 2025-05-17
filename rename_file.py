import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

def replace_text():
    folder = folder_path.get()
    old_text = old_text_entry.get()
    new_text = new_text_entry.get()
    
    if not folder:
        messagebox.showerror("Błąd", "Wybierz folder.") #select folder
        return
    
    if not old_text:
        messagebox.showerror("Błąd", "Wprowadź tekst do zamiany.") #"Error", "Enter text to replace."
        return
    
    try:
        for filename in os.listdir(folder):
            old_file_path = os.path.join(folder, filename)
            if os.path.isfile(old_file_path) and old_text in filename:
                new_filename = filename.replace(old_text, new_text)
                new_file_path = os.path.join(folder, new_filename)
                os.rename(old_file_path, new_file_path)
        messagebox.showinfo("Sukces", "Operacja zakończona.") #"Success", "Operation completed."
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił problem: {str(e)}") #"Error", A problem occurred:

# Tworzenie GUI
root = tk.Tk()
root.title("Zamiana tekstu w nazwach plików") #Replacing text in file names

folder_path = tk.StringVar()

# Wybór folderu
tk.Label(root, text="Folder:").grid(row=0, column=0, padx=10, pady=10, sticky="e") #Folder:
tk.Entry(root, textvariable=folder_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Wybierz", command=select_folder).grid(row=0, column=2, padx=10, pady=10) #Select

# Pola tekstowe
tk.Label(root, text="Stary tekst:").grid(row=1, column=0, padx=10, pady=10, sticky="e") #Old Text
old_text_entry = tk.Entry(root, width=50)
old_text_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Nowy tekst:").grid(row=2, column=0, padx=10, pady=10, sticky="e") #New text
new_text_entry = tk.Entry(root, width=50)
new_text_entry.grid(row=2, column=1, padx=10, pady=10)

# Przycisk do zamiany
tk.Button(root, text="Zamień tekst", command=replace_text).grid(row=3, column=1, pady=20) #Change text

root.mainloop()
