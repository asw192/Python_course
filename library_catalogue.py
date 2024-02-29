class Book:
      
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # All books start as available
    
    def display_info(self):
        availability = "Available" if self.is_available else "Checked out"
        print(f"Title: {self.title}, Author: {self.author}, Status: {availability}")
    
    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"Book '{self.title}' checked out successfully.")
        else:
            print(f"Book '{self.title}' is currently not available.")
    
    def return_book(self):
        self.is_available = True
        print(f"Book '{self.title}' returned successfully.")

book1 = Book("Book1", "Abhijit Wander")
book2 = Book("Book2", "Shivani Sharma")

# Display book information
book1.display_info()
book2.display_info()

# Check out a book
book1.check_out()
book1.display_info()  # Display info to confirm status change

# Try to check out the same book again
book1.check_out()

# Return the book
book1.return_book()
book1.display_info()  # Display info to confirm status change
