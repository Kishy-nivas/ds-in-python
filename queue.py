# queue 

class Queue(object):

	def __init__(self):
		self.content = [] 

	def enqueue (self,value):
		self.content.append(value)

	def dequeue(self):
		self.content.pop(0)

	def is_empty(self):
		return len(self.content)==0 

	def peek(self):
		if self.content:
			return self.content[0]
		else:
			return "queue is empty "

if __name__ == '__main__':
	q= Queue() 
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	q.dequeue()
	print (q.is_empty())
	print (q.peek())
	q.dequeue()
	print (q.peek()) 
	q.dequeue() 
	print(q.is_empty())
	print (q.peek())
