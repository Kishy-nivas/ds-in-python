"""
Given	a	linked	list,	swap	every	two	adjacent	nodes	and	return	its	head.
For	example,	Given	1->2->3->4,	you	should	return	the	list	as	2->1->4->3.
Your	algorithm	should	use	only	constant	space.	You	may	not	modify	the	values	in
the	list,	only	nodes	itself	can	be	changed.
"""
from linkedlist import LinkedList, Node


class LinkedList2(LinkedList):												   #inheritance 

    def swap_pairs(self, head):                                                #adding a new funtion 
        dummy = Node(0)
        dummy.next = head
        current = dummy
        while current.next and current.next.next :
        	first =current.next 
        	second = current.next.next
        	first.next = second.next 
        	second.next =first 
        	current.next = second
        	current =current.next.next 
        return dummy.next 
       




if __name__ == '__main__':
    l1 = LinkedList2()
    l1.add_end(1)
    l1.add_end(2)
    l1.add_end(3)
    l1.add_end(4)
    l1.traverse()
    print("after swapping :")
    newhead = l1.swap_pairs(l1.get_tail())
    r= newhead 
    while r:
    	print(r.value ,end="->")
    	r= r.next 
 
