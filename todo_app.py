import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python To-Do List")
        self.root.geometry("500x500")
        self.root.resizable(False, False)

        # File to store tasks
        self.file_path = "tasks.json"
        self.tasks = self.load_tasks()

        # GUI Elements
        self.setup_gui()

    def setup_gui(self):
        # Title
        title_label = tk.Label(
            self.root,
            text="To-Do List",
            font=("Helvetica", 18, "bold"),
            fg="#333"
        )
        title_label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(
            self.root,
            width=50,
            font=("Helvetica", 12),
            bd=2,
            relief="groove"
        )
        self.task_entry.pack(pady=(0, 10), padx=20)
        self.task_entry.focus()

        # Buttons Frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=(0, 10))

        add_button = tk.Button(
            buttons_frame,
            text="Add Task",
            bg="#4CAF50",
            fg="white",
            width=12,
            command=self.add_task
        )
        add_button.pack(side=tk.LEFT, padx=5)

        update_button = tk.Button(
            buttons_frame,
            text="Update Task",
            bg="#2196F3",
            fg="white",
            width=12,
            command=self.update_task
        )
        update_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(
            buttons_frame,
            text="Delete Task",
            bg="#F44336",
            fg="white",
            width=12,
            command=self.delete_task
        )
        delete_button.pack(side=tk.LEFT, padx=5)

        # Task List Frame
        self.task_list_frame = tk.Frame(self.root)
        self.task_list_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        # Scrollable Task List
        self.task_listbox = tk.Listbox(
            self.task_list_frame,
            height=15,
            width=60,
            font=("Helvetica", 12),
            selectbackground="#a6a6a6",
            selectmode=tk.SINGLE,
            activestyle="none",
            bd=2,
            relief="groove"
        )
        self.task_listbox.pack(fill=tk.BOTH, expand=True, pady=5)

        # Populate task list
        self.refresh_task_list()

        # Checkbox (for completion toggle)
        complete_button = tk.Button(
            self.root,
            text="Toggle Complete",
            bg="#FF9800",
            fg="white",
            command=self.toggle_complete
        )
        complete_button.pack(pady=(5, 15))

    def load_tasks(self):
        """Load tasks from JSON file (if exists)."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        else:
            return []

    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(self.file_path, "w") as f:
            json.dump(self.tasks, f)

    def refresh_task_list(self):
        """Update task list in GUI."""
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "•"
            self.task_listbox.insert(tk.END, f"{idx+1}. {status} {task['text']}")

    def add_task(self):
        """Add a new task."""
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.save_tasks()
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Empty Task", "Please enter a task!")

    def update_task(self):
        """Edit selected task."""
        selected_task = self.task_listbox.curselection()
        if not selected_task:
            messagebox.showwarning("No Selection", "Please select a task to update!")
            return

        new_text = self.task_entry.get().strip()
        if not new_text:
            messagebox.showwarning("Empty Task", "Please enter updated task text!")
            return

        task_idx = selected_task[0]
        self.tasks[task_idx]["text"] = new_text
        self.save_tasks()
        self.task_entry.delete(0, tk.END)
        self.refresh_task_list()

    def delete_task(self):
        """Remove selected task."""
        selected_task = self.task_listbox.curselection()
        if not selected_task:
            messagebox.showwarning("No Selection", "Please select a task to delete!")
            return

        task_idx = selected_task[0]
        del self.tasks[task_idx]
        self.save_tasks()
        self.refresh_task_list()

    def toggle_complete(self):
        """Mark task as complete/incomplete."""
        selected_task = self.task_listbox.curselection()
        if not selected_task:
            messagebox.showwarning("No Selection", "Please select a task to toggle!")
            return

        task_idx = selected_task[0]
        self.tasks[task_idx]["completed"] = not self.tasks[task_idx]["completed"]
        self.save_tasks()
        self.refresh_task_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
