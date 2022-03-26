class Node(object):
    """A Node of a Linked List

        Args:
            data (any type): Data to be stored
            next_node (any type, optional): Pointer to the next Node. Defaults to None.
        """
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        """Returns the next Node

        Returns:
            any type: the next Node
        """
        return self.next_node

    def set_next(self, next_node):
        """Set the next Node

        Args:
            next_node (any type): the next Node
        """
        self.next_node = next_node

    def get_data(self):
        """Returns the data of the Node

        Returns:
            any type: the data of the Node
        """
        return self.data

    def set_data(self, data):
        """Set the data of the Node

        Args:
            data (any type): the data of the Node
        """
        self.data = data