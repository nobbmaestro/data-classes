# Module 8 - Trees

Trees are a very common data structure in the real world. They are very useful for storing data in a hierarchical manner. For example, you might have a tree that represents a company structure. Each node in the tree has a name, and each node can have a list of employees. And each employee can have a list of subordinates. But not just that, trees are the foundations of storage systems like SQL server and a critical part of searching. For example, when you search for something on YouTube, it auto-completes your word or sentence for you, right? Under the covers, it is basically walking through a special kind of tree called a Trie to produce those suggestions.

## Project - Trie

A **trie** (pronounced as "try") or **prefix tree** is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

- **Trie()** Initializes the trie object.

- **void insert(String word)** Inserts the string **word** into the trie.

- **boolean search(String word)** Returns **true** if the string **word** is in the trie (i.e., was inserted before), and false otherwise.

- **boolean startsWith(String prefix)** Returns **true** if there is a previously inserted string **word** that has the prefix **prefix**, and **false** otherwise.

### Examples:
>Input<br>
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]<br>
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]<br>
Output<br>
[null, null, true, false, true, null, true]<br>

Explanation
>Trie trie = new Trie();<br>
trie.insert("apple");<br>
trie.search("apple");   // return True<br>
trie.search("app");     // return False<br>
trie.startsWith("app"); // return True<br>
trie.insert("app");<br>
trie.search("app");     // return True<br>


# Resources

- [Tree data structure @ CMU](https://www.cs.cmu.edu/~clo/www/CMU/DataStructures/Lessons/lesson4_1.htm)

- [What is a Tree Data structure?](https://afteracademy.com/blog/what-is-a-tree-data-structure)

- [Trees in Python](https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/)

- [Trees at Coursera](https://www.coursera.org/lecture/data-structures/trees-95qda)

# Self Assessment

- [Binary Tree Inorder Traversal](https://www.engineeringwithutsav.com/Binary%20Tree%20Inorder%20Traversal)

- [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal)

- [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal)

- [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

- [Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers)

- [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)

- [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths)

- [Same Tree](https://leetcode.com/problems/same-tree)

- [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree)

- [Path Sum](https://leetcode.com/problems/path-sum)

- [Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree)

- [Maximum Depth of N-ary Tree](https://leetcode.com/problems/maximum-depth-of-n-ary-tree)