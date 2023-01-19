'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
import math


class Solution:
    def __init__(self):
        self.max_gcd_root = 0
        self.max_gcd = 0

    def solve(self, root):
        if root is None:
            return -1

        if root.left is not None and root.right is not None:
            gcd = math.gcd(root.left.data, root.right.data)
            if gcd > self.max_gcd:
                self.max_gcd_root = root.data
                self.max_gcd = gcd
            elif gcd == self.max_gcd:
                self.max_gcd_root = max(self.max_gcd_root, root.data)

        self.solve(root.left)
        self.solve(root.right)

    def maxGCD(self, root):
        self.solve(root)
        return self.max_gcd_root


# {
# Driver Code Starts
from collections import deque


# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if (len(s) == 0 or s[0] == "N"):
        return None

    # Creating list of strings from input 
    # string after spliting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size = size + 1

    # Starting from the second element
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currNode = q[0]
        q.popleft()
        size = size - 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if (currVal != "N"):
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.left)
            size = size + 1
        # For the right child
        i = i + 1
        if (i >= len(ip)):
            break
        currVal = ip[i]

        # If the right child is not null
        if (currVal != "N"):
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.append(currNode.right)
            size = size + 1
        i = i + 1
    return root


if __name__ == "__main__":
    t = 1
    input1 = "5 49 N 5 N 21 49 1 4 5 10"
    for _ in range(0, t):
        s = input1
        root = buildTree(s)
        ob = Solution()
        print(ob.maxGCD(root))
