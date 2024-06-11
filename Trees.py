# Creator: Aidan Scott
# Date: 6/11/24
# Description: Implements and tests Binary Tree,
# Binary Search Tree, and AVL Tree classes

class BinaryTree:
    def __init__(self, payload=None, leftChild=None, rightChild=None):
        """
        Constructor:
        :param payload (Any Value): default None
        :param leftChild (Binary Tree): default None
        :param rightChild (Binary Tree): default None
        """
        self.__payload = payload
        self.__leftChild = leftChild
        self.__rightChild = rightChild

        return

    def getPayload(self):
        """
        Gets the value of the payload and returns it
        :return: The value of the payload
        """
        return self.__payload

    def getLeftChild(self):
        """
        Gets the left child node of the current node
        :return: the left child node
        """
        return self.__leftChild

    def getRightChild(self):
        """
        Gets the right child node of the current node
        :return: the right child node
        """
        return self.__rightChild

    def setPayload(self, other):
        """
        Sets the value of the current node's payload
        :param other (Any Value): The value that the payload is set to
        :return: None
        """
        self.__payload = other

        return

    def setLeftChild(self, other):
        """
        Sets the value of the current node's left child
        :param other (Binary Tree): The node the left child is set to
        :return: None
        """
        self.__leftChild = other

        return

    def setRightChild(self, other):
        """
        Sets the value of the current node's right child
        :param other (Binary Tree): The node the right child is set to
        :return: None
        """
        self.__rightChild = other

        return

    def preorderTraversal(self):
        """
        Processes the tree into a string using a pre-order traversal
        :return: A string representation of the tree using pre-order traversal
        """
        result = ""

        if self.isEmpty():
            return result

        else:
            # root node
            result += str(self.getPayload()) + " "

            # left side
            if self.getLeftChild() is not None:
                result += self.getLeftChild().preorderTraversal()

            # right side
            if self.getRightChild() is not None:
                result += self.getRightChild().preorderTraversal()

        return result

    def inorderTraversal(self):
        """
        Processes the tree into a string using an in-order traversal
        :return: A string representation of the tree using in-order traversal
        """
        result = ""

        if self.isEmpty():
            return result

        else:
            # left side
            if self.getLeftChild() is not None:
                result += self.getLeftChild().inorderTraversal()

            # root node
            result += str(self.getPayload()) + " "

            # right side
            if self.getRightChild() is not None:
                result += self.getRightChild().inorderTraversal()

        return result

    def postorderTraversal(self):
        """
        Processes the tree into a string using a post-order Traversal
        :return: A string representation of the tree using post-order traversal
        """
        result = ""

        if self.isEmpty():
            return result

        else:
            # left side
            if self.getLeftChild() is not None:
                result +=  self.getLeftChild().postorderTraversal()

            # right side
            if self.getRightChild() is not None:
                result += self.getRightChild().postorderTraversal()

            # root node
            result += str(self.getPayload()) + " "

        return result

    def __str__(self):
        """
        Returns the string representation of the binary tree using
            an in-order traversal
        :return (string): The string representation of the binary tree
        """
        return self.inorderTraversal()

    def isEmpty(self):
        """
        Returns True if a tree is empty, False if otherwise
        :return (bool): True if the tree is empty, False if otherwise
        """
        # self cannot be none because you cannot call methods on an
        # object that does not exist.
        return self is None or self.getPayload() is None

class BinarySearchTree(BinaryTree):
    def __init__(self, payload=None, leftChild=None, rightChild=None):
        """
        Constructor:
        :param payload (any comparable value): the contents of the root
        :param leftChild (BinarySearchTree): the right subtree
        :param rightChild (BinarySearchTree): the right subtree
        """
        BinaryTree.__init__(self, payload, leftChild, rightChild)

        # empty tree
        if self.getPayload() is None:
            self.__height = -1
        # leaf height is 0
        else:
            self.__height = 0

        return

    def getHeight(self):
        """
        Gets the height of the current node on the Binary Search Tree
        :return (int): The height of the current node
        """
        return self.__height

    def computeHeight(self):
        """
        Compute and set the height based on the height of the subtrees.
        The height is -1 for an empty tree, 0 for a leaf, or the max
        of the heights of its children plus one
        :return: None
        """
        # height of a leaf as a default value
        height = -1

        # find left side max height
        if self.getLeftChild() is not None:
            height = max(height, self.getLeftChild().getHeight())

        # find right side max height
        if self.getRightChild() is not None:
            height = max(height, self.getRightChild().getHeight())

        self.__height = height + 1

        return

    def insert(self, x):
        """
        Inserts a value into the current Binary Search Tree
        :param x (any comparable type): The value being inserted into the tree
        :return: None
        """
        if self.isEmpty():
            self.setPayload(x)
            self.computeHeight()

        # left side of tree
        elif x < self.getPayload():
            # insertion step
            if self.getLeftChild() is None:
                self.setLeftChild(BinarySearchTree(x))
                self.computeHeight()
            # recursively insert into right subtree otherwise
            else:
                self.getLeftChild().insert(x)
                self.computeHeight()

        # right side of tree
        else:
            # insertion step
            if self.getRightChild() is None:
                self.setRightChild(BinarySearchTree(x))
                self.computeHeight()
            # recursively insert into right subtree otherwise
            else:
                self.getRightChild().insert(x)
                self.computeHeight()

        return

    def find(self, x):
        """
        Finds some value in the Binary Search Tree
        :param x (any comparable type): the contents of the root
        :return: The value stored in the tree, None if not found
        """
        # return None if empty
        if self.isEmpty():
            return None

        # check if the value is found in the tree
        elif x == self.getPayload():
            return self.getPayload()

        # left side of the tree
        elif x < self.getPayload():
            if self.getLeftChild() is not None:
                return self.getLeftChild().find(x)
            else:
                return None

        # right side of the tree
        else:
            if self.getRightChild() is not None:
                return self.getRightChild().find(x)
            else:
                return None

    def minValue(self):
        """
        Returns the minimum value in the BST.
        Returns None if the tree is empty
        :return: the minimum value in the BST
        """
        if self.isEmpty():
            return None

        # recursively progress down the left side of the tree
        # until the furthest left leaf node (the min) is found
        else:
            nextValue = self.getLeftChild()
            if nextValue is None:
                return self.getPayload()
            else:
                return nextValue.minValue()

    def maxValue(self):
        """
        Returns the maximum value in the BST.
        Returns None if the tree is empty
        :return: the maximum value in the BST
        """
        # base case
        if self.isEmpty():
            return None

        # recursively progress down the right side of the tree
        # until the furthest right leaf node (the max) is found
        else:
            nextValue = self.getRightChild()
            if nextValue is None:
                return self.getPayload()
            else:
                return nextValue.maxValue()

    def inorderTraversal(self):
        """
        Processes the binary search tree into a string using an in-order traversal
        :return: A string representation of the BST using in-order traversal
        """
        result = ""

        if self.isEmpty():
            return result

        else:
            # left side
            if self.getLeftChild() is not None:
                result += self.getLeftChild().inorderTraversal()

            # root node
            result += str(self.getPayload()) + "(" + str(self.getHeight()) + ")" + " "

            # right side
            if self.getRightChild() is not None:
                result += self.getRightChild().inorderTraversal()

        return result

class AVLTree(BinarySearchTree):
    def balance(self):
        """
        Returns true if tree is unbalanced
        :return (bool): True if tree is unbalanced, False otherwise
        """
        # check the height of the left child of the tree
        if self.getLeftChild() is not None:
            lHeight = self.getLeftChild().getHeight()
        else:
            lHeight = -1

        # check the height of the right child of the tree
        if self.getRightChild() is not None:
            rHeight = self.getRightChild().getHeight()
        else:
            rHeight = -1

        return abs(lHeight - rHeight) < 2

    def insert(self, x):
        """
        Insert a value into the AVL Tree
        :param x (any comparable type): the contents of the root
        :return: the new root of the tree
        """
        # empty AVL Tree
        if self.isEmpty():
            self.setPayload(x)
            self.computeHeight()
            return self

        # left side of tree
        elif x < self.getPayload():
            # insertion step
            if self.getLeftChild() is None:
                self.setLeftChild(AVLTree(x))
                self.computeHeight()
                return self

            # recursively insert into right subtree otherwise
            else:
                self.setLeftChild(self.getLeftChild().insert(x))
                if not self.balance():
                    # Case 1:
                    if x < self.getLeftChild().getPayload():
                        return self.rotateWithLeftChild()

                    # Case 2:
                    else:
                        self.setLeftChild(self.getLeftChild().rotateWithRightChild())
                        return self.rotateWithLeftChild()

                self.computeHeight()
                return self

        # right side of tree
        else:
            # insertion step
            if self.getRightChild() is None:
                self.setRightChild(AVLTree(x))
                self.computeHeight()
                return self

            # recursively insert into right subtree otherwise
            else:
                self.setRightChild(self.getRightChild().insert(x))
                if not self.balance():
                    # Case 3:
                    if x >= self.getRightChild().getPayload():
                        return self.rotateWithRightChild()

                    # Case 4:
                    else:
                        self.setRightChild(self.getRightChild().rotateWithLeftChild())
                        return self.rotateWithRightChild()

                self.computeHeight()
                return self

    def rotateWithLeftChild(self):
        """
        Rotates the self tree with its left child
        :return: the new root of the tree
        """
        k1 = self.getLeftChild()

        # Move right child of k1 to self
        self.setLeftChild(k1.getRightChild())

        # attach self to k1
        k1.setRightChild(self)

        # recalculate heights
        self.computeHeight()
        k1.computeHeight()

        return k1

    def rotateWithRightChild(self):
        """
        Rotates the self tree with its right child
        :return: the new root of the tree
        """
        k2 = self.getRightChild()

        # Move left child of k1 to self
        self.setRightChild(k2.getLeftChild())

        # attach self to k1
        k2.setLeftChild(self)

        # recalculate heights
        self.computeHeight()
        k2.computeHeight()

        return k2

def main():
    # test the Binary Tree class
    print("Binary Tree Testing:\n")

    # create a new Binary Tree
    BT = BinaryTree()

    # test methods
    print("isEmpty() = " + str(BT.isEmpty()))
    print(BT)

    # add a value to the tree
    BT.setPayload(101)
    print("isEmpty() = " + str(BT.isEmpty()))

    # populate tree
    BT.setLeftChild(BinaryTree(50))
    BT.setRightChild(BinaryTree(250))
    BT.getLeftChild().setLeftChild(BinaryTree(42))
    BT.getLeftChild().getLeftChild().setLeftChild(BinaryTree(31))
    BT.getRightChild().setRightChild(BinaryTree(315))
    BT.getRightChild().setLeftChild(BinaryTree(200))

    # test methods again on populated tree
    print("Inorder traversal: " + BT.inorderTraversal())
    print("Preorder traversal: " + BT.preorderTraversal())
    print("Postorder traversal: " + BT.postorderTraversal())

    # test the Binary Search Tree class
    print("\nBinary Search Tree Testing:\n")

    BST = BinarySearchTree()
    print("isEmpty() = " + str(BST.isEmpty()))
    print(BST)

    # insert the first value into the tree and test empty method
    BST.insert(101)
    print("isEmpty() = " + str(BST.isEmpty()))

    # populate teh rest of the tree
    BST.insert(50)
    BST.insert(250)
    BST.insert(42)
    BST.insert(31)
    BST.insert(315)
    BST.insert(200)

    # print the tree with height values
    print(BST)
    print()

    valueList = [50, 100, 101, 200, 250, 30, 31]

    for value in valueList:
        found = BST.find(value)
        if found is not None:
            print(f"{value} was found in the BST")
        else:
            print(f"Value not found")

    print(f"\nThe minimum value in the BST is {BST.minValue()}")
    print(f"The maximum value in the BST is {BST.maxValue()}")

    # test the AVL Tree class
    print("\nAVL Tree Testing:\n")

    values = [41, 12, 2, -10, -15, 81, 89, 93, 4, 6, 20, 17, 23, 10]

    myTree = AVLTree()
    print("isEmpty() = " + str(myTree.isEmpty()))
    print(myTree)

    myTree = myTree.insert(63)
    print("isEmpty() = " + str(myTree.isEmpty()))
    print(myTree)

    for value in values:
        myTree = myTree.insert(value)
        print(myTree)

    valueList = [81, 93, 10-10, 5, 4, 17, 23]

    print()
    for el in valueList:
        found = myTree.find(el)
        if found is not None:
            print(f"{el} was found in the AVL Tree")
        else:
            print(f"Value not found")

    print()
    print(f"The minimum value in the BST is {myTree.minValue()}")
    print(f"The maximum value in the BST is {myTree.maxValue()}")

    return

if __name__ == "__main__":
    main()
