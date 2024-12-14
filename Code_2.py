class Book:
    def __init__(self, title, author, year, isbn, pages):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}, ISBN: {self.isbn}, Pages: {self.pages}"

def add_book(books):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = int(input("Enter year of publication: "))
    isbn = input("Enter book ISBN: ")
    pages = int(input("Enter number of pages: "))
    books.append(Book(title, author, year, isbn, pages))
    print("Book added successfully!")

def display_books(books):
    if not books:
        print("No books in the library.")
    else:
        for i, book in enumerate(books, start=1):
            print(f"Book {i}: {book}\n" + "-" * 20)

def search_book_by_title(books):
    title = input("Enter title to search for: ")
    for book in books:
        if book.title.lower() == title.lower():
            print("Book found:", book)
            return
    print("Book not found.")

def main():
    books = []
    while True:
        choice = input("\nLibrary Menu:\n1. Add Book\n2. Display Books\n3. Search Book by Title\n4. Exit\nEnter your choice: ")
        if choice == '1':
            add_book(books)
        elif choice == '2':
            display_books(books)
        elif choice == '3':
            search_book_by_title(books)
        elif choice == '4':
            print("Program Closed.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
