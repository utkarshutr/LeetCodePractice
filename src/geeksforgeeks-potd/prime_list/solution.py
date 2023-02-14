import math
from typing import Optional


class Solution:
    def primeList(self, head: Optional['Node']) -> Optional['Node']:
        temp = head
        while temp is not None:
            data = temp.data
            if data == 1:
                temp.data = 2
                continue

            test1 = test2 = data
            while not self.isPrime(test2):
                test2 += 1
            while not self.isPrime(test1):
                test1 -= 1

            if (data - test1) <= (test2 - data):
                data = test1
            else:
                data = test2
            temp.data = data
            temp = temp.next
        return head

    def isPrime(self, num):
        if num == 2:
            return True
        else:
            k = 2
            while k <= math.sqrt(num):
                if num % k == 0:
                    return False
                k += 1
            return True


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


def printList(node):
    while node != None:
        print(node.data, end=" ")
        node = node.next
    print()


def inputList(len_list, input_list):
    n = int(len_list)  # length of link list
    data = [int(i) for i in input_list.strip().split()]  # all data of linked list in a line
    head = Node(data[0])
    tail = head
    for i in range(1, n):
        tail.next = Node(data[i])
        tail = tail.next
    return head


if __name__ == "__main__":
    input1 = ["4", "3", "3"]
    input2 = ["2 8 6 9", "2 6 10", "1 15 20"]
    for in1, in2 in zip(input1, input2):
        head = inputList(in1, in2)

        obj = Solution()
        res = obj.primeList(head)

        printList(res)
