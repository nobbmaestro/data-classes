import unittest

from dataClasses.libs.module8.trie import Trie
from dataClasses.libs.module8.extendedTrie import ExtendedTrie

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

class TestExtendedTrie(unittest.TestCase):
    def setUp(self):
        self.test_object = ExtendedTrie()
        self.omxs30 = [
            "ABB Ltd",
            "Alfa Laval",
            "Assa Abloy B",
            "Astra Zeneca",
            "Atlas Copco A",
            "Atlas Copco B",
            "Autoliv Inc. SDB",
            "Boliden Råvaror",
            "Electrolux B",
            "Ericsson B",
            "Essity B",
            "Evolution",
            "Getinge Teknik",
            "Hennes & Mauritz B",
            "Hexagon AB B",
            "Investor B",
            "Kinnevik B",
            "Nordea Bank",
            "Sandvik Industri",
            "Sinch AB",
            "SEB A",
            "Skanska B",
            "SKF B",
            "SCA B",
            "Svenska Handelsbanken A",
            "Swedbank A",
            "Swedish Match",
            "Tele2 B",
            "Telia Company",
            "Volvo B",
        ]

    def test_insert_and_search (self):
        msg = "{company} was not found."
        for company in self.omxs30:
            self.assertIsNone(self.test_object.insert(company))
            self.assertEqual(self.test_object.search(company), True, msg.format(company=company))

        for company in self.omxs30:
            self.assertEqual(self.test_object.search(company), True, msg.format(company=company))

    def test_suggest(self):
        self.test_object.insert(self.omxs30)

        keyword = 'Swedbank A'
        expected_outputs = {
            'S'         : ["Sandvik Industri", "Sinch AB", "SEB A", "Skanska B", "SKF B","SCA B", "Svenska Handelsbanken A", "Swedbank A", "Swedish Match"],
            'Sw'        : ["Swedbank A", "Swedish Match"],
            'Swe'       : ["Swedbank A", "Swedish Match"],
            'Swed'      : ["Swedbank A", "Swedish Match"],
            'Swedb'     : ["Swedbank A"],
            'Swedba'    : ["Swedbank A"],
            'Swedban'   : ["Swedbank A"],
            'Swedbank'  : ["Swedbank A"],
            'Swedbank ' : ["Swedbank A"],
            'Swedbank A': ["Swedbank A"]
        }

        msg = "failed at keyword '{keyword}'."
        for i in range(1, len(keyword)):
            self.assertEqual(self.test_object.suggest(keyword[:i]), expected_outputs[keyword[:i]], msg.format(keyword=keyword[:i]))