# "Library Book Organiser"

books = ["The Jungle Book", "Harry Potter", "Matilda", "The Hobbit", "Wonder"]
print(books)

print("Total number of books:", len(books))
print("First book:", books[0])
print("Last book:", books[-1])
print("First three books:", books[:3])

books.append("Charlotte's Web")
print("Updated book list:", books)

books.remove("Matilda")
print("Book list after removing Matilda:", books)

books.sort()
print("Books sorted alphabetically:", books)

books.reverse()
print("Books list reversed:", books)

librarian = {
    "name": "Mrs. Rupinder Kaur",
    "library": "School Library",
    "experience": 10
}

print("Librarian's details:", librarian)
print("Library name:", librarian["library"])
print("Librarian's experience:", librarian.get("experience"))

librarian["experience"] = 12
print("Updated librarian experience:", librarian["experience"])

librarian["email"] = "rupinder.kaur@gmail.com"
print("Librarian's email:", librarian["email"])

removed_detail = librarian.pop("experience")
print("Removed experience:", removed_detail)

book_ids = [101, 102, 103, 104, 105]
book_pairs = zip(book_ids, books)
print("Book ID and title pairs:", dict(book_pairs))