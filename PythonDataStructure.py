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