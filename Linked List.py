# Creator: Aidan Scott
# Date: 6/10/24
# Description: This program stores and tests a linked list class

class listNode:
    def __init__(self, payload=None, next=None):
        """
        Constructor: creates an empty listNode as the default
        :param payload: Any type that is comparable
        :param next (listNode): the listNode after the current listNode
                                None if it is the last node in the list
        """
        self.__payload = payload
        self.__next = next

    def getPayload(self):
        """
        Get the value that is stored in the payload of the current node
        :return: The value stored in the payload of the current node
        """
        return self.__payload

    def setPayload(self, payload):
        """
        Sets the current payload to a new value
        :param payload: The value that the payload will be set to
        """
        self.__payload = payload

        return

    def getNext(self):
        """
        Get the value of the next value in the listNode
        :return (listNode): The next value of the listNode
        """
        return self.__next

    def setNext(self, next):
        """
        Sets the current next value of the listNode to a new listNode
        :param next: The listNode that the current next will be changed to
        """
        self.__next = next

        return

class LinkedList:
    def __init__(self):
        """
        Constructor: creates an empty list with a no head or tail and a size of zero
        """
        self.__head = None
        self.__tail = None
        self.__size = 0

        return

    def __getIthNode(self, i):
        """
        Returns the listNode at the ith position in the list where
        the first position is zero. Negative values count backwards through
        the linked list. An IndexError is raised for any value of i greater
        than the length of the list
        :param i (int): The position in the list
        :return: the listNode at the ith position
        :raises: IndexError if i >= len
        """
        # check for negative index values and for index errors
        if i < 0:
            i = self.__size + 1
        elif i >= self.__size:
            raise IndexError ("List index out of range")

        # set current equal to the list node at the head of the list
        current = self.__head
        count = 0

        # traverse the list until the end of the list is hit
        # or the listNode is found
        while current is not None and count < i:
            count += 1
            current = current.getNext()

        return current

    def insert(self, i, x):
        """
        :param i (int): Position to insert x. 0 is found before the
                        first value of the list, and 1 is found after
                        the first value and before the rest of the list.
                        If i >= len, then item is appended to list
        :param x: Any type that is comparable
        :return: None
        """
        # handle empty lists - i does not matter
        if self.isEmpty():
            self.__head = listNode(x)
            self.__tail = self.__head

        # insert listNode before the head
        elif i <= 0:
            self.__head = listNode(x, self.__head)

        # insert listNode after the tail
        elif i >= self.__size:
            self.__tail.setNext(listNode(x))
            self.__tail = self.__tail.getNext()

        # insert listNode in the middle of the list (list traversal)
        else:
            previous = self.__getIthNode(i - 1)
            previous.setNext(listNode(x, previous.getNext()))

            # check if the previous value was the tail and reassign tail value
            if self.__tail == previous:
                self.__tail = self.__tail.getNext()

        # update the size of the list
        self.__size += 1

        return

    def front(self):
        """
        Returns the value at the front of the list
        :return: The value at the front of the list or None if the list is empty
        """
        if self.isEmpty():
            value = None
        else:
            value = self.__head.getPayload()

        return value

    def back(self):
        """
        Returns the value at the back of the list
        :return: The value at the back of the list or None if the list is empty
        """
        if self.isEmpty():
            value = None
        else:
            value = self.__tail.getPayload()

        return value

    def __len__(self):
        """
        Returns the length of the linked list
        :return (int): the amount of elements in the linked list
        """
        return self.__size

    def isEmpty(self):
        """
        Checks if the list is empty and returns the associated boolean
        :return (bool): True or False indicator of an empty list
        """
        # check the value of the head for whether the list is empty or not
        if self.__head is None:
            empty = True
        else:
            empty = False

        return empty

    def __str__(self):
        """
        Returns the string representation of the linked list
        :return (str): The string representation of the linked list
        """
        # create the string and the assign the first element of the linked
        # list to current
        string = ""
        current = self.__head

        while current is not None:
            # use concatenation to add each payload of each node to the string
            string += str(current.getPayload()) + " "

            # set current to the next listNode
            current = current.getNext()

        return string

    def prepend(self, x):
        """
        Adds an item at the beginning of the linked list
        :param x: Any comparable type
        :return: None
        """
        self.insert(0, x)

        return

    def append(self, x):
        """
        Adds an item to the end of the linked list
        :param x: Any comparable type
        :return: None
        """
        self.insert(len(self) - 1, x)

        return

    def pop(self, i=None):
        """
        Remove the item at position i in the linked list. If i is left empty,
            then the last item is removed from the list. Will return None if
            the list is empty.
        :param i (int): The position of the node that is to be removed
                        where the starting position is i = 0
        :return: The value stored in the list node that was removed
        """
        # check if list is empty, if so return none
        if self.isEmpty():
            return None
        # default i value should be set to the last value if not specified
        else:
            if i is None:
                i = self.__size - 1

        # pop an item from the beginning of the list
        if i == 0:
            # store the payload
            value = self.__head.getPayload()
            # move the head of the list
            self.__head = self.__head.getNext()
            # decrement the size
            self.__size -= 1

            # make sure head matches the tail for an empty list
            if self.__head is None:
                self.__tail = None

            return value

        # pop an item from any other part of the list (needs list traversal)
        else:
            # get the previous node in the list using a list traversal
            previous = self.__getIthNode(i - 1)

            # store the payload of the node being removed
            value = previous.getNext().getPayload()

            # change the tail attribute if the tail is being deleted
            if self.__tail == previous.getNext():
                self.__tail = previous

            # make the next value of the previous node skip to
            # the node after the node you are removing
            previous.setNext(previous.getNext().getNext())

            # decrement the size
            self.__size -= 1

            return value

    def find(self, item):
        """
        Finds an element in the linked list. Returns None if item is not found.
        :param item: Any comparable type that is being searched for in the list.
        :return: The value stored in the linked list that is found.
                returns None if the item is not found
        """
        # start at the beginning of the list and loop until the value is found
        current = self.__head

        while current is not None:
            if current.getPayload() == item:
                return current.getPayload()

            # set current to the next value in the list
            current = current.getNext()

        # return None if the value was not found in the list
        return None

def main():
    """
    Tests the methods of the LinkedList and linkNode classes
    """
    myLinkedList = LinkedList()

    # test methods on an empty list
    print(f"The list is empty == {myLinkedList.isEmpty()}")
    print(f"The size of the list is {len(myLinkedList)}")
    print(myLinkedList)
    print()

    # create values of different types to be added to the list
    value1 = 1
    value2 = "two"
    value3 = [3]
    value4 = "not in list"

    # insert a value at the beginning of the list
    myLinkedList.prepend(value1)
    print(myLinkedList)

    # insert a value at the end of the list
    myLinkedList.append(value2)
    print(myLinkedList)

    # insert a value in the middle of the list
    myLinkedList.insert(1, value3)
    print(myLinkedList)

    # test methods on a populated list
    print()
    print(f"The list is empty == {myLinkedList.isEmpty()}")
    print(f"The size of the list is {len(myLinkedList)}")
    print(f"The item at the front of the list is: {myLinkedList.front()}")
    print(f"The item at the back of the list is: {myLinkedList.back()}")
    print(myLinkedList)

    # find values in the list
    result1 = myLinkedList.find(value1)
    if result1 is not None:
        print(f"{result1} found in myLinkedList")
    else:
        print("value not found in myLinkedList")

    result2 = myLinkedList.find(value2)
    if result2 is not None:
        print(f"{result2} found in myLinkedList")
    else:
        print("value not found in myLinkedList")

    result3 = myLinkedList.find(value4)
    if result3 is not None:
        print(f"{result3} found in myLinkedList")
    else:
        print("value not found in myLinkedList")

    # pop the last value from the list
    myLinkedList.pop()
    print(myLinkedList)

    # pop the second value from the list
    myLinkedList.pop(1)
    print(myLinkedList)

    # pop the first value from the list
    myLinkedList.pop(0)
    print(myLinkedList)

    # try to pop from an empty list (should return None)
    print(myLinkedList.pop())

    return

if __name__ == "__main__":
    main()
