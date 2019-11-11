import sys, requests
from .classmodule import Book, ReadingList
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def main():
    my_list = ReadingList()

    for t in range(3):
        search = input('Enter your book search query: ')
    
        url = 'https://www.googleapis.com/books/v1/volumes?q=' 
        result_num = '&maxResults=5'
        key = '&key=' + getenv('api_key')

        api_call = url + search + result_num + key
        json_data = requests.get(api_call).json()

        objs = [Book(json_data['items'][i]['volumeInfo']['authors'], json_data['items'][i]['volumeInfo']['title'], json_data['items'][i]['volumeInfo']['publisher']) for i in range(5)]
        for obj in objs:
            print('*'*50)
            print('Author(s): ', obj.author)
            print('Title: ', obj.title)
            print('Publisher: ', obj.publisher)
            print('*'*50)
        my_list.add_book(objs[int(input('Enter the number of the book you want to add to your reading list (in the order it appears in your results): ')) - 1])
        
    print('The following is on your reading list:')
    my_list.display_reading_list()

if __name__ == '__main__':
    main()