# Question Link: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        # initialize the sum linked list with zero (later while considering the output, we remove the head by only considering the tail)
        l_sum = ListNode(0)
        
        # store the pointer to the last node of l_sum in `temp`
        temp = l_sum
        
        # intitialize the carry
        carry = 0

        # till both l1 and l2 are not empty
        while l1 or l2:
            # addition for the current place
            curr_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            # update the sum linked list
            temp.next = ListNode(curr_sum % 10)

            # update the linked lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            temp = temp.next
            
            # update the carry
            carry = curr_sum // 10
        
        # if carry is still non-zero after traversing both lists
        if carry != 0:
            temp.next = ListNode(carry)
        
        # Return the tail of l_sum (read the initialization comments of l_sum)
        return l_sum.next