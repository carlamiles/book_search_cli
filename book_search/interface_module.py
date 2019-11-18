from .class_module import Book, ReadingList, BooksAPI
from .api_module import call_api, json_data

# create a loop that allows the user to search for books and save a book from the search to their reading list
def create_reading_list():
    my_list = ReadingList()
    for t in range(3):
        call_api()
            
        # create book instances out of the Google Books API data received
        book_objs = [Book(json_data['items'][i]['volumeInfo']['authors'], json_data['items'][i]['volumeInfo']['title'], json_data['items'][i]['volumeInfo']['publisher']) for i in range(5)]
        for book_obj in book_objs:
            book_obj.display_book()
            
        # request user to enter the book they wish to add to their reading list by order in results
        my_list.add_book(book_objs[int(input('Enter the number of the book you want to add to your reading list (in the order it appears in your results): ')) - 1])
        print('*'*50)    
    print('The following is on your reading list:')
    my_list.display_reading_list()

