import unittest
from class_definitions.i_adjective import IAdjective as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.i_adjective = t('ii', 'i')

    def tearDown(self):
        del self.i_adjective

    def test_find_root(self):
        self.assertEqual(t.find_root(self.i_adjective), 'yo')

    def test_find_ku_form(self):
        self.assertEqual(t.find_ku_form(self.i_adjective), 'yoku')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.i_adjective), 'yokute')

    def test_check_plain_negative(self):
        self.assertEqual(self.i_adjective.plain_present_negative, 'yokunai')

    def test_check_polite_negative(self):
        self.assertEqual(self.i_adjective.polite_present_negative, 'yoku arimasen')

    def test_check_plain_past(self):
        self.assertEqual(self.i_adjective.plain_past, 'yokatta')

    def test_check_polite_past(self):
        self.assertEqual(self.i_adjective.polite_past, 'yokatta desu')

    def test_check_plain_neg_past(self):
        self.assertEqual(self.i_adjective.plain_past_negative, 'yokunakatta')

    def test_check_polite_neg_past(self):
        self.assertEqual(self.i_adjective.polite_past_negative, 'yoku arimasendeshita')

    def test_check_polite_present(self):
        self.assertEqual(self.i_adjective.polite_present, 'ii desu')

    def test_check_plain_present(self):
        self.assertEqual(self.i_adjective.plain_present, 'ii')


if __name__ == '__main__':
    unittest.main()