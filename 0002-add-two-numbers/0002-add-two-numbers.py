
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dumy=ListNode(0)
        current=dumy
        carry=0
        while l1 or l2 or carry:
            if l1:
                one=l1.val
            else:
                one=0
            if l2:
                two=l2.val
            else:
                two=0
            total=one+two+carry
            carry=total//10
            digits=total%10
            current.next=ListNode(digits)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return dumy.next