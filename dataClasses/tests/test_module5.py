import unittest

from dataClasses.libs.module5.queue import Queue
from dataClasses.libs.module5.myCircularQueue import MyCircularQueue

class TestMyCircularQueue(unittest.TestCase):
    def setUp(self):
        # set up emtry MyCircularQueue
        self.test_object_empty = MyCircularQueue(3)

        # set up full MyCircularQueue
        self.test_object_full = MyCircularQueue(3)
        self.test_object_full.enqueue('1st')
        self.test_object_full.enqueue('2nd')
        self.test_object_full.enqueue('3rd')

        # set up test from example
        self.cmd = {
            0: "MyCircularQueue", 
            1: "enqueue", 
            2: "enqueue", 
            3: "enqueue", 
            4: "enqueue", 
            5: "rear", 
            6: "is_full", 
            7: "dequeue", 
            8: "enqueue", 
            9: "rear"
        }
        self.input = {
            0: 3, 
            1: 1, 
            2: 2, 
            3: 3, 
            4: 4, 
            5: "", 
            6: "", 
            7: "", 
            8: 4, 
            9: ""
        }
        self.output = {
            0: None, 
            1: True, 
            2: True, 
            3: True, 
            4: False, 
            5: 3, 
            6: True, 
            7: True, 
            8: True, 
            9: 4
        }

    def test_method_front(self):
        self.assertEqual(self.test_object_empty.front(), -1)
        self.assertEqual(self.test_object_full.front(), '1st')

    def test_method_rear(self):
        self.assertEqual(self.test_object_empty.rear(), -1)
        self.assertEqual(self.test_object_full.rear(), '3rd')

    def test_method_enqueue(self):
        self.assertEqual(self.test_object_empty.enqueue('New data'), True)
        self.assertEqual(self.test_object_full.enqueue('New data'), False)

    def test_method_dequeue(self):
        self.assertEqual(self.test_object_empty.dequeue(), False)
        self.assertEqual(self.test_object_full.dequeue(), True)

    def test_method_is_empty(self):
        self.assertEqual(self.test_object_empty.is_full(), False)
        self.assertEqual(self.test_object_full.is_full(), True)

    def test_method_is_full(self):
        self.assertEqual(self.test_object_empty.is_empty(), True)
        self.assertEqual(self.test_object_full.is_empty(), False)

    def test_lifecycle(self):
        to_eval = "test_object.{cmd}({input})"
        for i in range(9):
            if i == 0:
                test_object = eval(self.cmd[i] + "(" + str(self.input[i]) + ")")
            else:
                self.assertEqual(eval(to_eval.format(cmd=self.cmd[i], input=self.input[i])), self.output[i])

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
        self.assertEqual(self.test_object.contains(0), True)
        self.assertEqual(self.test_object.contains(1), False)

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
                self.assertEqual(self.queue.is_full(), True)

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
        self.assertEqual(self.test_object.contains(0), True)
        self.assertEqual(self.test_object.contains(1), False)
        

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