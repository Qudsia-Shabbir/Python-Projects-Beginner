import tkinter as tk
from tkinter import messagebox
import os

root = tk.Tk()
root.title("Task Manager")
root.geometry("500x400")

filename = "tasks.txt"

tasks = []

def load_tasks():
    global tasks
    tasks = []
    if os.path.exists(filename):
        with open(filename, "r") as file:
            for line in file:
                name, status = line.strip().split(", ")
                tasks.append({"name": name, "status": status.upper()})
    update_task_display()

def save_tasks():
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['name']}, {task['status']}\n")
    messagebox.showinfo("Save", "Tasks saved successfully!")

def update_task_display():
    task_display.delete(1.0, tk.END)
    for idx, task in enumerate(tasks, start=1):
        status = "DONE" if task["status"] == "DONE" else "PENDING"
        task_display.insert(tk.END, f"{idx}. {task['name']} - {status}\n")

def add_task():
    task_name = task_entry.get().strip()
    if task_name:
        tasks.append({"name": task_name.capitalize(), "status": "PENDING"})
        task_entry.delete(0, tk.END)
        update_task_display()
    else:
        messagebox.showwarning("Input Error", "Please enter a task name.")

def delete_task():
    try:
        task_index = int(task_entry.get().strip()) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            update_task_display()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number to delete.")

def mark_task_done():
    try:
        task_index = int(task_entry.get().strip()) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["status"] = "DONE"
            update_task_display()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number to mark as done.")

title_label = tk.Label(root, text="Task Manager", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
task_entry.pack(pady=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_button = tk.Button(btn_frame, text="Add Task", command=add_task, width=12, bg="lightblue")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(btn_frame, text="Delete Task", command=delete_task, width=12, bg="lightcoral")
delete_button.grid(row=0, column=1, padx=5)

done_button = tk.Button(btn_frame, text="Mark as Done", command=mark_task_done, width=12, bg="lightgreen")
done_button.grid(row=0, column=2, padx=5)

save_button = tk.Button(root, text="Save Tasks", command=save_tasks, width=20, bg="lightyellow")
save_button.pack(pady=5)

task_display = tk.Text(root, height=10, width=50, font=("Helvetica", 12))
task_display.pack(pady=10)

load_tasks()

root.mainloop()
