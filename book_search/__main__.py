import sys
from .classmodule import Book, ReadingList
from .funcmodule import my_function
def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    my_first_book = Book('J.D. Salinger', 'The Cather in the Rye', 'Little, Brown and Company')
    my_second_book = Book('Toni Morrison', 'The Bluest Eye', 'Holt McDougal')
    my_third_book = Book('Toni Morrison', 'Song of Solomon', 'Alfred A. Knopf')
    for arg in args:
        # print('passed argument :: {}'.format(arg))
        print(my_object.say_author().say_title().say_publisher())
    # my_function('hello world')
    my_list = ReadingList()
    my_list.add_book(my_first_book).add_book(my_second_book).add_book(my_third_book)
    my_list.display_reading_list()
if __name__ == '__main__':
    main()