import tkinter as tk
from tkinter import scrolledtext, messagebox
from summarizer import summarize_text

class ChatSummarizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Summarizer")
        self.chat_history = ""

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(root, width=60, height=20, state='disabled', wrap=tk.WORD)
        self.chat_display.pack(pady=10)

        # User input
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(side=tk.LEFT, padx=10)
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)

        # Summarize button
        self.summary_button = tk.Button(root, text="Summarize", command=self.show_summary)
        self.summary_button.pack(side=tk.LEFT, padx=10)

    def send_message(self, event=None):
        message = self.entry.get().strip()
        if message:

            self.chat_history += f"You: {message}\n"
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"You: {message}\n")
            self.chat_display.config(state='disabled')
            self.entry.delete(0, tk.END)

    def show_summary(self):
        print("\nself.chat_history:", self.chat_history)
        summary = summarize_text(self.chat_history)
        if summary:
            self.chat_history = f""
            self.chat_display.config(state='normal')
            self.chat_display.insert(tk.END, f"\nSummary: {summary}\n\n")
            self.chat_display.config(state='disabled')
            self.entry.delete(0, tk.END)
        # messagebox.showinfo("Chat Summary", summary)


if __name__ == "__main__":
    root = tk.Tk()
    app = ChatSummarizerApp(root)
    root.mainloop()
