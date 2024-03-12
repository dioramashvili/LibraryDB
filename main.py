import sqlite3
from random import randint, choice

conn = sqlite3.connect('LibraryDB')
c = conn.cursor()
c.execute("""CREATE TABLE books (
        name text,
        pages integer,
        cover text,
        category text
        )""")

data = [
    (
        f"Book {i}",
        randint(100, 500),
        choice(["cover1", "cover2", "cover3"]),
        choice(["Fiction", "Non-Fiction", "Science", "History", "Biography"])
    ) for i in range(10)
]
c.executemany("INSERT INTO books VALUES(?, ?, ?, ?)", data)
conn.commit()
print("-----------")
for row in c.execute("SELECT name, pages, cover, category FROM books ORDER BY pages"):
    print(row)

conn.commit()
conn.close()
new_con = sqlite3.connect("LibraryDB")
new_cur = new_con.cursor()
res = new_cur.execute("SELECT AVG(pages) FROM books")
avg_pages = res.fetchone()[0]
print(f'The average number of pages in our library is {avg_pages}')
res2 = new_cur.execute("SELECT name, pages FROM books ORDER BY pages DESC")
name, pages = res2.fetchone()
print(f'The biggest book is "{name}", with {pages} pages')