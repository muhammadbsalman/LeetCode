# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current_node = head
        
        while current_node!=None:
            current_node=current_node.next
            count+=1
        if count == 1: return None;
        to_skip = (count - n) + 1
        if to_skip ==1: 
            head = head.next
            return head
        
        count = 1
        current_node = head
        
        while current_node!=None:
            if count==to_skip-1:
                current_node.next = current_node.next.next
                break;
            current_node = current_node.next
            count+=1
            
        return head
