from matplotlib import markers


class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        """
        You can reuse the method we implemented previously.
        """
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_start_from_list(self):
        """
        Implement this method! It should:
        - If self.__root is None, raise a RuntimeError as the list is already empty
        - Create a variable which stores the root
        - Set self.__root to be equal to the root's next node
        - Return the variable created previously
        :return:
        """
        if not self.__root:
            raise RuntimeError("The linked list is empty")

        store_root = self.__root
        self.__root = self.__root.get_next()
        return store_root

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, text):
        marker = self.__root
        while marker:
            if marker.text == text:
                return marker
            marker.get_next()

        raise LookupError("Text {} is not in the list".format(text))

    def size(self):
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count
