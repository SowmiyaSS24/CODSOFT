import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.configure(bg="#FFFFE0")

        self.tasks = []

        # GUI Components
        self.task_input_label = tk.Label(root, text="Task Description:", bg="#f0f8ff", fg="#333333", font=("Arial", 12, "bold"))
        self.task_input_label.pack(pady=5)

        self.task_input = tk.Entry(root, width=50, font=("Arial", 10))
        self.task_input.pack(pady=5)

        self.due_date_label = tk.Label(root, text="Due Date (DATE-MONTH-YEAR):", bg="#f0f8ff", fg="#333333", font=("Arial", 12, "bold"))
        self.due_date_label.pack(pady=5)

        self.due_date_input = tk.Entry(root, width=50, font=("Arial", 10))
        self.due_date_input.pack(pady=5)

        self.add_task_button = tk.Button(root, text="Add Task", command=self.add_task, bg="#FFC0CB", fg="#333333", font=("Arial", 12, "bold"), relief="raised", borderwidth=2)
        self.add_task_button.pack(pady=10)

        # Clear button to clear the input boxes
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_inputs, bg="#f8f8ff", fg="#333333", font=("Arial", 12, "bold"), relief="raised", borderwidth=2)
        self.clear_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=80, height=15, font=("Arial", 10), bg="#e6f7ff", fg="#333333")
        self.task_listbox.pack(pady=10)

        self.mark_completed_button = tk.Button(root, text="Mark as Completed", command=self.mark_completed, bg="#90ee90", fg="#333333", font=("Arial", 12, "bold"), relief="raised", borderwidth=2)
        self.mark_completed_button.pack(pady=5)

        self.update_task_button = tk.Button(root, text="Update Task", command=self.update_task, bg="#87CEEB", fg="#333333", font=("Arial", 12, "bold"), relief="raised", borderwidth=2)
        self.update_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(root, text="Remove Task", command=self.remove_task, bg="#ffa07a", fg="#333333", font=("Arial", 12, "bold"), relief="raised", borderwidth=2)
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        description = self.task_input.get().strip()
        due_date = self.due_date_input.get().strip()

        if not description:
            messagebox.showwarning("Input Error", "Task description cannot be empty.")
            return

        try:
            if due_date:
                datetime.strptime(due_date, "%d-%m-%Y")
        except ValueError:
            messagebox.showwarning("Input Error", "Invalid date format. Use DATE-MONTH-YEAR.")
            return

        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'due_date': due_date or "No due date",
            'created_at': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'completed': False
        }
        self.tasks.append(task)
        self.refresh_task_list()

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Done" if task['completed'] else "Pending"
            self.task_listbox.insert(tk.END, f"[{status}] Task {task['id']}: {task['description']} (Due: {task['due_date']})")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No task selected.")
            return

        index = selected[0]
        self.tasks[index]['completed'] = True
        self.refresh_task_list()

    def remove_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No task selected.")
            return

        index = selected[0]
        del self.tasks[index]
        self.refresh_task_list()

    def update_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Selection Error", "No task selected.")
            return

        index = selected[0]
        current_task = self.tasks[index]

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Task")
        update_window.configure(bg="#f0f8ff")

        tk.Label(update_window, text="New Description:", bg="#f0f8ff", fg="#333333", font=("Arial", 12, "bold")).pack(pady=5)
        new_description_input = tk.Entry(update_window, width=50, font=("Arial", 10))
        new_description_input.pack(pady=5)
        new_description_input.insert(0, current_task['description'])

        tk.Label(update_window, text="New Due Date (DATE-MONTH-YEAR):", bg="#f0f8ff", fg="#333333", font=("Arial", 12, "bold")).pack(pady=5)
        new_due_date_input = tk.Entry(update_window, width=50, font=("Arial", 10))
        new_due_date_input.pack(pady=5)
        new_due_date_input.insert(0, current_task['due_date'] if current_task['due_date'] != "No due date" else "")

        def save_update():
            new_description = new_description_input.get().strip()
            new_due_date = new_due_date_input.get().strip()

            if not new_description:
                messagebox.showwarning("Input Error", "Task description cannot be empty.")
                return

            try:
                if new_due_date:
                    datetime.strptime(new_due_date, "%d-%m-%Y")
            except ValueError:
                messagebox.showwarning("Input Error", "Invalid date format. Use DATE-MONTH-YEAR.")
                return

            current_task['description'] = new_description
            current_task['due_date'] = new_due_date or "No due date"
            self.refresh_task_list()
            update_window.destroy()

        tk.Button(update_window, text="Save", command=save_update, bg="#add8e6", fg="#333333", font=("Arial", 12, "bold"), relief="raised", borderwidth=2).pack(pady=10)

    def clear_inputs(self):
        self.task_input.delete(0, tk.END)
        self.due_date_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
