''' define the data resolver '''
from type import Book

# data souce (should probably be in its own file)
def get_books():
    return [
        Book(
            title='Hello, world!',
            author='Mr. Introduction',
        ),
        Book(
            title='The Great Gatsby',
            author='F. Scott Fitzgerald',
        ),
        Book(
            title='L\'amica geniale',
            author='Elena Ferrante',
        ),
    ]
