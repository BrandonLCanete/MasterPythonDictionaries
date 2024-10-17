# Book 1
book_object_one = {
    "book_id" : 1,
    "book_title" : "GO Programming in easy steps",
    "book_author" : "Mike McGrath",
    "book_genre" : "Paperback · Non-fiction · Computer",
    "book_price" : "839.00"
}
# Book 2
book_object_two = {
    "book_id" : 2,
    "book_title" : "Web Coding & Development All-in-one For Dummies",
    "book_author" : "Paul McFedries",
    "book_genre" : "Non-fiction · Computer",
    "book_price" : "2,530.40"
}
# Book 3
book_object_three = {
    "book_id" : 3,
    "book_title" : "Effective Java",
    "book_author" : "Joshua Bloch",
    "book_genre" : "Paperback · Non-fiction · Business/Economics",
    "book_price" : "1,149.74"
}
# Book 4
book_object_four = {
    "book_id" : 4,
    "book_title" : "Logic Primer, third edition",
    "book_author" : "Colin Allen and Michael Hand",
    "book_genre" : "Paperback · Non-fiction · Mathematics",
    "book_price" : "1,919.32"
}
# Book 5
book_object_five = {
    "book_id" : 5,
    "book_title" : "Logically Fallacious",
    "book_author" : "Bo Bennett",
    "book_genre" : "Paperback · Non-fiction · Education",
    "book_price" : "1,441.51"
}

# Hold the book dictionaries to boos variable
books = [book_object_one,book_object_two,book_object_three,book_object_four,book_object_five]
# Loop through the dictionaries
for book in books:
    # Print the data
    print(f"Book Title: {book.get('book_title')}, Book Author: {book.get('book_author')}, Book Genre: {book.get('book_genre')}, Book Price: {book.get('book_price')}")