class Solution:
    def reverseKGroup(self, head, k):
        cur = head
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next

        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverseKGroup(curr, k)
        return prev
