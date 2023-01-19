# User function Template for python3

def swap(num1, num2):
    num1, num2 = num2, num1
    return num1, num2


class Solution:

    def carpetBox(self, A, B, C, D):
        l = max(A, B)
        w = min(A, B)
        ans = 0

        if C < D:  # C is length which should always be greater than width
            C, D = swap(C, D)

        while l > C:
            l = l // 2
            if l < w:
                l, w = swap(l, w)

            ans += 1

        while w > D:
            w = w // 2
            ans += 1

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = 1
    input1 = "131203071 738050652 84 5"
    while (T > 0):
        A, B, C, D = map(int, input1.split())

        obj = Solution()
        print(obj.carpetBox(A, B, C, D))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
