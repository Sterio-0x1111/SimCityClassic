import tkinter as tk
from tkinter import filedialog


class FileSelection:
    def select_json_file(self):
        root = tk.Tk()
        root.withdraw()  # Verberge das Tkinter-Fenster

        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        return file_path
