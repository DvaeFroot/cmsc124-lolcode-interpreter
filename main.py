import tkinter as tk
from tkinter import *
from tkinter import Scrollbar, ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor Application - {filepath}")

def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor Application - {filepath}")

window = tk.Tk()
window.title("Text Editor Application")
window.columnconfigure(0, weight=1)

#Frame for upper subwindows
fr_upper = tk.Frame(window)
fr_upper.grid(row=0,column=0, sticky=NW)
#Frame for File Explorer and Text Editor
fr_code = tk.Frame(fr_upper)
fr_code.grid(row=0, column=0, padx=5, sticky=N)
#Frame for List of tokens and Symbol Table
fr_tokens = tk.Frame(fr_upper)
fr_tokens.grid(row=0, column=1, sticky=N)
#Frame for Execute button and console/Lower subwindows
fr_run = tk.Frame(window)
fr_run.grid(row=1,column=0)

#Frame for File Explorer
fr_buttons = tk.Frame(fr_code)
fr_buttons.columnconfigure(0, weight=1)
fr_buttons.rowconfigure(0, weight=1)
fr_buttons.pack(expand=True)

#Button to open File Explorer
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_open.grid(row=0, column=0, sticky='nesw')

#Text Editor
sb_edity = Scrollbar(fr_code)
sb_edity.pack(side=RIGHT,fill=Y)
sb_editx = Scrollbar(fr_code,orient=HORIZONTAL)
sb_editx.pack(side=BOTTOM,fill=X)

txt_edit = tk.Text(fr_code,width=50,height=15, wrap=NONE, yscrollcommand=sb_edity.set, xscrollcommand=sb_editx.set)
txt_edit.pack()

sb_edity.config(command=txt_edit.yview)
sb_editx.config(command=txt_edit.xview)

#Frame for List of tokens
fr_lex = tk.Frame(fr_tokens)
fr_lex.grid(row=0, column=0, sticky=N)

lb_lex = tk.Label(fr_lex,text="Lexemes")
lb_lex.pack()

#Table for Lexemes
sb_lex = Scrollbar(fr_lex)
sb_lex.pack(side=RIGHT,fill=Y)

tbl_lex = ttk.Treeview(fr_lex, yscrollcommand=sb_lex.set)
tbl_lex['columns'] = ('Lexeme', 'Classification')

tbl_lex.column('#0', width=0, stretch=NO)
tbl_lex.column('Lexeme', anchor=CENTER, width=200)
tbl_lex.column('Classification', anchor=CENTER, width=200)

tbl_lex.heading('#0', text="",anchor=CENTER)
tbl_lex.heading('Lexeme', text="Lexeme",anchor=CENTER)
tbl_lex.heading('Classification', text="Classification",anchor=CENTER)

sb_lex.config(command=tbl_lex.yview)

tbl_lex.pack()

window.mainloop()
