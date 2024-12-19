import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        # Get input text
        source_text = input_text.get("1.0", tk.END).strip()
        if not source_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        # Get selected languages
        source_lang = source_lang_combo.get()
        target_lang = target_lang_combo.get()

        # Perform translation
        translator = Translator()
        translated = translator.translate(source_text, src=source_lang, dest=target_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

# Initialize the GUI application
root = tk.Tk()
root.title("Language Translator Tool")
root.geometry("600x400")
root.resizable(False, False)

# Add Title Label
title_label = tk.Label(root, text="Language Translator", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Input Text Area
input_label = tk.Label(root, text="Input Text:", font=("Arial", 12))
input_label.pack(anchor="w", padx=20)
input_text = tk.Text(root, height=5, wrap=tk.WORD)
input_text.pack(fill="x", padx=20, pady=5)

# Language Selection
languages = list(LANGUAGES.values())
language_codes = {v: k for k, v in LANGUAGES.items()}

source_lang_frame = tk.Frame(root)
source_lang_frame.pack(fill="x", padx=20, pady=5)

source_lang_label = tk.Label(source_lang_frame, text="Source Language:", font=("Arial", 10))
source_lang_label.pack(side="left")
source_lang_combo = ttk.Combobox(source_lang_frame, values=languages, state="readonly", width=20)
source_lang_combo.pack(side="left", padx=10)
source_lang_combo.set("english")  # Default source language

target_lang_label = tk.Label(source_lang_frame, text="Target Language:", font=("Arial", 10))
target_lang_label.pack(side="left", padx=20)
target_lang_combo = ttk.Combobox(source_lang_frame, values=languages, state="readonly", width=20)
target_lang_combo.pack(side="left")
target_lang_combo.set("hindi")  # Default target language

# Translate Button
translate_button = tk.Button(root, text="Translate", font=("Arial", 12), bg="lightblue", command=translate_text)
translate_button.pack(pady=10)

# Output Text Area
output_label = tk.Label(root, text="Translated Text:", font=("Arial", 12))
output_label.pack(anchor="w", padx=20)
output_text = tk.Text(root, height=5, wrap=tk.WORD)
output_text.pack(fill="x", padx=20, pady=5)

# Run the application
root.mainloop()
