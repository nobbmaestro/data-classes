# Module 5 - Queues

Queues are pretty self-explanatory and quite common as well. How many of you tried buying a Playstation 5 when it released in the summer of 2020, and got hit with the dreaded "You have been added to a queue... do not refresh the browser" message? What is happening there? Well, because so many people rushed to buy the product at the same time, the web server reached its capacity and could not handle any more traffic. But instead of just erroring out, the load balancer redirected you to a temporary queue, which is a FIFO (First in, First out) data structure. As traffic improves in the web server, the queue is "dequeued", letting the first person that got put in the queue through to the website, then the second, then third ... just like a queue in the shopping mall.

## Project - Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out) principle and the last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the **MyCircularQueue** class:

- **MyCircularQueue(k)** Initializes the object with the size of the queue to be **k**.

- **int Front()** Gets the front item from the queue. If the queue is empty, return -1.

- **int Rear()** Gets the last item from the queue. If the queue is empty, return -1.

- **boolean enQueue(int value)** Inserts an element into the circular queue. Return true if the operation is successful.

- **boolean deQueue()** Deletes an element from the circular queue. Return true if the operation is successful.

- **boolean isEmpty()** Checks whether the circular queue is empty or not.

- **boolean isFull()** Checks whether the circular queue is full or not.

You must solve the problem without using the built-in queue data structure in your programming language. 

### Examples:
**Input**
>["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]<br>
[[3], [1], [2], [3], [4], [], [], [], [4], []]

**Output**
>null, true, true, true, false, 3, true, true, true, 4]

**Explanation**
>MyCircularQueue myCircularQueue = new MyCircularQueue(3);<br>
myCircularQueue.enQueue(1); // return True<br>
myCircularQueue.enQueue(2); // return True<br>
myCircularQueue.enQueue(3); // return True<br>
myCircularQueue.enQueue(4); // return False<br>
myCircularQueue.Rear();     // return 3<br>
myCircularQueue.isFull();   // return True<br>
myCircularQueue.deQueue();  // return True<br>
myCircularQueue.enQueue(4); // return True<br>
myCircularQueue.Rear();     // return 4<br>

## Resources

- [Queue Python Documentation](https://docs.python.org/3/library/queue.html)

- [Queues in Python](https://www.educba.com/queue-in-python/)

- [Python Queues](https://www.youtube.com/watch?v=XLXWidXVRJk)

## Self Assessment

- [Implement queue using stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

- [First unique character in a string](https://leetcode.com/problems/first-unique-character-in-a-string/)

- [Time needed to buy tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/)