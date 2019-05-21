import unittest

from book import Book

class TestBookMethods(unittest.TestCase):
  
    def test_not_equal(self):
        book = Book(author='Melville, Herman', title='Moby-Dick')
        self.assertNotEqual(book, Book())

    def test_equal(self):
        book = Book(author='Melville, Herman', title='Moby-Dick')
        self.assertEqual(book, Book('Moby-Dick', 'Melville, Herman'))

    def test_less_than(self):
        book = Book(title='2001: A Space Odyssey', author='Clarke, Arthur C.')
        self.assertLess(book, Book('2010: Odyssey Two', 'Clarke, Arthur C.'))

    def test_greater_than(self):
        book = Book(title='Great Expectations', author='Dickens, Charles')
        self.assertGreater(book, Book('Great Expectations', 'Acker, Kathy'))

if __name__ == '__main__':
    unittest.main()