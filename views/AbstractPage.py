class AbstractPage:
    """Abstract page class"""
    def show_page(self):
        """Abstract method for showing page (needs to be implemented in derived classes)"""
        raise NotImplementedError("show_page method not implemented")
