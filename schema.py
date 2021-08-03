''' define Query type and schema '''
import typing
import strawberry

from type import Book
from resolver import get_books


@strawberry.type
class Query:
	# the strawberry.field(resolver=...) part tells it how to fetch the data when they ask for books
    books: typing.List[Book] = strawberry.field(resolver=get_books)

# make the actual GraphQL schema
schema = strawberry.Schema(query=Query)
