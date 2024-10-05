#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.
#You are maintaining a library system where each book is stored as a tuple within a list. 
#Your task is to update this system by adding new books and ensuring no duplicates.
#existing Library Data:
#library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
#-Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.


def add_book(library, book):
    if book in library:
        print(f"The book '{book[0]}' by {book[1]} already exists in the library.")
    else:
        library.append(book)
        print(f"Added '{book[0]}' by {book[1]} to the library.")


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


new_books = [("Fahrenheit 451", "Ray Bradbury"), ("1984", "George Orwell")]


for book in new_books:
    add_book(library, book)


print("\nUpdated Library:")
for title, author in library:
    print(f"{title} by {author}")