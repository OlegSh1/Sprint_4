import pytest
from main import BooksCollector

@pytest.fixture
def booksCollector():
    collector = BooksCollector()
    collector.add_new_book('Бегущий в лабиринте')
    collector.set_book_genre('Бегущий в лабиринте', 'Фантастика')
    collector.add_new_book('Град обреченный')
    collector.set_book_genre('Град обреченный', 'Фантастика')
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')
    collector.add_new_book('Дракула')
    collector.set_book_genre('Дракула', 'Ужасы')
    collector.add_new_book('Убийство на улице Морг')
    collector.set_book_genre('Убийство на улице Морг', 'Детективы')
    collector.add_new_book('Три богатыря')
    collector.set_book_genre('Три богатыря', 'Мультфильмы')
    collector.add_new_book('Похождения бравого солдата Швейка')
    collector.set_book_genre('Похождения бравого солдата Швейка', 'Комедии')
    collector.add_new_book('Роки')


    return collector