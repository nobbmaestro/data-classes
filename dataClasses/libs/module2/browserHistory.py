from .linkedList import LinkedList

class BrowserHistory(object):
    """Browser History - stores the browser activity

        Args:
            homepage (str): the homepage
        """
    def __init__(self, homepage: str):
        
        self.browserHistory_forward = LinkedList(homepage)
        self.browserHistory_backward = LinkedList(homepage)

    def visit(self, url: str):
        """The visit request. The given URL to be stored in the history. 

        Args:
            url (str): url of the website
        """
        self.browserHistory_forward = LinkedList(url)
        self.browserHistory_backward.add(url)

    def back(self, steps: int):
        """Backs the history of n given steps. If steps is greater than the history lenght, the last website will be returned.

        Args:
            steps (int): the number of steps to move back in history

        Returns:
            str: the URL of the resulting website.
        """
        current_url = self.browserHistory_backward.get_root()
        for i in range(steps):
            next_url = current_url.get_next()
            self.browserHistory_backward.remove(current_url.get_data())
            if next_url == None:
                return current_url.get_data()
            else:
                self.browserHistory_forward.add(next_url.get_data())
                current_url = next_url

        return current_url.get_data()

    def forward(self, steps: int):
        """Moves forward in the history of n given steps. If steps is greater than the history lenght, the last website will be returned.

        Args:
            steps (int): the number of steps to move forward in history

        Returns:
            str: the URL of the resulting website.
        """
        current_url = self.browserHistory_forward.get_root()
        for i in range(steps):
            next_url = current_url.get_next()
            self.browserHistory_forward.remove(current_url.get_data())
            if next_url == None:
                return current_url.get_data()
            else:
                self.browserHistory_backward.add(next_url.get_data())
                current_url = next_url

        return current_url.get_data()