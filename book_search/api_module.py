import sys, requests
from .class_module import Book, ReadingList, BooksAPI
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def call_api():
    search = input('Enter your book search query: ')
    
    # construct Google Books API URL using a BooksAPI instance
    key = '&key=' + getenv('api_key')
            
    google_books_api_call = BooksAPI('https://www.googleapis.com/books/v1/volumes?q=', search, '&maxResults=5', key)
    return google_books_api_call.link

json_data = requests.get(call_api()).json()
    