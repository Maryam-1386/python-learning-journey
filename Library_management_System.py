class Book:
    def __init__(self , id , title , author ):
        self.id = id 
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        if self.available:
            return f"Book: {self.title} | {self.author} | Available"
        else:
            return f"Book: {self.title} | {self.author} | Borrowed"

class Member:

    def __init__(self , id , name ):
        self.id = id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"Member: {self.name} | Borrowed Books: {self.borrowed_books}"
    
class Library:
    def __init__(self):
        self.books =[]
        self.members =[]

    def add_book(self,book: Book):
        self.books.append(book)

    def add_member(self,member: Member):
        self.members.append(member)

    def show_books(self):
        for book in self.books:
            print(book)

    def show_members(self):
        for member in self.members:
            print(member)
    
    def find_book(self,book_id) -> Book:
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    def find_member(self,member_id) -> Member:
        for member in self.members:
            if member.id == member_id:
                return member
        return None
            
    def borrow_book(self,member_id , book_id):
        book = self.find_book(book_id)
        member = self.find_member(member_id)
        
        if not book or not member:
            return None
        
        if book.available :
            book.available = False
            member.borrowed_books.append(book)
        else:
            print("Book is not available.")
        
    def return_book(self , member_id , book_id):
        book = self.find_book(book_id)
        member= self.find_member(member_id)

        if not book or not member:
            return None
        
        if book.available == False:
            book.available=True
            member.borrowed_books.remove(book)
        else:
            print("book was returned")
    
    def remove_book(self,book_id):
        book = self.find_book(book_id)

        if not book:
            return
        
        if not book.available:
            print("Book is borrowed.")
            return
        
        self.books.remove(book)
    
    def remove_member(self,member_id):
        member= self.find_member(member_id)

        if not member:
            return
        
        if member.borrowed_books:
            print("member borrowed the books")
            return
        
        self.members.remove(member)

