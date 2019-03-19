import unittest

import ex01

class TestEx01Methods(unittest.TestCase):
    
    # TODO: replace ValueError with the correct Exception type
    def test_no_default_empty_init(self):
        with self.assertRaises(TypeError):
            ex01.NoDefault()

    # TODO: invoke NoDefault() with fld_1 set to expected value
    def test_no_default_init_fld_1(self):
        self.assertEqual(ex01.NoDefault(fld_1=42).fld_1, 42)

    def test_with_default_init_fld_1(self):
        self.assertEqual(ex01.WithDefault().fld_1, 42)

    def test_with_default_init_fld_2(self):
        self.assertEqual(ex01.WithDefault().fld_2, 'hello')

    # TODO: invoke WithDefault() with fld_1 set to expected value
    def test_with_default_assign_fld_1(self):
        self.assertEqual(ex01.WithDefault(fld_1=-28).fld_1, -28)

    # TODO: invoke WithDefault() with fld_2 set to expected value
    def test_with_default_assign_fld_2(self):
        self.assertEqual(ex01.WithDefault(fld_2='world').fld_2, 'world')

    def test_with_method(self):
        self.assertAlmostEqual(ex01.WithMethod().fld_sum(), 2.12132034)


if __name__ == '__main__':
    unittest.main()