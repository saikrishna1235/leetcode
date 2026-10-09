class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        sum=0
        result=0
        for i in range(k):
            sum+=arr[i]
        if sum/k >= threshold:
            result+=1
        for i in range(k,len(arr)):
            sum-=arr[i-k]
            sum+=arr[i]
            if sum/k>=threshold:
                result+=1
        return result