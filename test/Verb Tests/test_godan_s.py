import unittest
from class_definitions.verb import Verb as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.verb = t('hanasu', 'hanashimasu')

    def tearDown(self):
        del self.verb

    def test_find_root(self):
        self.assertEqual(t.find_root(self.verb), 'hanas')

    def test_determine_type(self):
        self.assertEqual(t.determine_type(self.verb), 'godan')

    def test_find_pre_masu_stem(self):
        self.assertEqual(t.find_pre_masu_stem(self.verb), 'hanashi')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.verb), 'hanashite')

    def test_find_plain_negative(self):
        self.assertEqual(t.find_plain_negative(self.verb), 'hanasanai')

    def test_find_polite_negative(self):
        self.assertEqual(t.find_polite_negative(self.verb), 'hanashimasen')

    def test_find_plain_past(self):
        self.assertEqual(t.find_plain_past(self.verb), 'hanashita')

    def test_find_polite_past(self):
        self.assertEqual(t.find_polite_past(self.verb), 'hanashimashita')

    def test_find_plain_neg_past(self):
        self.assertEqual(t.find_plain_neg_past(self.verb), 'hanasanakatta')

    def test_find_polite_neg_past(self):
        self.assertEqual(t.find_polite_neg_past(self.verb), 'hanashimasendeshita')

    def test_find_volitional(self):
        self.assertEqual(t.find_volitional(self.verb), 'hanashitai')



if __name__ == '__main__':
    unittest.main()