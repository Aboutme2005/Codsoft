import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg="#f0f0f0")  # Set window background color

        self.tasks = []

        # Entry box to input tasks
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 14), borderwidth=2, relief="solid", bg="#e6f2ff", fg="black")
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add Task button
        self.add_button = tk.Button(root, text="Add Task", width=20, height=2, command=self.add_task, bg="#4CAF50", fg="white", font=("Arial", 12, 'bold'))
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, height=10, width=50, selectmode=tk.SINGLE, font=("Arial", 12), bg="#ffffff", fg="black", bd=2, relief="solid")
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Update Task button
        self.update_button = tk.Button(root, text="Update Task", width=20, height=2, command=self.update_task, bg="#ffcc00", fg="black", font=("Arial", 12, 'bold'))
        self.update_button.grid(row=2, column=0, padx=10, pady=10)

        # Delete Task button
        self.delete_button = tk.Button(root, text="Delete Task", width=20, height=2, command=self.delete_task, bg="#ff6347", fg="white", font=("Arial", 12, 'bold'))
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        # Status label to show messages
        self.status_label = tk.Label(root, text="", font=("Arial", 12), fg="green", bg="#f0f0f0")
        self.status_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
            self.status_label.config(text="Task added successfully!", fg="green")
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            new_task = self.task_entry.get()
            if new_task != "":
                old_task = self.tasks[selected_task_index]
                self.tasks[selected_task_index] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
                self.status_label.config(text=f"Task '{old_task}' updated to '{new_task}'", fg="blue")
            else:
                messagebox.showwarning("Input Error", "Task cannot be empty.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            task_to_delete = self.tasks[selected_task_index]
            del self.tasks[selected_task_index]
            self.update_task_listbox()
            self.status_label.config(text=f"Task '{task_to_delete}' deleted.", fg="red")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def update_task_listbox(self):
        """Updates the listbox with the current tasks."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
app = TodoApp(root)
root.mainloop()
