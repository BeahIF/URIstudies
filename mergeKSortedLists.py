# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists)==0:
            return None
        while len(lists) > 1:
            mergedLists=[]
            for i in range(0, len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if( i+1) < len(lists)else None
                mergedLists.append(self.mergeList(l1,l2))
            lists = mergedLists
        return lists[0]
    
    def mergeList(self, l1,l2):
        lista = ListNode()
        linha = lista
        
        while l1 and l2:
            print("voltei")
            if l1.val < l2.val:
                linha.next = l1
                l1 = l1.next
            else:
                print("here")
                print(l2)
                linha.next = l2
                print(linha)
                l2 = l2.next
                print(l2)
            linha = linha.next
            print("linha de fora")
            print(linha)
        if l1:
            linha.next = l1
            print("estou iterando aqui")
        if l2:
            linha.next = l2
        return lista.next
            
                
        
        