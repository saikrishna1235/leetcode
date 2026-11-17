class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        arr = []

        for i in range(len(mat)):
            count = sum(mat[i])
            arr.append((count, i))

        arr.sort()

        return [arr[i][1] for i in range(k)]