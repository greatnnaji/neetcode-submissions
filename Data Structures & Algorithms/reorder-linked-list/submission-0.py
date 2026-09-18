# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        # Step 1: Find the middle of the list
        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        # 'slow' is at the middle. The second half starts at slow.next
        prev = None
        current = slow.next
        slow.next = None
        
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        first_half = head
        second_half = prev
        
        while second_half:
            nxt1 = first_half.next
            nxt2 = second_half.next

            first_half.next = second_half
            second_half.next = nxt1

            first_half = nxt1
            second_half = nxt2


