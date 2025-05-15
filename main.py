#Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
#Create the Book class (plus methods and attributes)
class Book:
    def __init__(self, numPages, author, title):
        self.numPages = numPages
        self.author = author
        self.title = title

class Novel(Book):
    def __init__(self, numPages, author, title, genre, numChaps):
        super().__init__(numPages, author, title)
        self.genre = genre
        self.numChaps = numChaps


def rateBook(self, rating):
    rating = int(input("Give this book a rating out of 10"))


#Create the Novel class that inherits from Book class.
#Create the Magazine class that inherits from Book class.