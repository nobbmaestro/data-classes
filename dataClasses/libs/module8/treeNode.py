class TNode(object):
    """Node of a Trie.

    Stored elements:
        char (str): stored character. None if root Node.
        children (dict): Dictionary of childrens where char key points to child instance.
        end_of_word (boolean): Indication for end of word.
        counter (int): Counting number of usage. 

    Args:
        char (str): Character to be stored in the Node.
    """
    def __init__(self, char: str = None):
        self.char = char
        self.children = {}
        self.end_of_word = False
        self.counter = 0