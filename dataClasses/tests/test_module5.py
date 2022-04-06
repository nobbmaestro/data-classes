import unittest

from dataClasses.libs.module5.queue import Queue

class TestFiniteQueue(unittest.TestCase):
    def setUp(self):
        self.test_object = Queue(5)
        self.test_object.enqueue(0)

    def test_get_size(self):
        self.assertEqual(self.test_object.get_size(), 1)

    def test_enqueue(self):
        self.assertEqual(self.test_object.enqueue(1), True)

    def test_peek(self):
        self.assertEqual(self.test_object.peek(), 0)

    def test_dequeue(self):
        self.assertEqual(self.test_object.dequeue(), 0)

    def test_contains(self):
        #self.assertEqual(self.test_object.contains(0), False)
        #self.assertEqual(self.test_object.contains(1), True)
        pass

    def test_lifecycle(self):
        # Create an queue of len 5
        self.queue = Queue(5)

        # Try to assign 10 values
        for i in range(0, 10):
            # First 5 values shall be enqueued
            if i < 5:
                self.assertEqual(self.queue.enqueue(i), True)
            # For 6th value and above, IndexError shall be raised
            else:
                self.assertRaises(IndexError, self.queue.enqueue, i)

        # First value to dequeue shall be 0
        self.assertEqual(self.queue.peek(), 0)
        self.assertEqual(self.queue.get_size(), 5)

        # Try to enqueue additional value, it shall raise IndexError 
        self.assertRaises(IndexError, self.queue.enqueue, 100)

        # Dequeue shall return 0 and reduce the size to 4
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.get_size(), 4)

        # Try to enqueue additional value, it shall return True
        self.assertEqual(self.queue.enqueue(101), True)
        self.assertEqual(self.queue.get_size(), 5)

        # Dequeue shall return 1
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.get_size(), 4)

        # Dequeue shall return 2
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.get_size(), 3)

        # Dequeue shall return 3
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.get_size(), 2)

        # Dequeue shall return 4
        self.assertEqual(self.queue.dequeue(), 4) 
        self.assertEqual(self.queue.get_size(), 1)

        # Dequeue shall return 100
        self.assertEqual(self.queue.dequeue(), 101) 
        self.assertEqual(self.queue.get_size(), 0)

        # Dequeue shall raise IndexError
        self.assertRaises(IndexError, self.queue.dequeue) 

class TestInfiniteQueue(unittest.TestCase):
    def setUp(self):
        self.test_object = Queue()
        self.test_object.enqueue(0)

    def test_get_size(self):
        self.assertEqual(self.test_object.get_size(), 1)

    def test_enqueue(self):
        self.assertEqual(self.test_object.enqueue(1), True)

    def test_peek(self):
        self.assertEqual(self.test_object.peek(), 0)

    def test_dequeue(self):
        self.assertEqual(self.test_object.dequeue(), 0)

    def test_contains(self):
        #self.assertEqual(self.test_object.contains(0), False)
        #self.assertEqual(self.test_object.contains(1), True)
        pass

    def test_lifecycle(self):
        # Create an queue of len 5
        self.queue = Queue()

        # Try to assign 10 values
        for i in range(0, 10):
            # All values shall be enqueued
            self.assertEqual(self.queue.enqueue(i), True)
            self.assertEqual(self.queue.get_size(), i+1)

        j = 9
        for i in range(0, 10):
            self.assertEqual(self.queue.dequeue(), i)
            self.assertEqual(self.queue.get_size(), j-i)

        # Dequeue shall raise IndexError
        self.assertRaises(IndexError, self.queue.dequeue) 