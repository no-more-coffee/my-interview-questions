# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        queue = deque((), maxlen=n)
        cur = head
        while cur:
            queue.append(cur)
            cur = cur.next

        target = queue.popleft()
        target.val = target.next.val
        target.next = target.next.next
        return head
