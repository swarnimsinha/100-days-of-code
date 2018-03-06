class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = ''
        maxVal = 0
        for key,val in enumerate(s):
            while val in ans:
                ans = ans[1:]
            ans += val
            if len(ans) > maxVal:
                maxVal = len(ans)
                print(ans)
        return maxVal