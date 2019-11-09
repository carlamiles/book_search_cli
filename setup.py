from setuptools import setup
setup(
    name = 'book_search_cli',
    version = '0.1.0',
    packages = ['book_search'],
    entry_points = {
        'console_scripts': [
            'book_search = book_search.__main__:main'
        ]
    })