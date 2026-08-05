import json
import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS books(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    available INTEGER
)
""")

conn.commit()
def save_books():
    data = []

    for book in books:
        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "year": book.year,
            "available": book.available
        })

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
def load_books():
    global books

    try:
        with open("books.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        books = []

        for item in data:
            book = Book(
                item["id"],
                item["title"],
                item["author"],
                item["year"]
            )
            book.available = item["available"]
            books.append(book)

    except FileNotFoundError:
        books = []       

class Book:
 def __init__(self, id, title, author, year):
        self.id=id
        self.title=title
        self.author=author
        self.year=year
        self.available=True
        
        
books=[]   
def add_book():
    id = input("Enter ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = int(input("Enter year: "))

    cursor.execute("""
    INSERT INTO books(id, title, author, year, available)
    VALUES (?, ?, ?, ?, ?)
    """, (id, title, author, year, 1))

    conn.commit()
    print("کتاب با موفقیت اضافه شد.")
def show_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    if not rows:
        print("هیچ کتابی در کتابخانه موجود نیست.")
        return

    for row in rows:
        print(row)
               
def search_books():
    search = input("Enter ID: ")

    cursor.execute("SELECT * FROM books WHERE id = ?", (search,))
    book = cursor.fetchone()

    if book:
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Year: {book[3]}")
    else:
        print("کتابی پیدا نشد.")


def delete_books():
    delete = input("Enter ID to delete: ")

    cursor.execute("DELETE FROM books WHERE id = ?", (delete,))
    conn.commit()

    if cursor.rowcount > 0:
        print("کتاب با موفقیت حذف شد.")
    else:
        print("کتابی با این شناسه پیدا نشد.")


def update_book():
    search = input("Enter ID: ")

    cursor.execute("SELECT * FROM books WHERE id = ?", (search,))
    book = cursor.fetchone()

    if not book:
        print("کتابی با این شناسه پیدا نشد.")
        return

    title = input("Enter new title: ")
    author = input("Enter new author: ")
    year = int(input("Enter new year: "))

    cursor.execute("""
        UPDATE books
        SET title = ?, author = ?, year = ?
        WHERE id = ?
    """, (title, author, year, search))

    conn.commit()
    print("اطلاعات کتاب با موفقیت ویرایش شد.")

load_books()    
while True:
    input_1 = int(input("""
1. افزودن کتاب
2. نمایش کتاب
3. جستجوی کتاب
4. حذف کتاب
5. ویرایش کتاب
6. خروج
"""))

    if input_1 == 6:
        print("خروج از برنامه...")
        break
    elif input_1 == 1:
        add_book()
    elif input_1 == 2:
        show_books()
    elif input_1 == 3:
        search_books()
    elif input_1 == 4:
        delete_books()
    elif input_1 == 5:
        update_book()
    
