import unittest
from class_definitions.verb import Verb as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.verb = t('kiku', 'kikimasu')

    def tearDown(self):
        del self.verb

    def test_find_root(self):
        self.assertEqual(t.find_root(self.verb), 'kik')

    def test_determine_type(self):
        self.assertEqual(t.determine_type(self.verb), 'godan')

    def test_find_pre_masu_stem(self):
        self.assertEqual(t.find_pre_masu_stem(self.verb), 'kiki')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.verb), 'kiite')

    def test_find_plain_negative(self):
        self.assertEqual(t.find_plain_negative(self.verb), 'kikanai')

    def test_find_polite_negative(self):
        self.assertEqual(t.find_polite_negative(self.verb), 'kikimasen')

    def test_find_plain_past(self):
        self.assertEqual(t.find_plain_past(self.verb), 'kiita')

    def test_find_polite_past(self):
        self.assertEqual(t.find_polite_past(self.verb), 'kikimashita')

    def test_find_plain_neg_past(self):
        self.assertEqual(t.find_plain_neg_past(self.verb), 'kikanakatta')

    def test_find_polite_neg_past(self):
        self.assertEqual(t.find_polite_neg_past(self.verb), 'kikimasendeshita')

    def test_find_volitional(self):
        self.assertEqual(t.find_volitional(self.verb), 'kikitai')



if __name__ == '__main__':
    unittest.main()