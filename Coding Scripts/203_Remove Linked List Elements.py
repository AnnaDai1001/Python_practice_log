# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # Easier solution
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        curr = dummy_head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy_head.next

        # #   Or treat the head seperately
        # while head and head.val == val:
        #     head = head.next
        # curr = head
        # while curr:
        #     if curr.next and curr.next.val == val:
        #         curr.next = curr.next.next
        #     else:
        #         curr = curr.next
        # return head


