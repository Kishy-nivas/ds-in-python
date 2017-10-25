# linked list implementation 

class Node(object):
	def__init__(self,value,pointer=None)
	self.value =value 
	self.next =None 

class LinkedList(object):

	def __init__(self):
		self.head =None 
		self.tail =None 

	def add(self,value ):
		if self.head==None:
			self.head =self.tail = Node(value )
			self.head.next =self.tail.next =None 
		else:
			self.head.next = Node(value )
			self.head = self.head.next 

	def traverse(self):
		r= self.tail
		while r:
			print(r.value )	
			r=r.next 


if __name__ == '__main__':	