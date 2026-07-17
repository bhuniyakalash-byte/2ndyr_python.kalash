class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def show(self):
        if self.available:
            print(self.title, "-", self.author, "(Available)")
        else:
            print(self.title, "-", self.author, "(Borrowed)")


class Patron:
    def __init__(self, name):
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.bookList = []
        self.patronList = []

    def addBook(self, title, author):
        b = Book(title, author)
        self.bookList.append(b)

    def addPatron(self, name):
        p = Patron(name)
        self.patronList.append(p)

    def borrowBook(self, pname, bname):
        for p in self.patronList:
            if p.name == pname:
                for b in self.bookList:
                    if b.title == bname:
                        if b.available:
                            b.available = False
                            p.books.append(b)
                            print("Book Borrowed")
                        else:
                            print("Book not available")
                        return
        print("Book or Patron not found")

    def returnBook(self, pname, bname):
        for p in self.patronList:
            if p.name == pname:
                for b in p.books:
                    if b.title == bname:
                        b.available = True
                        p.books.remove(b)
                        print("Book Returned")
                        return
        print("Book not found")

    def displayBooks(self):
        print("\nBooks in Library")
        for b in self.bookList:
            b.show()

    def displayPatrons(self):
        print("\nPatrons")
        for p in self.patronList:
            print(p.name)
            if len(p.books) == 0:
                print("No books")
            else:
                for b in p.books:
                    print(b.title)


lib = Library()

lib.addBook("1984", "George Orwell")
lib.addBook("The Hobbit", "J.R.R Tolkien")

lib.addPatron("Alice")
lib.addPatron("Bob")

lib.borrowBook("Alice", "1984")
lib.borrowBook("Bob", "1984")

lib.displayBooks()
lib.displayPatrons()

lib.returnBook("Alice", "1984")

lib.displayBooks()