# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        header = []
        while (head):
            header.append(head.val)
            head = head.next

        return header == header[::-1]