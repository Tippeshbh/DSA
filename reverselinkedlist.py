 class ListNode:
    def __init__(self, val = 0,next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev
    
head = ListNode(1)
head.next =ListNode(2)
head.next.next =ListNode(3)
head.next.next.next =ListNode(4)

obj = Solution()
new_head = obj.reverseList(head)

while new_head:
    print(new_head.val,end = "-->")
    new_head= new_head.next






