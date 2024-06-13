# Creator: Aidan Scott
# Date: 6/11/24
# Description: Implements and tests a hash table class

from Linked_List import LinkedList
import random
class HashTableChaining:
    def __init__(self, size=101):
        """
        Constructor:
        :param size (int): The size of the table. Should be a prime number,
        default is 101.
        """
        self.__buckets = []
        for i in range(size):
            self.__buckets.append(LinkedList())

        return

    def __hash(self, value):
        """
        Hash function
        :param value (any comparable value):
        :return (int): The bucket number for the value
        """
        return value % len(self.__buckets)

    def insert(self, value):
        """
        Inserts a value into the hash table
        :param value (int):
        :return: None
        """
        bucketNum = self.__hash(value)
        self.__buckets[bucketNum].append(value)

        return

    def find(self, value):
        """
        Finds a value in the hash table.
        Returns None if value is not in the hash table
        :param value (int): The value being searched for
        :return: The value in the table, returns None if not found
        """
        bucketNum = self.__hash(value)
        result = self.__buckets[bucketNum].find(value)

        return result

    def __str__(self):
        """
        Generates a string representation of the hash table
        :return (string): A string representation of the hash table
        """
        result = ""
        for i in range(len(self.__buckets)):
            # print out each bucket on separate lines
            result += "bucket" + str[i] + ": " + str(len(self.__buckets[i])) + ": "
            result += str(self.__buckets[i]) + "\n"

        return result

class HashTableProbing:
    def __init__(self, size=101):
        """
        Constructor:
        :param size (int): The size of the table. Should be a prime number,
        default is 101.
        """
        self.__buckets = [None] * size
        self.__skip = 1

        return

    def __hash(self, value):
        """
        Hash function
        :param value (any comparable value):
        :return (int): The bucket number for the value
        """
        return value % len(self.__buckets)

    def __rehash(self, bucketNum):
        """
        Rehash function
        :param bucketNum (int): The last bucket number attempted
        :return: The next bucket number to try
        """
        return (bucketNum + self.__skip) % len(self.__buckets)

    def insert(self, value):
        """
        Inserts a value into the hash table
        :param value (int):
        :return: None
        """
        # hash the value for the bucket number
        bucketNum = self.__hash(value)

        # keep original bucket number to keep track of when to stop searching
        originalBucketNum = bucketNum

        # initial rehash
        if self.__buckets is not None:
            bucketNum = self.__rehash(bucketNum)

        # loop rehashes until an empty bucket is found
        # or the original bucket is found
        while self.__buckets[bucketNum] is not None and bucketNum != originalBucketNum:
            bucketNum = self.__rehash(bucketNum)

        # insert value if bucket is empty, otherwise raise exception
        if self.__buckets[bucketNum] is None:
            self.__buckets[bucketNum] = value
        else:
            raise Exception("Table Full")

        return

    def find(self, value):
        """
        Finds a value in the hash table.
        Returns None if value is not in the hash table
        :param value (int): The value being searched for
        :return: The value in the table, returns None if not found
        """
        # hash the value for the bucket number
        bucketNum = self.__hash(value)

        # keep original bucket number to keep track of when to stop searching
        originalBucketNum = bucketNum

        # initial rehash
        if self.__buckets is not None and self.__buckets[bucketNum] == value:
            return self.__buckets[bucketNum]
        else:
            bucketNum = self.__rehash(bucketNum)

        # loop rehashes until an empty bucket is found
        # or the original bucket is found
        while self.__buckets[bucketNum] is not None and \
                self.__buckets[bucketNum] != value and \
                bucketNum != originalBucketNum:
            bucketNum = self.__rehash(bucketNum)

        # insert value if bucket is empty, otherwise raise exception
        if self.__buckets[bucketNum] is not None and self.__buckets[bucketNum] == value:
            return self.__buckets[bucketNum]
        else:
            return None

    def __str__(self):
        """
        Generates a string representation of the hash table
        :return (string): A string representation of the hash table
        """
        result = ""
        for i in range(len(self.__buckets)):
            # print each bucket on a separate line
            result += "bucket" + str[i] + ": " + str(self.__buckets[i]) + "\n"

        return result

def main():
    """
    Main function tests the hash table classes with random values
    """
    # create a list of random values
    values = []
    for i in range(20):
        values.append(random.randint(0, 100))

    # print the list of values
    print(values)

    # create two hash tables, one using chaining and one using probing
    myChainingHashTable = HashTableChaining()
    myProbingHashTable = HashTableProbing()

    # insert the values into both tables
    for value in values:
        myChainingHashTable.insert(value)
        myProbingHashTable.insert(value)

    # create a list of values to lookup
    # should likely return value not found on the last three values
    # appended values are out of range of the randint
    values.append(1001)
    values.append(-1001)
    values.append(5000)

    # lookup each value in the chaining hash table
    for i in values:
        result = myChainingHashTable.find(i)
        if result is not None:
            print(f"{result} found in chaining hash table")
        else:
            print("Value not found")

    for k in values:
        result = myProbingHashTable.find(k)
        if result is not None:
            print(f"{result} found in probing hash table")
        else:
            print("Value not found")

    return

if __name__ == "__main__":
    main()