"""
Napisz funkcję, która wygeneruje zadaną liczbę ksiażek.

BookObject
    id
    title
    description
    author
    slug
"""
import csv
import os

from dataclasses import dataclass
from pathlib import Path
from typing import List, Union

from django.template.defaultfilters import slugify
from faker import Faker

faker = Faker("pl_PL")
print(os.getcwd())

@dataclass
class BookObject:
    id: int
    title: str
    description: str
    author: str
    year: int
    pages: int
    slug: str = None


    def __post_init__(self):
        self.slug = slugify(self.title)

    def values_to_list(self):
        return [self.id, self.title, self.description, self.author, self.year, self.pages, self.slug]


def generate_books(n: int) -> List[BookObject]:
    books = []
    for i in range(1, n + 1):
        books.append(BookObject(
            id=i,
            title=faker.text(50),
            description=faker.text(500),
            author=f"{faker.first_name()} {faker.last_name()}",
            year=faker.date_of_birth().year,
            pages=faker.random.randint(10, 500)
        ))
    return books


def export_to_csv(books: List[BookObject], f_name: str = None) -> Path:
    """zapisuje książki do csv o nazwie f_name albo books.csv i zwraca ściężkę do pliku"""

    if not f_name:
        f_name = "data/data.csv"

    path = Path(f_name)
    books = [b.values_to_list() for b in books]

    # books_tmp = []
    # for b in books:
    #     books_tmp.append(b.values_to_list())
    # books = books_tmp

    with path.open('w', newline='') as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(books)

    return path


def read_from_csv(f_name: Union[Path, str]) -> List[BookObject]:  # Path|str

    if type(f_name) is str:
        f_name = Path(f_name)
    data = []
    with f_name.open() as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            id, title, description, author, year, pages, slug = row
            id, year, pages = int(id), int(year), int(pages)
            book = BookObject(id, title, description, author, year, pages, slug)
            data.append(book)
    return data


# books = generate_books(n=100) # wygeneorwac listę zawierającą 100 książek
# export_to_csv(books)
# print(read_from_csv("data/data.csv"))
