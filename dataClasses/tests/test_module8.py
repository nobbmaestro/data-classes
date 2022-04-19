import unittest

from dataClasses.libs.module8.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.test_object = Trie()
        self.elements = ['apple', 'orange', [['banana']]]

    def test_insert(self):
        self.assertIsNone(self.test_object.insert(self.elements[0]))
        self.assertIsNone(self.test_object.insert(self.elements))

        self.assertRaises(ValueError, self.test_object.insert, 1)
        self.assertRaises(ValueError, self.test_object.insert, [1])
        self.assertRaises(ValueError, self.test_object.insert, [[1], 1])

    def test_search(self): 
        self.test_object.insert(self.elements)
        search_keywords = ['apple', 'app', 'orange', 'banana']
        expected_results = [True, False, True, True]
        for i in range(len(expected_results)):
            self.assertEqual(self.test_object.search(search_keywords[i]), expected_results[i])

    def test_starts_with(self):
        self.test_object.insert(self.elements)
        search_keywords = ['apple', 'app', 'orange', 'banana']
        expected_results = [True, True, True, True]
        for i in range(len(expected_results)):
            self.assertEqual(self.test_object.starts_with(search_keywords[i]), expected_results[i])


