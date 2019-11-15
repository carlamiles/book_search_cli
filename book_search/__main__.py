import sys, requests
from .classmodule import Book, ReadingList, BooksAPI
# from os import getenv
# from dotenv import load_dotenv, find_dotenv
from .apimodule import call_api, json_data

# load_dotenv(find_dotenv())

def main():
    # create reading list instance
    my_list = ReadingList()

    # create a loop that allows the user to search for books and save a book from the search to their reading list
    for t in range(3):
        # ask for user's search query - search keyword will appear in title of each result
        # search = input('Enter your book search query: ')
        
        # # construct Google Books API URL using a BooksAPI instance
        # key = '&key=' + getenv('api_key')
        
        # google_books_api_call = BooksAPI('https://www.googleapis.com/books/v1/volumes?q=', search, '&maxResults=5', key)
        
        # json_data = requests.get(google_books_api_call.link).json()
        call_api()
        
        # create book instances out of the Google Books API data received
        book_objs = [Book(json_data['items'][i]['volumeInfo']['authors'], json_data['items'][i]['volumeInfo']['title'], json_data['items'][i]['volumeInfo']['publisher']) for i in range(5)]
        for book_obj in book_objs:
            book_obj.display_book()
        
        # request user to enter the book they wish to add to their reading list by order in results
        my_list.add_book(book_objs[int(input('Enter the number of the book you want to add to your reading list (in the order it appears in your results): ')) - 1])
    
    # display books in the user's reading list    
    print('The following is on your reading list:')
    my_list.display_reading_list()

if __name__ == '__main__':
    main()