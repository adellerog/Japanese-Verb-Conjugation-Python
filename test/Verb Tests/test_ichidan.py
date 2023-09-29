import unittest
from class_definitions.verb import Verb as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.verb = t('kiru', 'kimasu')

    def tearDown(self):
        del self.verb

    def test_find_root(self):
        self.assertEqual(t.find_root(self.verb), 'ki')

    def test_determine_type(self):
        self.assertEqual(t.determine_type(self.verb), 'ichidan')

    def test_find_pre_masu_stem(self):
        self.assertEqual(t.find_pre_masu_stem(self.verb), 'ki')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.verb), 'kite')

    def test_find_plain_negative(self):
        self.assertEqual(t.find_plain_negative(self.verb), 'kinai')

    def test_find_polite_negative(self):
        self.assertEqual(t.find_polite_negative(self.verb), 'kimasen')

    def test_find_plain_past(self):
        self.assertEqual(t.find_plain_past(self.verb), 'kita')

    def test_find_polite_past(self):
        self.assertEqual(t.find_polite_past(self.verb), 'kimashita')

    def test_find_plain_neg_past(self):
        self.assertEqual(t.find_plain_neg_past(self.verb), 'kinakatta')

    def test_find_polite_neg_past(self):
        self.assertEqual(t.find_polite_neg_past(self.verb), 'kimasendeshita')

    def test_find_volitional(self):
        self.assertEqual(t.find_volitional(self.verb), 'kitai')



if __name__ == '__main__':
    unittest.main()