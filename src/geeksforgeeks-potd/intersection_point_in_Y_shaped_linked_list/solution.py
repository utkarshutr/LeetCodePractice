"""
Approach:

1) We can observe that to find the first common node between both the lists,
    we can traverse both the lists at the same time & keep checking whether both nodes are equal or not.

    However, if length of both lists are different it will give us a null pointer exception as we will reach end of
        the smaller linked list before the larger one.

2) To solve this, we'll first find whether the length of these to vary in size or not.
    If yes, we'll keep moving the head pointer of the larger list to next nodes till both lists become equal in size.

3) After that, we simply keep traverse both lists simultaneously till we either find a same node
        or we reach the end of the list i.e (head1 == None or head2 == None).
"""


def get_length(head):
    l = 0
    while head is not None:
        l += 1
        head = head.next
    return l


class Solution:

    def intersetPoint(self, head1, head2):
        head1_len = get_length(head1)
        head2_len = get_length(head2)

        while head1_len != head2_len:
            if head1_len > head2_len:
                head1_len -= 1
                head1 = head1.next
            else:
                head2_len -= 1
                head2 = head2.next

        while head1 is not None:
            if head1 == head2:
                return head1.data
            head1 = head1.next
            head2 = head2.next
        return -1


class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        temp = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if __name__ == '__main__':
    input1 = ["3 1 2", "2 3 3"]  # number of nodes in each linked list
    input2 = ["3 6 9", "4 1"]  # linked list#1
    input3 = ["10", "5 6 1"]  # linked list#2
    input4 = ["15 30", "8 5 4"]  # Common linked list

    for in1, in2, in3, in4 in zip(input1, input2, input3, input4):
        x, y, z = map(int, in1.strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, in2.strip().split()))
        nodes_b = list(map(int, in3.strip().split()))
        nodes_common = list(map(int, in4.strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(node)  # add to the end of the list b, only the intersection
        ob = Solution()
        print(ob.intersetPoint(a.head, b.head))
