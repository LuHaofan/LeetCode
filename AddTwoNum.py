class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        n1 = 0
        c = 1
        while l1 != None:
            n1 += c*l1.val
            c = c*10
            l1 = l1.next
        print(n1)    
        n2 = 0
        c = 1
        while l2 != None:
            n2 += c*l2.val
            c *= 10
            l2 = l2.next
        print(n2)
        re = str(n1+n2)
        l3 = ListNode(int(re[-1]))
        currNode = l3
        for i in range(len(re)-2, -1, -1):
            print(currNode)
            currNode.next = ListNode(int(re[i]))
            currNode = currNode.next
        return l3

sol = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
sol.addTwoNumbers(l1,l2)
