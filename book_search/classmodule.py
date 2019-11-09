class Book():
    def __init__(self, author, title, publisher):
        self.author = author
        self.title = title
        self.publisher = publisher
    def say_author(self):
        print('author is {}'.format(self.author))
        return self
    def say_title(self):
        print('title is {}'.format(self.title))
        return self
    def say_publisher(self):
        print('publisher is {}'.format(self.publisher))
        return self

class ReadingList():
    def __init__(self):
        self.reading_list = []
        self.book = Book("author", "title", "publisher")
    def add_book(self, book):
        self.reading_list.append(book)
        print('Added book to reading list')
        return self
    def display_reading_list(self):
        print(self.reading_list)
        for book in self.reading_list:
            book.say_author()
            book.say_title()
            book.say_publisher()
        return self

    
    