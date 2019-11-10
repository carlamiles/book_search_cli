import sys, requests
from .classmodule import Book, ReadingList
from .funcmodule import my_function
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def main():
    print('in main')
    # args = sys.argv[1:]
    # print('count of args :: {}'.format(len(args)))
    # my_first_book = Book('J.D. Salinger', 'The Cather in the Rye', 'Little, Brown and Company')
    # my_second_book = Book('Toni Morrison', 'The Bluest Eye', 'Holt McDougal')
    # my_third_book = Book('Toni Morrison', 'Song of Solomon', 'Alfred A. Knopf')
    # for arg in args:
        # print('passed argument :: {}'.format(arg))
        # print(my_object.say_author().say_title().say_publisher())
    # my_function('hello world')
    # my_list = ReadingList()
    # my_list.add_book(my_first_book).add_book(my_second_book).add_book(my_third_book)
    # my_list.display_reading_list()
    url = 'https://www.googleapis.com/books/v1/volumes?q=' 
    args = sys.argv[1:]
    for arg in args:
        query = arg + '+' 
    # flowers
    result_num = '&maxResults=5'
    key = '&key=' + getenv('api_key')

    api_call = url + query + result_num + key
    print(api_call)
    json_data = requests.get(api_call).json()

    # for i in range(5):
    #     print('Authors:', json_data['items'][i]['volumeInfo']['authors'])
    #     print('Title:', json_data['items'][i]['volumeInfo']['title'])
    #     print('Publisher:', json_data['items'][i]['volumeInfo']['publisher'])
    
    # for i in range(5):
    #     result_[i] = Book(json_data['items'][i]['volumeInfo']['authors'], json_data['items'][i]['volumeInfo']['title'], json_data['items'][i]['volumeInfo']['publisher'])

    book_1 = Book(json_data['items'][0]['volumeInfo']['authors'], json_data['items'][0]['volumeInfo']['title'], json_data['items'][0]['volumeInfo']['publisher'])
    book_2 = Book(json_data['items'][1]['volumeInfo']['authors'], json_data['items'][1]['volumeInfo']['title'], json_data['items'][1]['volumeInfo']['publisher'])
    book_3 = Book(json_data['items'][2]['volumeInfo']['authors'], json_data['items'][2]['volumeInfo']['title'], json_data['items'][2]['volumeInfo']['publisher'])
    book_4 = Book(json_data['items'][3]['volumeInfo']['authors'], json_data['items'][3]['volumeInfo']['title'], json_data['items'][3]['volumeInfo']['publisher'])
    book_5 = Book(json_data['items'][4]['volumeInfo']['authors'], json_data['items'][4]['volumeInfo']['title'], json_data['items'][4]['volumeInfo']['publisher'])

    print(book_1.say_title())
    print(book_2.say_author())
    print(book_3.say_publisher())

    my_list = ReadingList()
    my_list.add_book(book_1).add_book(book_2).add_book(book_5)
    print('The following is on your reading list:')
    my_list.display_reading_list()
if __name__ == '__main__':
    main()