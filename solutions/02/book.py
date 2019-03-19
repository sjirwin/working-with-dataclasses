from dataclasses import dataclass

# TODO: add decorator option and fields
@dataclass(order=True)
class Book:
    title: str = ''
    author: str = ''