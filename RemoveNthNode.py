# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/603/
# Using two pointer


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        index = 0
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head
