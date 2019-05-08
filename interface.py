from tkinter import *
from backend import Database

database = Database('books.db')

class Window(object):

    def __init__(self,window):
        self.window = window
        self.window.wm_title('BOOKSTORE')
        label_Title = Label(text='Title')
        label_Year = Label(text='Year')
        label_Author = Label(text='Author')
        label_ISBN = Label(text='ISBN')

        label_Title.grid(row=0, column=0, pady=2)
        label_Year.grid(row=1, column=0, pady=2)
        label_Author.grid(row=0, column=4, pady=2)
        label_ISBN.grid(row=1, column=4, pady=2)

        # -----------------------------------------
        self.title_text = StringVar()
        self.title_entry = Entry(self.window, textvariable=self.title_text)
        self.year_text = StringVar()
        self.year_entry = Entry(self.window, textvariable=self.year_text)
        self.author_text = StringVar()
        self.author_entry = Entry(self.window, textvariable=self.author_text)
        self.isbn_text = StringVar()
        self.isbn_entry = Entry(self.window, textvariable=self.isbn_text)

        self.title_entry.grid(row=0, column=1, pady=2)
        self.year_entry.grid(row=1, column=1, pady=2)
        self.author_entry.grid(row=0, column=5, pady=2)
        self.isbn_entry.grid(row=1, column=5, pady=2)
        # -----------------------------------------
        self.listbox = Listbox(self.window, height=12, width=35)
        self.listbox.grid(row=2, column=0, rowspan=8, columnspan=2, pady=2)
        self.listbox.bind('<<ListboxSelect>>', self.get_selected_row)
        sb1 = Scrollbar(self.window)
        sb1.grid(row=2, column=3, rowspan=6)

        self.listbox.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.listbox.yview)
        # -----------------------------------------
        viewall_button = Button(self.window, text='View All', justify='right', width=12, command=self.view_command)
        search_button = Button(self.window, text='Search Entry', justify='right', width=12, command=self.search_command)
        add_button = Button(self.window, text='Add Entry', justify='right', width=12, command=self.add_command)
        update_button = Button(self.window, text='Update Entry', justify='right', width=12, command=self.update_command)
        delete_button = Button(self.window, text='Delete Entry', justify='right', width=12, command=self.delete_command)
        close_button = Button(self.window, text='Close', justify='right', width=12, command=self.window.destroy)

        viewall_button.grid(row=2, column=5, pady=2)
        search_button.grid(row=3, column=5, pady=2)
        add_button.grid(row=4, column=5, pady=2)
        update_button.grid(row=5, column=5, pady=2)
        delete_button.grid(row=6, column=5, pady=2)
        close_button.grid(row=7, column=5, pady=2)


    def get_selected_row(self,event):
        try:
            global selected_tuple
            index = self.listbox.curselection()[0]
            selected_tuple = self.listbox.get(index)
            self.title_entry.delete(0,END)
            self.title_entry.insert(END, selected_tuple[1])
            self.author_entry.delete(0, END)
            self.author_entry.insert(END, selected_tuple[2])
            self.year_entry.delete(0, END)
            self.year_entry.insert(END, selected_tuple[3])
            self.isbn_entry.delete(0, END)
            self.isbn_entry.insert(END, selected_tuple[4])
        except Exception as e:
            pass
        # title, author, year, isbn
        # print(selected_tuple)
        return selected_tuple

    def view_command(self,):
        self.listbox.delete(0,END)
        for row in database.view():
            self.listbox.insert(END,row)

    def search_command(self):
        self.listbox.delete(0, END)
        for row in database.search(self.title_text.get(),self.author_text.get(), self.year_text.get(),self.isbn_text.get()):
            self.listbox.insert(END,row)

    def add_command(self):
        try:
            if(len(self.title_text.get())>0 and len(self.author_text.get())>0 and  len(self.year_text.get())>0 and len(self.isbn_text.get())>0):

                # print('yes')
                database.insert(self.title_text.get(),self.author_text.get(), self.year_text.get(),self.isbn_text.get())
                self.listbox.delete(0,END)
                self.listbox.insert(0,(self.title_text.get(),self.author_text.get(), self.year_text.get(),self.isbn_text.get()))
            else:
                # print(len(self.title_text.get())>0 , len(self.author_text.get())>0 ,  len(self.year_text.get())>0 , len(self.isbn_text.get())
                # print('no')
                raise Exception()
        except Exception as e:
            pass


    def update_command(self):
        try:
            database.update(selected_tuple[0],self.title_text.get(),self.author_text.get(), self.year_text.get(),self.isbn_text.get())
        # print(selected_tuple[0],self.title_text.get(),self.author_text.get(), self.year_text.get(),self.isbn_text.get())
        # self.listbox.delete(0, END)
        # self.listbox.insert(0, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))
        except Exception as e:
            pass

    def delete_command(self):
        try:
            database.delete(selected_tuple[0])
        except Exception as e:
            pass

window = Tk()
Window(window)
window.mainloop()