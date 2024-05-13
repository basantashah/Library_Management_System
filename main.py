class Book:
    def __init__(self, serial_number, title, author, publication):
        self.serial_number = serial_number
        self.title = title
        self.author = author
        self.publication = publication
        # TO-DO will add more parameters as needed
        
class Library:
    def __init__(self):
        self.books = []
        # self.serial_counter = 1 #starting from 1 for serial counter
        
    def add_book(self, book):
        self.books.append(book)
        
    # def add_book(self, title, author, publication):
    #     book = Book(self.serial_counter, title, author, publication)
    #     self.book.append(book)
    #     self.serial_counter += 1
        
if __name__ == "__main__":
    library = Library()
    
    #adding book
    def add_new_book():
        serial_number = int(input("Enter serial Number of book"))
        title = input("Enter title of book")
        author = input("Enter author name")
        publication = input("Enter publication")
        library.add_book(Book(serial_number, title, author, publication))
        print("book added")
    
    
        
    while True:
        print("\n Please press on list of Menu provided")
        print("1. Add a book")
        
        choice = input("Enter your choice")
        
        if choice == "1":
            add_new_book()
        else:
            print("Invalid option")
        
        
