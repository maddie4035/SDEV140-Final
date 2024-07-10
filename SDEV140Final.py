import tkinter as tk
from tkinter import messagebox

def showDashboard(root):
    for widget in root.winfo_children():
        widget.destroy()

    dashboard_frame = tk.Frame(root)
    menu_bar = tk.Menu(root)
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open")
    menu_bar.add_cascade(label="File", menu=file_menu)

    edit_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu.add_command(label="Add Recipe")
    edit_menu.add_command(label="Edit Recipe")
    edit_menu.add_command(label="Delete Recipe")
    menu_bar.add_cascade(label="Edit", menu=edit_menu)

    view_menu = tk.Menu(menu_bar, tearoff=0)
    view_menu.add_command(label="Ingredient list")
    view_menu.add_command(label="Schedule")
    view_menu.add_command(label="All recipes")
    menu_bar.add_cascade(label="View", menu=view_menu)

    root.config(menu=menu_bar)
    dashboard_frame.pack()

def main():
    root = tk.Tk()
    root.title("BakeEasy: Baking Recipe Manager")

    # Welcome Screen
    welcome_frame = tk.Frame(root)
    welcome_label = tk.Label(welcome_frame, text="Welcome to BakeEasy")
    enter_button = tk.Button(welcome_frame, text="Enter", command=lambda: showDashboard(root))
    exit_button = tk.Button(welcome_frame, text="Exit", command=root.quit)

    welcome_label.pack()
    enter_button.pack()
    exit_button.pack()
    welcome_frame.pack()

    root.mainloop()

if __name__ == "__main__":
    main()