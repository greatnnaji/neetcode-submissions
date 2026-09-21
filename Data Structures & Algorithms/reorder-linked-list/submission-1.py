# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first middle of list
        slow = head
        fast = head

        while fast and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        # slow is at mid point of loop
        

        # re-wire pointers
        prev = None
        # 2 -> 4 -> 6 -> None and 10 -> 8 -> None 
        # As opposed to if prev = slow:
        # 2 -> 4 -> 6 -> None and 10 -> 8 -> 6 -> None
        # 6 is duplicated which breaks when merging
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # adjust list in place
        head1 = head
        head2 = prev # head of reversed list

        while head2:
            nx1 = head1.next
            nx2 = head2.next

            head1.next = head2
            head2.next = nx1

            head1 = nx1
            head2 = nx2

        # Every independent list must have a distinct -> None
        
        



