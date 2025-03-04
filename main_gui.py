from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from main import report
import sys
import os

class TableDisplay(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Create Treeview widget for table display
        self.tree = ttk.Treeview(self, columns=('Character', 'Count', 'Percentage'), show='headings')
        
        # Define headings
        self.tree.heading('Character', text='Character')
        self.tree.heading('Count', text='Count')
        self.tree.heading('Percentage', text='Percentage')
        
        # Define column widths
        self.tree.column('Character', width=100, anchor='center')
        self.tree.column('Count', width=100, anchor='center')
        self.tree.column('Percentage', width=100, anchor='center')
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        # Pack widgets
        self.tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Word count label
        self.word_count_label = Label(master, text="", font=('Helvetica', 10))
        self.word_count_label.pack()
    
    def display_table(self, report_data):
        # Clear previous entries
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Update word count
        self.word_count_label.config(text=f"Total Words: {report_data['word_count']}")
        
        # Get character data
        character_data = report_data['character_data']
        
        # Calculate total characters for percentage
        total_chars = sum(char['num'] for char in character_data)
        
        # Add rows to table
        for char_dict in character_data:
            if char_dict['char'].isalpha():
                # Calculate percentage
                percentage = (char_dict['num'] / total_chars * 100)
                
                # Insert row
                self.tree.insert('', 'end', values=(
                    char_dict['char'].upper(), 
                    char_dict['num'], 
                    f"{percentage:.2f}%"
                ))

def shorten_filepath(filepath):
    """
    Shorten the filepath to a more readable format.
    Shows the last two components of the path.
    """
    # Split the path into components
    path_components = filepath.split(os.path.sep)
    
    # If the path is short, return it as is
    if len(path_components) <= 2:
        return filepath
    
    # Return last two components with leading '..'
    return os.path.join('..', path_components[-2], path_components[-1])

# Global variable to store the selected file path
selected_filepath = ""

def select_filepath():
    global selected_filepath
    selected_filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if selected_filepath:
        # Shorten the filepath for display
        shortened_path = shorten_filepath(selected_filepath)
        selected_file_label.config(text=shortened_path)
    return selected_filepath

def button_clicked():
    global selected_filepath
    if selected_filepath:
        # Capture the table from report function
        report_data = report(selected_filepath)
        if report_data:
            # Display the table
            table_display.display_table(report_data)
    else:
        selected_file_label.config(text="Please select a file first", fg="red")

# Create main window
root = Tk()
root.title("Bookbot by Fa")

# Label at the top
label = Label(root, text="Bookbot by Fa")
label.pack(pady=10)

# Label to show selected file path
selected_file_label = Label(root, text="No file selected", fg="gray")
selected_file_label.pack(pady=5)

# Buttons
button_select = Button(root, text="Pick me", command=select_filepath)
button_select.pack(pady=5)

button_run = Button(root, text="Run me", command=button_clicked)
button_run.pack(pady=5)

# Table display area
table_display = TableDisplay(root)
table_display.pack(padx=10, pady=10, fill=BOTH, expand=True)

# Start the GUI
root.mainloop()