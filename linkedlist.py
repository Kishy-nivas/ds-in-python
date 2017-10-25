# linked list implementation 

class Node(object):

	def __init__(self,value,next=None):
		
		self.value =value
		self.next=None 


class LinkedList(object):

	def __init__(self):
		
		self.head =None 
		self.tail =None 

	def add_begin (self,value ):
		
		if self.head==None:
			self.head =self.tail = Node(value )
			self.head.next =self.tail.next =None 
		else:
			self.head.next = Node(value )
			self.head = self.head.next

	def add_end(self,value ):
		
		if self.head==None:
			self.head= self.tail=Node(value )
			self.head.next=self.tail.next =None 
		else:
			dummy =Node(value)
			dummy.next = self.tail
			self.tail = dummy 


	def traverse(self):

		r= self.tail
		while r :
			print(r.value )	
			r=r.next

	
	def find (self,value):

		index =0
		r= self.tail 
		while r and r.value !=value: 
			r=r.next
			index +=1  

		if r==None:
			return 0
		else:
			return index 


	def delete(self,value):
		is_present = self.find(value )
		if is_present:
			if self.head.value ==value :           # start element 
				r= self.tail 
				while r.next!=self.head:
					r= r.next 
				self.head=r 
				del(r.next)
				self.head.next = None 

			elif self.tail.value ==value:			# end element 
				temp = self.tail 
				dummy =self.tail.next 
				self.tail = dummy
				del(temp) 

			else :
				r= self.tail  						# deleting middle elements 
				while r and r.value !=value:
					prev = r 
					r= r.next 
					curr = r 

				if r is not None:
					prev.next = curr.next 
					curr.next=None 
					del(curr)



		else:
			print ("value not found ")

if __name__ == '__main__':
	l=LinkedList() 
	l.add_begin(5)
	l.add_begin(6)
	l.add_begin(7)
	l.add_begin(8)
	l.add_end(4)
	l.traverse()
	l.delete(7) 
	l.traverse()
	l.delete(7)
