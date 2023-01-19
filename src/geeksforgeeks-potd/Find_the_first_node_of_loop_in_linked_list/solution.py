# User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""


class Solution:
    # Function to find first node if the linked list has a loop.
    def findFirstNode(self, head):
        if head is None or head.next is None:
            return -1

        slow = head
        fast = head

        slow = slow.next
        fast = fast.next.next

        while fast and fast.next:
            if fast == slow:
                break

            slow = slow.next
            fast = fast.next.next

        if slow != fast:
            return -1

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow.data


# {
# Driver Code Starts
# Initial Template for Python 3

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    # connects last node to node at position pos from begining.
    def loopHere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    input1 = 5
    input2 = "1 3 2 4 5"
    input3 = 2
    for _ in range(1):
        n = input1

        LL = LinkedList()
        for i in input2.split():
            LL.insert(int(i))

        LL.loopHere(input3)

        print(Solution().findFirstNode(LL.head))
# } Driver Code Ends
