# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book:
  def __init__(self, title):
    self.title=title

# TODO: create instances of the class
book1 = Book("War and Peace")
book2 = Book("The Catcher in the Rye")

# TODO: print the class and property
print(book1)
print(book1.title)