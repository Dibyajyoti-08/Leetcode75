# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        curr = nxt = head
        prev = None
        while nxt and nxt.next:
            prev = curr
            curr = curr.next
            nxt = nxt.next.next
        prev.next = curr.next
        return head
        

        