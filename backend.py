import sqlite3


def connect():
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text,author text, year interger, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute("SELECT * FROM  books")
    rows = curr.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute("SELECT * FROM books WHERE title=? OR author=? or year=? or isbn=?",(title,author,year,isbn))
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('DELETE FROM BOOKS WHERE ID=?',(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('UPDATE BOOKs SET TITLE=?,AUTHOR=?,YEAR=?,ISBN=? WHERE ID=?',(title,author,year,isbn,id))

#     ---------------------------
connect()
# insert("the man who sold his ferrari","paulo coelho",2005,1978111)
# insert("godan","munshi premchand",1934,1978112)
# insert("game of thrones","amit",2015,1978113)
# insert("da vinci code","leonardo da vinci",1638,1978114)
# print(view())
# print(search(author='munshi premchand'))
# delete(1978112)
# update(1,'the man who sold his fiat', 'amit kumar', 2015, 1978110)
# print(view())
