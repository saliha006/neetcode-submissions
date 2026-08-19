# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #provides starting point
        tail = dummy 

        while list1 and list2: #while neither hits none
            if list1.val < list2.val:
                tail.next = list1 #point next tail to l1's val+next
                list1 = list1.next #l1 pointer ahead for next comparison
            else:
                tail.next = list2 #point next tail to l2's val+next
                list2 = list2.next #l2 pointer ahead for next comparison

            tail = tail.next #bookmarks where next node connection needs to begin 

        tail.next = list1 if list1 else list2 #point tail's next elements to the
         #remaining elements of l1 or l2 if either is empty while other is not 

        return dummy.next #return all the elements from starting to end node



