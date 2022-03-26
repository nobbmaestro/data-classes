# Module 2 - Linked Lists

Linked lists don't get enough love, but they are quite handy data structures, especially you are unsure about the size or the capacity ahead of time. Are you the kind that has 100 tabs open in your browser? Well, then you've been using Linked Lists daily. When you press Ctrl + Tab to cycle between those tabs, you are basically making your way through a circular linked list.

## Project - Browser History

You have a **browser** of one tab where you start on the **homepage** and you can visit another **url**, get back in the history number of **steps** or move forward in the history number of **steps**.

Implement the **BrowserHistory** class:

 - **BrowserHistory(string homepage)** Initializes the object with the **homepage** of the browser.

 - **void visit(string url)** Visits **url** from the current page. It clears up all the forward history.

 - **string back(int steps)** Move **steps** back in history. If you can only return x steps in the history and **steps > x**, you will return  only x steps. Return the current **url** after moving back in history **at most steps**.

 - **string forward(int steps)** Move **steps** forward in history. If you can only forward x steps in the history and **steps > x**, you will forward only x steps. Return the current **url** after forwarding in history **at most steps**.

### Examples:

Input:
>["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]<br>[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

Output:
>[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
> BrowserHistory browserHistory = new BrowserHistory("leetcode.com");<br>
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"<br>
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"<br>
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"<br>
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"<br>
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"<br>
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"<br>
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"<br>
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.<br>
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"<br>
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

## Resources

 - [Singly Linked Lists at Coursera](https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK)

 - [CS 61B Linked Lists I](https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0)

 - [CS 61B Linked Lists II](https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w)

 - [Linked Lists vs Arrays](https://www.coursera.org/lecture/data-structures-optimizing-performance/core-linked-lists-vs-arrays-rjBs9)

 - [Doubly Linked Lists](https://www.coursera.org/lecture/data-structures/doubly-linked-lists-jpGKD)

 - [More Linked Lists](https://brilliant.org/wiki/linked-lists/)

 - [Implementation of Linked Lists](https://www.freecodecamp.org/news/implementing-a-linked-list-in-javascript/)

 - [Linked Lists in Python](https://realpython.com/linked-lists-python/)

## Self Assessment

 - [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

 - [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/)

 - [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

 - [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

 - [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)

 - [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements)