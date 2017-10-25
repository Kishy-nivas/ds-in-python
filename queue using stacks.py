class Queue(object):

	def __init__(self ):
		self.in_array =[]
		self.out_array =[] 

	def enqueue(self,value ):
		self.in_array.append(value )

	def transfer(self):
		while self.in_array:
			self.out_array.append(self.in_array.pop())

	def dequeue(self):
		if self.out_array:
			self.out_array.pop()   
		else:
			self.transfer() 						#reverse the in array elements to the out array 
			self.out_array.pop()

	def peek(self):
		if self.out_array:
			return self.out_array[-1]					
		else:
			if self.in_array:
				return self.in_array[0] 


if __name__ == '__main__':
	q = Queue() 
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.dequeue() 
	print(q.peek())
	q.dequeue() 
	print(q.peek())



