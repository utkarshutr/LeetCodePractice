# User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

'''


class Solution():
    # An utility function to merge two sorted linked lists
    def merge(self, l1, l2):
        # if the first linked list is empty then return the second list
        if(l1 == None):
            return l2

        # if the second linked list is empty then return the first list
        if(l2 == None):
            return l1

        # compare the data members of the two linked lists
        # and put the larger one in the result
        result = None

        if (l1.data <= l2.data):
            result = l1
            result.bottom = self.merge(l1.bottom,l2)
        else:
            result = l2
            result.bottom = self.merge(l1,l2.bottom)

        result.next = None
        return result

    def flatten(self, root):

        # Base Case
        if(root == None or root.next == None):
            return root
        # recur for the list on the right

        root.next = self.flatten(root.next)

        # now merge
        root = self.merge(root, root.next)

        # return the root

        return root


# Your code here


# {
# Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while (node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    input_val1 = 1
    input_val2 = 16
    input_val3 = "20 1 20 14 10 13 20 6 13 15 14 13 11 3 20 14"
    input_val4 = "265 769 365 160 793 54 79 267 934 454 747 967 14 665 516 613 298 96 694 638 838 295 753 985 733 956 171 900 424 197 763 933 645 754 545 696 644 480 382 201 644 159 615 114 189 903 398 589 681 717 129 709 740 119 120 347 942 294 518 370 436 60 108 561 661 555 887 522 968 894 79 115 716 968 403 415 617 73 196 530 341 240 929 111 961 903 759 234 608 867 350 290 720 782 468 395 249 294 459 831 340 368 162 913 292 551 986 682 655 904 920 793 95 668 595 449 544 913 693 656 387 502 652 148 848 544 597 477 807 605 674 146 194 597 283 177 722 35 542 885 342 796 427 839 229 983 280 976 110 234 887 849 715 748 797 954 120 872 308 712 448 787 431 752 393 90 400 561 894 691 283 28 557 734 954 810 935 350 38 485 867 238 852 968 286 407 977 673 834 438 325 720 434 559 459 163 304 542 318 363 783 409 720 861 318 516 270"

    # t=int(input())
    t = int(input_val1)
    while (t > 0):
        head = None
        # N=int(input())
        N = int(input_val2)
        arr = []

        # arr=[int(x) for x in input().strip().split()]
        arr = [int(x) for x in input_val3.strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        # listo=[int(x) for x in input().strip().split()]
        listo = [int(x) for x in input_val4.strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag is 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 is 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        obj = Solution()
        root = obj.flatten(head)
        printList(root)

        t -= 1

# } Driver Code Ends
