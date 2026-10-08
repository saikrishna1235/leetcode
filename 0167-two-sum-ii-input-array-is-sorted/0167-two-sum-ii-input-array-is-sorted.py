class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        first=0
        last=len(numbers)-1
        while(first<last):
            if numbers[first]+numbers[last]==target:
                return [first+1,last+1]
            if numbers[first]+numbers[last]<target:
                first+=1
            else:
                last-=1
        return [first+1,last+1]