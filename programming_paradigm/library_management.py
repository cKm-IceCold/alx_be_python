class Book:
    """A class representing a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track if the book is checked out

    def check_out(self):
        """Mark the book as checked out if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Book is already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Book was not checked out

    def is_available(self):
        """Return True if the book is not checked out."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of Book instances."""

    def __init__(self):
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """Add a book to the library's collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # Book not found

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found

    def list_available_books(self):
        """Print a list of all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

