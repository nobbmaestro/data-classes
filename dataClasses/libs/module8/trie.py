from .treeNode import TNode

class Trie(object):
    def __init__(self):
        self.root = TNode()

    def insert(self, string: str):
        """Inserts arg string into the trie. If arg string is a list of strings, the elements will be inserted recursively.

        Args:
            string (str, list): keyword, or list of keywords to be inserted.

        Raises:
            ValueError: arg is not of type str
        """
        if type(string) is list:
            for word in string:
                self.insert(word)
        elif type(string) is not str:
            raise ValueError('arg is not of type str')

        else:
            ptr = self.root
            for char in string:
                if char in ptr.children:
                    ptr = ptr.children[char]
                    ptr.counter += 1
                else:
                    new_node = TNode(char)
                    ptr.children[char] = new_node
                    ptr = new_node 

            ptr.end_of_word = True
    
    def search(self, string: str):
        """Searches for the arg string by traversing the nodes in the trie. 

        Args:
            string (str): search keyword.

        Returns:
            bool: True if string in the trie and end of word.
        """
        ptr = self.root
        for char in string:
            if char not in ptr.children:
                return False
            else:
                ptr = ptr.children[char]

        if ptr.end_of_word:
            return True
        else:
            return False
        
    def starts_with(self, string: str):
        """Searches for the arg string by traversing the nodes in the trie. Returns true regardless of the keyword is at end of the word or not.

        Args:
            string (str): search keyword.

        Returns:
            bool: True if string in the trie
        """
        ptr = self.root
        for char in string:
            if char not in ptr.children:
                return False
            else:
                ptr = ptr.children[char]
                
        return True