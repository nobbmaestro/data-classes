from .node import Node

class LinkedList(object):
    """A Linked List

        Args:
            root (any type, optional): The root Node. Defaults to None.
    """
    def __init__(self, root = None):
       self.root = Node(root)
       self.size = 0

    def get_size(self):
        """Returns the size of the Linked List

        Returns:
           int: the size of the Linked List
        """
        return self.size

    def get_root(self):
        """Get root Node of the Linked List

        Returns:
            Node: The root Node
        """
        return self.root

    def add(self, data):
        """Adds new Node to the Linked List

        Args:
            data (any type): data to be stored
        """
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        """Removes the given Node from the Linked List

        Args:
            data (any type): Data to be removed from the Linked List

        Returns:
            boolean: True if removed successfully, else False.
        """
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            
            else:
                prev_node = this_node
                this_node = this_node.get_next()

        return False 
                
    def find(self, data):
        """Searches for the given data in the Linked List

        Args:
            data (any type): Data to be searched

        Returns:
            any type: the data of the Node if found, else None
        """
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return data
            else:
                this_node = this_node.get_next()
        return None