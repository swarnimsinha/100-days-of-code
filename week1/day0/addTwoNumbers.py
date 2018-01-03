# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        ans = [0]
        while True:
            try:
                l2Val = l2.val
            except:
                l2Val = 0
            try:
                l1Val = l1.val
            except:
                l1Val = 0
            try:
                l1 = l1.next
            except:
                l1 = l1
            try:
                l2 = l2.next
            except:
                l2 = l2
            tempSum = ans[-1] + l2Val + l1Val
            carry = tempSum // 10
            sumVal = tempSum % 10
            ans.pop()
            ans.append(sumVal)
            ans.append(carry)
            if l1 == l2 == None:
                if ans[-1] == 0:
                    ans.pop()
                break
        answer = ListNode(','.join([str(z) for z in ans]))
        return(answer)