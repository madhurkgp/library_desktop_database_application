from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        selected_tuple = listbox.get(index)
        title_entry.delete(0,END)
        title_entry.insert(END, selected_tuple[1])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_tuple[2])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_tuple[3])
        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_tuple[4])
    except Exception as e:
        pass
    # title, author, year, isbn
    # print(selected_tuple)
    return selected_tuple
def view_command():
    listbox.delete(0,END)
    for row in backend.view():
        listbox.insert(END,row)

def search_command():
    listbox.delete(0, END)
    for row in backend.search(title_text.get(),author_text.get(), year_text.get(),isbn_text.get()):
        listbox.insert(END,row)

def add_command():
    try:
        if(len(title_text.get())>0 & len(author_text.get())>0 &  len(year_text.get())>0 & len(isbn_text.get())>0):
            backend.insert(title_text.get(),author_text.get(), year_text.get(),isbn_text.get())
            listbox.delete(0,END)
            listbox.insert(0,(title_text.get(),author_text.get(), year_text.get(),isbn_text.get()))
        else:
            raise Exception()
    except Exception as e:
        pass


def update_command():
    try:# id, title, author, year, isbn
        backend.update(selected_tuple[0],title_text.get(),author_text.get(), year_text.get(),isbn_text.get())
    # print(selected_tuple[0],title_text.get(),author_text.get(), year_text.get(),isbn_text.get())
    # listbox.delete(0, END)
    # listbox.insert(0, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    except Exception as e:
        pass

def delete_command():
    try:
        backend.delete(selected_tuple[0])
    except Exception as e:
        pass

window = Tk()
window.wm_title('BOOKSTORE')
# -----------------------------------------
label_Title = Label(text='Title')
label_Year = Label(text='Year')
label_Author = Label(text='Author')
label_ISBN = Label(text='ISBN')

label_Title.grid(row=0,column=0,pady=2)
label_Year.grid(row=1,column=0,pady=2)
label_Author.grid(row=0,column=4,pady=2)
label_ISBN.grid(row=1,column=4,pady=2)

# -----------------------------------------
title_text = StringVar()
title_entry = Entry(window, textvariable = title_text)
year_text = StringVar()
year_entry = Entry(window,textvariable = year_text)
author_text = StringVar()
author_entry = Entry(window,textvariable = author_text)
isbn_text = StringVar()
isbn_entry = Entry(window,textvariable = isbn_text)

title_entry.grid(row=0,column=1,pady=2)
year_entry.grid(row=1,column=1,pady=2)
author_entry.grid(row=0,column=5,pady=2)
isbn_entry.grid(row=1,column=5,pady=2)
# -----------------------------------------
listbox = Listbox(window,height=12,width=35)
listbox.grid(row=2,column=0,rowspan=8,columnspan=2,pady=2)
listbox.bind('<<ListboxSelect>>',get_selected_row)
sb1  = Scrollbar(window)
sb1.grid(row=2,column=3,rowspan=6)

listbox.configure(yscrollcommand=sb1.set)
sb1.configure(command=listbox.yview)
# -----------------------------------------
viewall_button = Button(window,text='View All',justify='right', width=12, command=view_command)
search_button = Button(window,text='Search Entry',justify='right', width=12, command=search_command)
add_button = Button(window,text='Add Entry',justify='right', width=12, command=add_command)
update_button = Button(window,text='Update Entry',justify='right', width=12, command=update_command)
delete_button= Button(window,text='Delete Entry',justify='right', width=12, command=delete_command)
close_button = Button(window,text='Close',justify='right', width=12, command=window.destroy)

viewall_button.grid(row=2,column=5,pady=2)
search_button.grid(row=3,column=5,pady=2)
add_button.grid(row=4,column=5,pady=2)
update_button.grid(row=5,column=5,pady=2)
delete_button.grid(row=6,column=5,pady=2)
close_button.grid(row=7,column=5,pady=2)



window.mainloop()