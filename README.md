# Book_Search_CLI

Package needed:
import dotenv (pip install dotenv) in order to utilize API key

To run program: 
Enter book_search in the command line

Note: the program breaks if the author, title, or publisher values are missing when retrieving book data from the Google Books API. I am working on how to fix this by not requiring these values, skipping books that don't have these values, or inserting "unknown" in place of where these values would be so that a book instance can still be created.

I approached building this command line interface by taking the following steps:

Structured classes to hold book inforamation and a reading list

1. Created a Book class with author, title, and publisher attributes and individual methods for displaying a book instance's author, title, and publisher to the console.
2. Experimented with creating instances of the book class and using the class's methods on these instances.
3. Created a ReadingList class with a reading list attribute that consisted of an emtpy list. 
4. Created a method to add a book instance to the list attribute of the ReadingList class.
5. Created a method to display all of the book instances inside of the reading list attribute of the ReadingList class.

Created the Google Books API URL for retriving book information in JSON format

6. Created variables to hold different aspects of the Google Books API request.
7. Created book instances out of the JSON data received from the Google Books API by parsing the API for author, title, and publisher information about each book received. I experimented with how to print these instances to the console, eventually deciding to create a dynamic loop to create book instances out of the JSON data.

Added functionality for adding a book from each search query to a reading list

8. Initially, I generated a ReadingList instance each time the user queried for books. I realized that this would make it impossible to save a book from each separate query. 
9. Created a ReadingList instance and then afterwards created a loop that would prompt the user to search for books and save a book from the results for up to 3 queries.
