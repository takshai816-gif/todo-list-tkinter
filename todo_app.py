"""
To-Do List Application & Reminders
Micro Project - I Year
------------------------------------
Features:
- Add task
- Delete selected task
- Clear all tasks
- Mark task as done (double-click)
- Task counter
Concepts used: Listbox, Buttons, Lists, Tkinter GUI events
"""

import tkinter as tk
from tkinter import messagebox


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("420x520")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        self.tasks = []  # underlying list of tasks

        self._build_ui()

    # ---------- UI SETUP ----------
    def _build_ui(self):
        title = tk.Label(
            self.root, text="📝 My To-Do List",
            font=("Segoe UI", 18, "bold"),
            bg="#1e1e2e", fg="#cdd6f4"
        )
        title.pack(pady=15)

        # Entry + Add button row
        entry_frame = tk.Frame(self.root, bg="#1e1e2e")
        entry_frame.pack(pady=5, fill="x", padx=20)

        self.task_entry = tk.Entry(
            entry_frame, font=("Segoe UI", 12),
            bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4",
            relief="flat"
        )
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 8))
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        add_btn = tk.Button(
            entry_frame, text="Add", command=self.add_task,
            bg="#89b4fa", fg="#1e1e2e", font=("Segoe UI", 10, "bold"),
            relief="flat", padx=12, cursor="hand2"
        )
        add_btn.pack(side="right")

        # Listbox
        list_frame = tk.Frame(self.root, bg="#1e1e2e")
        list_frame.pack(pady=15, padx=20, fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(
            list_frame, font=("Segoe UI", 12),
            bg="#313244", fg="#cdd6f4",
            selectbackground="#89b4fa", selectforeground="#1e1e2e",
            relief="flat", activestyle="none",
            yscrollcommand=scrollbar.set
        )
        self.listbox.pack(fill="both", expand=True)
        self.listbox.bind("<Double-Button-1>", self.toggle_done)
        scrollbar.config(command=self.listbox.yview)

        # Buttons row
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(pady=10, fill="x", padx=20)

        del_btn = tk.Button(
            btn_frame, text="Delete Selected", command=self.delete_task,
            bg="#f38ba8", fg="#1e1e2e", font=("Segoe UI", 10, "bold"),
            relief="flat", cursor="hand2"
        )
        del_btn.pack(side="left", expand=True, fill="x", padx=(0, 5), ipady=5)

        clear_btn = tk.Button(
            btn_frame, text="Clear All", command=self.clear_tasks,
            bg="#fab387", fg="#1e1e2e", font=("Segoe UI", 10, "bold"),
            relief="flat", cursor="hand2"
        )
        clear_btn.pack(side="right", expand=True, fill="x", padx=(5, 0), ipady=5)

        # Counter
        self.counter_label = tk.Label(
            self.root, text="0 tasks", font=("Segoe UI", 10),
            bg="#1e1e2e", fg="#a6adc8"
        )
        self.counter_label.pack(pady=(0, 10))

    # ---------- LOGIC ----------
    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            return
        self.tasks.append({"text": task, "done": False})
        self.task_entry.delete(0, tk.END)
        self.refresh_listbox()

    def delete_task(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("No selection", "Select a task to delete.")
            return
        index = selected[0]
        del self.tasks[index]
        self.refresh_listbox()

    def clear_tasks(self):
        if not self.tasks:
            return
        if messagebox.askyesno("Clear all", "Remove all tasks?"):
            self.tasks.clear()
            self.refresh_listbox()

    def toggle_done(self, event):
        selected = self.listbox.curselection()
        if not selected:
            return
        index = selected[0]
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.refresh_listbox()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            prefix = "✅ " if task["done"] else "🔲 "
            self.listbox.insert(tk.END, prefix + task["text"])
        pending = sum(1 for t in self.tasks if not t["done"])
        self.counter_label.config(text=f"{len(self.tasks)} tasks • {pending} pending")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
