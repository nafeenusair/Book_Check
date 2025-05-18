class Book:
    count = 0

    def __init__(self, isbn, bookTitle, numOfPages):
        self.isbn = isbn
        self.bookTitle = bookTitle
        self.numOfPages = numOfPages
        Book.count += 1

    def display(self):
        return f"Name of the book: {self.bookTitle}\nISBN: {self.isbn}\nNumber of pages: {self.numOfPages}"

    def onlyName(self):
        return f"Name of the book: {self.bookTitle}"

    def compareTo(self, otherBook):
        if self.numOfPages > otherBook.numOfPages:
            print(f"{self.bookTitle} has more pages then {otherBook.bookTitle}")
            return 1
        elif self.numOfPages < otherBook.numOfPages:
            print(f"{self.bookTitle} has less pages then {otherBook.bookTitle}")
            return -1
        elif self.numOfPages == self.numOfPages:
            print(f"{self.bookTitle} has same pages as {otherBook.bookTitle}")
            return 0
        else:
            print("Invalid")

    def isHeavy(self):
        if self.numOfPages > 500:
            return True
        else:
            return False