import unittest
from class_definitions.verb import Verb as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.verb = t('nomu', 'nomimasu')

    def tearDown(self):
        del self.verb

    def test_find_root(self):
        self.assertEqual(t.find_root(self.verb), 'nom')

    def test_determine_type(self):
        self.assertEqual(t.determine_type(self.verb), 'godan')

    def test_find_pre_masu_stem(self):
        self.assertEqual(t.find_pre_masu_stem(self.verb), 'nomi')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.verb), 'nonde')

    def test_find_plain_negative(self):
        self.assertEqual(t.find_plain_negative(self.verb), 'nomanai')

    def test_find_polite_negative(self):
        self.assertEqual(t.find_polite_negative(self.verb), 'nomimasen')

    def test_find_plain_past(self):
        self.assertEqual(t.find_plain_past(self.verb), 'nonda')

    def test_find_polite_past(self):
        self.assertEqual(t.find_polite_past(self.verb), 'nomimashita')

    def test_find_plain_neg_past(self):
        self.assertEqual(t.find_plain_neg_past(self.verb), 'nomanakatta')

    def test_find_polite_neg_past(self):
        self.assertEqual(t.find_polite_neg_past(self.verb), 'nomimasendeshita')

    def test_find_volitional(self):
        self.assertEqual(t.find_volitional(self.verb), 'nomitai')



if __name__ == '__main__':
    unittest.main()