import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.curr = self.conn.cursor()
        self.curr.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title text,author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self,title,author,year,isbn):
        self.curr.execute("INSERT INTO books VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()


    def view(self,):
        self.curr.execute("SELECT * FROM  books")
        rows = self.curr.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):
        self.curr.execute("SELECT * FROM books WHERE title=? OR author=? or year=? or isbn=?",(title,author,year,isbn))
        rows = self.curr.fetchall()
        return rows

    def delete(self,id):
        self.curr.execute('DELETE FROM BOOKS WHERE ID=?',(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.curr.execute('UPDATE BOOKS SET TITLE=?,AUTHOR=?,YEAR=?,ISBN=? WHERE ID=?',(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
    #     ---------------------------
# insert("the man who sold his ferrari","paulo coelho",2005,1978111)
# insert("godan","munshi premchand",1934,1978112)
# insert("game of thrones","amit",2015,1978113)
# insert("da vinci code","leonardo da vinci",1638,1978114)
# print(view(),end='\n')
# print(search(author='munshi premchand'))
# delete(1978112)
# update(1,'the man who sold his fiat', 'amit kumar', 2015, 1978110)
# print(view(),end='\n')
