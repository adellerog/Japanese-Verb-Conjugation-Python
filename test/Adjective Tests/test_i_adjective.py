import unittest
from class_definitions.i_adjective import IAdjective as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.i_adjective = t('takai', 'i')

    def tearDown(self):
        del self.i_adjective

    def test_find_root(self):
        self.assertEqual(t.find_root(self.i_adjective), 'taka')

    def test_find_ku_form(self):
        self.assertEqual(t.find_ku_form(self.i_adjective), 'takaku')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.i_adjective), 'takakute')

    def test_check_plain_negative(self):
        self.assertEqual(self.i_adjective.plain_present_negative, 'takakunai')

    def test_check_polite_negative(self):
        self.assertEqual(self.i_adjective.polite_present_negative, 'takaku arimasen')

    def test_check_plain_past(self):
        self.assertEqual(self.i_adjective.plain_past, 'takakatta')

    def test_check_polite_past(self):
        self.assertEqual(self.i_adjective.polite_past, 'takakatta desu')

    def test_check_plain_neg_past(self):
        self.assertEqual(self.i_adjective.plain_past_negative, 'takakunakatta')

    def test_check_polite_neg_past(self):
        self.assertEqual(self.i_adjective.polite_past_negative, 'takaku arimasendeshita')

    def test_check_polite_present(self):
        self.assertEqual(self.i_adjective.polite_present, 'takai desu')

    def test_check_plain_present(self):
        self.assertEqual(self.i_adjective.plain_present, 'takai')


if __name__ == '__main__':
    unittest.main()