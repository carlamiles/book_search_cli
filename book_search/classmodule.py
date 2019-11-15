class Book():
    def __init__(self, author, title, publisher):
        self.author = author
        self.title = title
        self.publisher = publisher
    def say_author(self):
        print('Author: {}'.format(self.author))
        return self
    def say_title(self):
        print('Title: {}'.format(self.title))
        return self
    def say_publisher(self):
        print('Publisher: {}'.format(self.publisher))
        return self
    def display_book(self):
        print('*'*50)
        print('Author(s): ', self.author)
        print('Title: ', self.title)
        print('Publisher: ', self.publisher)
        print('*'*50)
        return self

class ReadingList():
    def __init__(self):
        self.reading_list = []
    def add_book(self, book):
        self.reading_list.append(book)
        print('Added book to reading list:', book.title, 'by', book.author, 'published by', book.publisher)
        return self
    def display_reading_list(self):
        print(self.reading_list)
        for book in self.reading_list:
            print('*'*50)
            book.say_author()
            book.say_title()
            book.say_publisher()
            print('*'*50)
        return self

class BooksAPI():
    def __init__(self, url, query, params, key):
        self.url = url
        self.params = params
        self.query = query
        self.key = key
        self.link = url + query + params + key

    
    