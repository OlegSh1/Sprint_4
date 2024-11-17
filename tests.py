import pytest

from main import BooksCollector
from conftest import booksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    def test_add_new_book_more_conditions_not_add_book(self, booksCollector):
        book = '1111111111111111111111111111111111111111111111111111'
        booksCollector.add_new_book(book)
        assert book not in booksCollector.books_genre

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_book_in_books_genre_add_book(self):
        collector = BooksCollector()
        book = "Бегущий в лабиринте"
        genre = "Фантастика"

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert genre in collector.books_genre.values()

    def test_set_book_genre_genre_not_in_genre_no_added_book(self):
        collector = BooksCollector()
        book = "Роки"
        genre = "Боевик"

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.books_genre[book] == ''

    def test_set_book_genre_book_not_in_books_genre_no_added_book(self):
        collector = BooksCollector()
        book = "Роки"
        genre = "Фантастика"

        collector.set_book_genre(book, genre)
        assert collector.books_genre == {}

    def test_get_book_genre_book_in_books_genre_get_genre(self, booksCollector):
        book = "Оно"
        genre = "Ужасы"
        assert booksCollector.books_genre.get(book) == genre

    def test_get_book_genre_book_has_not_genre_empty_output(self, booksCollector):
        book = "Терминатор"
        booksCollector.add_new_book(book)

        assert booksCollector.get_book_genre(book) == ""

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_book_has_genre_correct_list(self, booksCollector, genre):
        for book in booksCollector.get_books_with_specific_genre(genre):
            assert booksCollector.books_genre.get(book) == genre

    def test_get_books_genre_correct_list(self, booksCollector):
        assert booksCollector.books_genre == booksCollector.get_books_genre()

    @pytest.mark.parametrize('book', ['Оно', 'Убийство на улице Морг'])
    def test_get_books_for_children_age_raiting_list_not_age_rated_films(self, book, booksCollector):
        assert book not in booksCollector.get_books_for_children()

    def test_add_book_in_favorites_book_in_books_genre_book_not_in_favorites_add_book(self, booksCollector):
        book = 'Убийство на улице Морг'
        booksCollector.add_book_in_favorites(book)
        assert book in booksCollector.favorites

    def test_add_book_in_favorites_book_not_in_books_genre_book_not_add(self, booksCollector):
        book = '1984'
        booksCollector.add_book_in_favorites(book)
        assert book not in booksCollector.favorites

    def test_add_book_add_book_twice_one_book_in_favorites(self, booksCollector):
        book_in_favorites = 'Бегущий в лабиринте'
        booksCollector.add_book_in_favorites(book_in_favorites)
        booksCollector.add_book_in_favorites(book_in_favorites)
        assert booksCollector.favorites.count(book_in_favorites) != 2

    def test_delete_book_from_favorites_list_favorites_book_book_delete(self, booksCollector):
        book = 'Убийство на улице Морг'
        booksCollector.delete_book_from_favorites(book)
        assert book not in booksCollector.favorites

    def test_get_list_of_favorites_books_list_favorites_book_get_list_of_favorites(self, booksCollector):
        booksCollector.add_book_in_favorites('Убийство на улице Морг')
        assert booksCollector.favorites == booksCollector.get_list_of_favorites_books()