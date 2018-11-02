class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i].reverse()
            A[i] = self.inverse(A[i])
        return A
    
    def inverse(self, image):
        for i in range(len(image)):
            image[i] ^= 1
        return image