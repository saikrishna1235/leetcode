class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        first = 0
        second = 0
        result=[]
        while first <m and second <n:
            if nums1[first]<=nums2[second]:
                result.append(nums1[first])
                first+=1
            else:
                result.append(nums2[second])
                second+=1
        while first<m:
            result.append(nums1[first])
            first+=1
        while second<n:
            result.append(nums2[second])
            second+=1
        nums1[:]=result