import unittest
from class_definitions.verb import Verb as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.verb = t('suru', 'shimasu')

    def tearDown(self):
        del self.verb

    def test_find_root(self):
        self.assertEqual(t.find_root(self.verb), 'su')

    def test_determine_type(self):
        self.assertEqual(t.determine_type(self.verb), 'irregular')

    def test_find_pre_masu_stem(self):
        self.assertEqual(t.find_pre_masu_stem(self.verb), 'shi')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.verb), 'shite')

    def test_find_plain_negative(self):
        self.assertEqual(t.find_plain_negative(self.verb), 'shinai')

    def test_find_polite_negative(self):
        self.assertEqual(t.find_polite_negative(self.verb), 'shimasen')

    def test_find_plain_past(self):
        self.assertEqual(t.find_plain_past(self.verb), 'shita')

    def test_find_polite_past(self):
        self.assertEqual(t.find_polite_past(self.verb), 'shimashita')

    def test_find_plain_neg_past(self):
        self.assertEqual(t.find_plain_neg_past(self.verb), 'shinakatta')

    def test_find_polite_neg_past(self):
        self.assertEqual(t.find_polite_neg_past(self.verb), 'shimasendeshita')

    def test_find_volitional(self):
        self.assertEqual(t.find_volitional(self.verb), 'shitai')



if __name__ == '__main__':
    unittest.main()