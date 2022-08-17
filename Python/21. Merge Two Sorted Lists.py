# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2:ListNode) -> ListNode:
        header = []

        while (list1 or list2):

            if(list1):
                header.append(list1.val)
                list1 = list1.next

            if (list2):
                header.append(list2.val)
                list2 = list2.next


        if header != []:

            header.sort()
            tam = len(header) -1
            aux = ListNode(header[tam])
            tam -=1

            while(tam >= 0) :
                aux1 = ListNode(header[tam])

                aux1.next = aux
                aux = aux1
                tam -= 1

        else:
            aux = ListNode()



k = [ 2,4]
aux = ListNode(1)
for i in k:
    header = ListNode(i)
    header.next = aux
    aux = header

aux1 = ListNode(1)
k = [ 3,4]
for i in k:
    header = ListNode(i)
    header.next = aux1
    aux1 = header

test = Solution()
node = test.mergeTwoLists(aux,aux1)

while(node):
    print(node.val,end='')
    node = node.next
print("mix")