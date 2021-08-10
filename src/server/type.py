import typing
import strawberry


# define Book type
@strawberry.type
class Book:
    title: str
    author: str
