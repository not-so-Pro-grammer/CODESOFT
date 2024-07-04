import tkinter as tk
from tkinter import messagebox
# using arial basic font for the project 
class TodoApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("To-Do List")
        
        #List to store tasks
        self.tasks = []

        # Create the main frame for listbox and scrollbar
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        #Create the listbox to display tasks.
        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, font=('Arial', 14))
        self.task_listbox.pack(side=tk.LEFT, padx=(0, 20))

        #Create the scrollbar and connect it to the listbox
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        #Create the entry widget to input new tasks
        self.entry = tk.Entry(root, width=45, font=('Arial', 14))
        self.entry.pack(pady=10)

        # Create the 'Add Task' button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, width=48, font=('Arial', 14))
        self.add_button.pack(pady=5)

        # Create the 'Remove Task' button
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task, width=48, font=('Arial', 14))
        self.remove_button.pack(pady=5)

    def add_task(self):
        # Get the task from the entry widget..
        task = self.entry.get()
        if task:
            #Add task to the list if it's not empty
            self.tasks.append(task)
            self.update_listbox()
            # Clear the entry widhget
            self.entry.delete(0, tk.END)
        else:
            # Show a warning if the task is empty
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            # Get the index of the selected task
            task_index = self.task_listbox.curselection()[0]
            # Remove the task from the list
            self.tasks.pop(task_index)
            self.update_listbox()
        except IndexError:
            # Show a warning if no task is selected
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def update_listbox(self):
        # Clear the listbox and add all tasks from the list
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    # Create the main window and run the app
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
