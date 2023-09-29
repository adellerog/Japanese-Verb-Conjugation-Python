import unittest
from class_definitions.na_adjective import NaAdjective as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.i_adjective = t('kirei', 'na')

    def tearDown(self):
        del self.i_adjective

    def test_find_root(self):
        self.assertEqual(t.find_root(self.i_adjective), 'kirei')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.i_adjective), 'kireide')

    def test_check_plain_negative(self):
        self.assertEqual(self.i_adjective.plain_present_negative, 'kirei ja nai')

    def test_check_polite_negative(self):
        self.assertEqual(self.i_adjective.polite_present_negative, 'kirei dewa arimasen')

    def test_check_plain_past(self):
        self.assertEqual(self.i_adjective.plain_past, 'kirei datta')

    def test_check_polite_past(self):
        self.assertEqual(self.i_adjective.polite_past, 'kirei deshita')

    def test_check_plain_neg_past(self):
        self.assertEqual(self.i_adjective.plain_past_negative, 'kirei ja nakatta')

    def test_check_polite_neg_past(self):
        self.assertEqual(self.i_adjective.polite_past_negative, 'kirei dewa arimasendeshita')

    def test_check_polite_present(self):
        self.assertEqual(self.i_adjective.polite_present, 'kirei desu')

    def test_check_plain_present(self):
        self.assertEqual(self.i_adjective.plain_present, 'kirei da'
                                                         '')


if __name__ == '__main__':
    unittest.main()