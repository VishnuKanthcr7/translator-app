import tkinter as tk
from tkinter import ttk
from googletrans import Translator


class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Language Translator")

        self.source_label = ttk.Label(root, text="Source Language:")
        self.source_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.source_combo = ttk.Combobox(
            root, values=["Auto", "English", "Spanish", "French", "German"]
        )
        self.source_combo.current(0)  # Default to Auto
        self.source_combo.grid(row=0, column=1, padx=10, pady=5)

        self.target_label = ttk.Label(root, text="Target Language:")
        self.target_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.target_combo = ttk.Combobox(
            root, values=["English", "Spanish", "French", "German"]
        )
        self.target_combo.current(0)
        self.target_combo.grid(row=1, column=1, padx=10, pady=5)

        self.text_label = ttk.Label(root, text="Enter Text:")
        self.text_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.text_entry = ttk.Entry(root, width=40)
        self.text_entry.grid(row=2, column=1, padx=10, pady=5)

        self.translate_button = ttk.Button(
            root, text="Translate", command=self.translate_text
        )
        self.translate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = ttk.Label(root, text="Translated Text:")
        self.result_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        self.result_text = tk.Text(root, width=40, height=5)
        self.result_text.grid(row=4, column=1, padx=10, pady=5)

    def translate_text(self):
        translator = Translator()

        source_lang = self.source_combo.get()
        target_lang = self.target_combo.get()
        text_to_translate = self.text_entry.get()

        if source_lang == "Auto":
            translated = translator.translate(text_to_translate, dest=target_lang)
        else:
            translated = translator.translate(
                text_to_translate, src=source_lang, dest=target_lang
            )

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, translated.text)


def main():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
