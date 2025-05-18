from book import Book

def main():
    book_entry = []

    num = int(input("Total books you'd like to enter: "))

    for n in range(num):
        print(f"Information for book no {n + 1} :")
        isbn = input("ISBN no: ")
        name = input("Name of the book: ")
        pages = int(input("Number of pages: "))
        book = Book(isbn, name, pages)
        book_entry.append(book)

        print(f"Entry for the book no. {n + 1} is successful")
        print()

    while True:
        print("_____Menu_____")
        print("1. View all the books")
        print("2. Compare between two books")
        print("3. Check if the book is heavy")
        choice = int(input("Enter your choice: "))
        print()

        match choice:
            case 1:
                for n in range(num):
                    print(f"{n + 1}.", book_entry[n].display())
            case 2:
                for n in range(num):
                    print(f"{n + 1}.", book_entry[n].onlyName())

                print("Enter the two index to compare")
                index1 = int(input("Index 1: ")) - 1
                index2 = int(input("Index 2: ")) - 1

                res = book_entry[index1].compareTo(book_entry[index2])
                print(f"Result: {res}")
            case 3:
                for n in range(num):
                    print(f"{n + 1}.", book_entry[n].onlyName())

                bookIndex = int(input("Enter the index of the book: "))
                res = book_entry[bookIndex - 1].isHeavy()
                print(f"is heavy? {res}")

            case _:
                print("Invalid")

if __name__ == "__main__":
    main()