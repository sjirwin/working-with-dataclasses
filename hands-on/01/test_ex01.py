import unittest

import ex01

class TestEx01NoDefault(unittest.TestCase):

    # TODO: replace ValueError with the correct Exception type
    def test_empty_init(self):
        with self.assertRaises(ValueError):
            ex01.NoDefault()

    # TODO: invoke NoDefault() with fld_1 set to expected value
    def test_init_fld_1(self):
        self.assertEqual(ex01.NoDefault(fld_1=None).fld_1, 42)

class TestEx01WithDefault(unittest.TestCase):

    def test_init_fld_1(self):
        self.assertEqual(ex01.WithDefault().fld_1, 42)

    def test_init_fld_2(self):
        self.assertEqual(ex01.WithDefault().fld_2, 'hello')

    # TODO: invoke WithDefault() with fld_1 set to expected value
    def test_assign_fld_1(self):
        self.assertEqual(ex01.WithDefault().fld_1, -28)

    # TODO: invoke WithDefault() with fld_2 set to expected value
    def test_assign_fld_2(self):
        self.assertEqual(ex01.WithDefault().fld_2, 'world')

    # TODO: correct the field values in the assert's expected value (second WithDefault())
    def test_eq(self):
        self.assertEqual(ex01.WithDefault(), ex01.WithDefault(fld_1=0,fld_2=''))

    # TODO: correct the expected string in the assertEqual()
    def test_repr(self):
        self.assertEqual(str(ex01.WithDefault()), "")

class TestEx01WithMethod(unittest.TestCase):

    def test_fld_sum(self):
        self.assertAlmostEqual(ex01.WithMethod().fld_sum(), 2.12132034)

if __name__ == '__main__':
    unittest.main()