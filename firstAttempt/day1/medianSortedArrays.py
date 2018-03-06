class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newlist = nums1 + nums2
        newlist = sorted(newlist)
        lengthVal = len(newlist)
        if lengthVal%2 == 1:
            return newlist[((lengthVal + 1) / 2) - 1]
        else:
            a = newlist[((lengthVal) / 2) - 1]
            b = newlist[((lengthVal) / 2)]
            return ((a + b)/2.0)