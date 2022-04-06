import unittest

from dataClasses.libs.module4.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.test_object = Stack(1)
        self.test_object_empty = Stack()

    def test_get_size(self):
        self.assertEqual(self.test_object.get_size(), 1)
        self.assertEqual(self.test_object_empty.get_size(), 0)

    def test_push(self):
        self.assertEqual(self.test_object.push(2), None)
        self.assertEqual(self.test_object.get_size(), 2)

    def test_peek(self):
        self.assertEqual(self.test_object.peek(), 1)
        self.assertEqual(self.test_object_empty.peek(), None)

    def test_pop(self):
        self.assertEqual(self.test_object.pop(), 1)
        self.assertEqual(self.test_object.get_size(), 0)

        self.assertRaises(IndexError, self.test_object_empty.pop)

    def test_contains(self):
        #self.assertEqual(self.test_object.contains(0), False)
        #self.assertEqual(self.test_object.contains(1), True)
        pass

    def test_lifecycle(self):
        # Create a stack
        self.stack = Stack(0)

        # Try to assign 10 values
        for i in range(0, 10):
            # All values shall be pushed
            self.assertEqual(self.stack.push(i), None)
            self.assertEqual(self.stack.get_size(), i+1)

        for i in range(9, -1, -1):
            self.assertEqual(self.stack.pop(), i)
            self.assertEqual(self.stack.get_size(), i)

        # Pop shall raise ValueError
        self.assertRaises(IndexError, self.stack.pop)

