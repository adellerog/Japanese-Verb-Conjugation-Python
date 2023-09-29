import unittest
from class_definitions.verb import Verb as t


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.verb = t('iku', 'ikimasu')

    def tearDown(self):
        del self.verb

    def test_find_root(self):
        self.assertEqual(t.find_root(self.verb), 'ik')

    def test_determine_type(self):
        self.assertEqual(t.determine_type(self.verb), 'irregular')

    def test_find_pre_masu_stem(self):
        self.assertEqual(t.find_pre_masu_stem(self.verb), 'iki')

    def test_find_te_form(self):
        self.assertEqual(t.find_te_form(self.verb), 'itte')

    def test_find_plain_negative(self):
        self.assertEqual(t.find_plain_negative(self.verb), 'ikanai')

    def test_find_polite_negative(self):
        self.assertEqual(t.find_polite_negative(self.verb), 'ikimasen')

    def test_find_plain_past(self):
        self.assertEqual(t.find_plain_past(self.verb), 'itta')

    def test_find_polite_past(self):
        self.assertEqual(t.find_polite_past(self.verb), 'ikimashita')

    def test_find_plain_neg_past(self):
        self.assertEqual(t.find_plain_neg_past(self.verb), 'ikanakatta')

    def test_find_polite_neg_past(self):
        self.assertEqual(t.find_polite_neg_past(self.verb), 'ikimasendeshita')

    def test_find_volitional(self):
        self.assertEqual(t.find_volitional(self.verb), 'ikitai')



if __name__ == '__main__':
    unittest.main()