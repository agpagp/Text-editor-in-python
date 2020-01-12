from tkinter import *
import tkinter.messagebox
import tkinter.scrolledtext
import tkinter.filedialog
from tkinter.colorchooser import askcolor


root=Tk()
root.title("Untitled")
root.geometry("650x620")
root.iconbitmap(r"C:\Users\Ganesh\Downloads\Bokehlicia-Captiva-Accessories-text-editor.ico")


current_file="no"


# function for open_File **completed**
def open_file(event=""):
    result=tkinter.filedialog.askopenfile(initialdir="/",filetypes=(("text files",".txt"),("all files",".*")))
    if(result!=None):
        global current_file
        textarea.delete(1.0,END) 
        for i in result:
            textarea.insert(END,i)
        current_file=result.name
        root.title(current_file)
        result.close()



# function for save as   **completed**
def save_as(event=""):
    f=tkinter.filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if f is None:
        return
    else:
        global current_file
        t1=textarea.get(1.0,END)
        current_file=f.name
        f.write(t1)
        root.title(current_file)
        f.close()
        return new
        



# function for save
def save(event=""):
    if(current_file=="no"):
        save_as()
    else:
        f=open(current_file,"w")
        f.write(textarea.get(1.0,END))
        tkinter.messagebox.showinfo("Info","you have saved the content")
        f.close()
    

    
    
    

# function for new file
def new(event=""):
    if len(textarea.get(1.0,END))>0:
        m=tkinter.messagebox.askyesno("Text Editor","Do you want save the file ?")
        if(m):
            x=save_as()
            if(x==new):
                textarea.delete(1.0,END)
            else:
                return

           
        else:
            textarea.delete(1.0,END)
        





# function for copy **completed**
def copy():
    textarea.clipboard_clear()
    textarea.clipboard_append(textarea.selection_get())
    

    
# function for cut
def cut():
    copy()
    textarea.delete("sel.first","sel.last")


# function for paste
def paste():
    textarea.insert(INSERT,textarea.clipboard_get())


# function for Exit  **completed**
def okcancel(event=""):
    p1=tkinter.messagebox.askokcancel("Text Editor","Are you sure you want to cancel this gui ?")
    if(p1):
        quit()


# function for about  **completed**
def about():
    tkinter.messagebox.showinfo("About","Basic text editor")


    
# color chooser
def selctcolor():
    (triple,color) = askcolor()

    if color:

       textarea.config(foreground=color)



# shortcut keys

root.bind("<Control-n>",new)
root.bind("<Control-o>",open_file)
root.bind("<Control-q>",okcancel)
root.bind("<Control-s>",save_as)
root.bind("<Control-w>",save)

def black():
    textarea.config(background="gray")
    textarea.config(foreground="black")
    
def white():
    textarea.config(background="white")
    textarea.config(foreground="black")
    
# status bar 
s1=Label(root,text="normal text",relief="sunken",bd=1,anchor="w")
s1.pack(side="bottom", fill="x")

# fonts
def f1():
    textarea.config(font="Helvetica")

def f2():
    textarea.config(font="Courier")
    
def f3():
    textarea.config(font="Times")

def f4():
    textarea.config(font="Italic")

def f5():
    textarea.config(font="Georgia")

def f6():
    textarea.config(font="Elephant")
    
# Textarea
textarea=tkinter.scrolledtext.ScrolledText(root,width=650,height=610,undo=True)
textarea.pack()


# Menu bar
m1=Menu(root)
root.config(menu=m1)
submenu1=Menu(m1)
m1.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="New File",accelerator="Ctrl+N",command=new)
submenu1.add_command(label="Open..",accelerator="Ctrl+O",command=open_file)
submenu1.add_command(label="Save",accelerator="Ctrl+w",command=save)
submenu1.add_command(label="Save As..",accelerator="Ctrl+S",command=save_as)
submenu1.add_separator()
submenu1.add_command(label="Exit",accelerator="Ctrl+Q",command=okcancel)


submenu2=Menu(m1)
m1.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Undo",accelerator="Ctrl+Z",command=textarea.edit_undo)
submenu2.add_command(label="Redo",accelerator="Ctrl+y",command=textarea.edit_redo)
submenu2.add_command(label="Text Color",command=selctcolor)
submenu2.add_separator()
submenu2.add_command(label="Cut",accelerator="Ctrl+X",command=cut)
submenu2.add_command(label="Copy",accelerator="Ctrl+C",command=copy)
submenu2.add_command(label="Paste",accelerator="Ctrl+V",command=paste)


submenu3=Menu(m1)
m1.add_cascade(label="Font",menu=submenu3)
submenu3.add_command(label="Helvetica",command=f1)
submenu3.add_command(label="Courier",command=f2)
submenu3.add_command(label="Times",command=f3)
submenu3.add_command(label="Italic",command=f4)
submenu3.add_command(label="Georgia",command=f5)
submenu3.add_command(label="Elephant",command=f6)



submenu4=Menu(m1)
m1.add_cascade(label="Theme",menu=submenu4)
submenu4.add_command(label="Gray",command=black)
submenu4.add_command(label="White",command=white)



submenu5=Menu(m1)
m1.add_command(label="About",command=about)



root.mainloop()


