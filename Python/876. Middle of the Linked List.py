# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:

        self.lis = None

        tam = 0
        aux = head
        while (aux):

            header = ListNode(aux.val)
            header.next = self.lis
            self.lis = header
            tam += 1
            aux = aux.next


        if(tam% 2):
            tam = int(tam / 2)
        else:
            tam = (int(tam / 2)) - 1

        cont = 0
        aux1 = None
        while (cont <= tam):


            header = ListNode(self.lis.val)
            header.next = aux1
            aux1 = header

            cont += 1
            self.lis = self.lis.next


        return aux1



