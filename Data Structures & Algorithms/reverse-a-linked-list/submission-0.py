# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #prev pointing at none, so none -> 0 -> 1 ...
        curr = head #curr pointing at the head so = 0

        while curr:
            next_node = curr.next #saving
            curr.next = prev #reversal
            prev = curr #moving prev to curr position
            curr = next_node #moving curr to next_node position saved earlier
        return prev #returning reversed values (as now tail = head)

        