class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here
        if not A or len(A) == 0:
            return None
        self.quickSort(A, 0, len(A)-1)
        
    def quickSort(self, A, start, end):
        if start >= end:
            return
        left = start
        right = end
        pivot = A[(start+end)//2]
        while left<=right:
            while A[left] < pivot and left <= right:
                left+=1
            while A[right] > pivot and left <= right:
                right -= 1
            if left <= right:
                A[left],A[right] = A[right], A[left]
                left+=1
                right-=1   
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
