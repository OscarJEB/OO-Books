class Book:
    def __init__(self, numPages, author, title):
        self.numPages = numPages
        self.author = author
        self.title = title

    def rateBook(self):
        rating = int(input(f"Give a rating out of 10 for '{self.title}': "))
        print(f"You rated the book '{self.title}' by {self.author} a {rating}/10.")

class Novel(Book):
    def __init__(self, numPages, author, title, genre, numChaps):
        super().__init__(numPages, author, title)
        self.genre = genre
        self.numChaps = numChaps

    # Use rateBook method for Novels now 
    def rateBook(self):
        rating = int(input(f"Give a rating out of 10 for the novel '{self.title}' in the genre '{self.genre}': "))
        print(f"You rated the novel '{self.title}' a {rating}/10. It has {self.numChaps} chapters.")
#mainline
books = [
    Book(100, "George Orwell", "Politics for Dummies"),
    Novel(300, "J.K. Rowling", "The Wandering Orphan", "Fantasy", 17)
    ]

for b in books:
    b.rateBook()  # Python will automatically use the right version of rateBook