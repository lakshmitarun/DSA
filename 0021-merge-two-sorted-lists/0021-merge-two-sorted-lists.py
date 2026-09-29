# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        s=[]
        while list1:
            s.append(list1.val)
            list1=list1.next
        while list2:
            s.append(list2.val)
            list2=list2.next
        s.sort()
        dummy = ListNode()
        previous = dummy
        for i in s:
            node=ListNode(i)
            previous.next=node
            previous=node
        return dummy.next 