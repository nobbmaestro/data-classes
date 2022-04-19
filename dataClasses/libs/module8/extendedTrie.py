from dataClasses.libs.module8.trie import Trie

class ExtendedTrie(Trie):
    def __to_flat_list(self, unflat_list):
        """Converts an unflat list to a flat list.

        Args:
            unflat_list (list): Unflat list

        Returns:
            list: Converted flat list
        """
        flat_list = []
        for element in unflat_list:
            if type(element) is list:
                flat_list.extend(self.__to_flat_list(element))
            else:
                flat_list.append(element)
        
        return flat_list

    def __get_node_at_string(self, string: str):
        """Searches for the arg string by traversing the nodes in the trie.

        Args:
            string (str): search keyword.

        Returns:
            if string exists in trie:
                Node (TNode): Node in the trie at keyword.
            else
                (boolean): False
        """
        ptr = self.root
        for char in string:
            if char not in ptr.children:
                return False
            else:
                ptr = ptr.children[char]
                
        return ptr

    def list_words(self, ptr = None, word = None):
        """Returns a list of words in the trie. Search process is done by traversing the trie recursively.

        Args:
            ptr (TNode, optional): _description_. Defaults to None.
            word (str, optional): _description_. Defaults to None.

        Returns:
            list: list of words stored in the trie.
        """
        if ptr is None:
            ptr = self.root
        
        if word is None:
            word = ''

        list_of_words = []
        if ptr.end_of_word:
            if ptr.children == {}:
                return word
            else:
                list_of_words.append(word)
        
        for char in list(ptr.children.keys()):
            tmp = word
            tmp += char
            list_of_words.append(self.list_words(ptr.children[char], tmp))

        return self.__to_flat_list(list_of_words)

    def suggest(self, string: str):
        """Returns a list of suggestions based on keyword.

        Args:
            string (str): The keyword

        Returns:
            list: list of suggestions
        """
        if self.starts_with(string):
            ptr = self.__get_node_at_string(string)
            return self.list_words(ptr, string)

        else:
            return None