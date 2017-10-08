""" Data Structures - Queue """

class Queue:

	def __init__(self, size=10):
		self.capacity = size
		self.data = []

	def enqueue(self, value):
		if len(self.data) == self.capacity:
			return False
		self.data.append(value)
		return True

	def dequeue(self):
		return self.data.pop(0)

	def top(self):
		return self.data[0]

	def isEmpty(self):
		return self.data == []

	def size(self):
		return len(self.data)

# Test Cases
q = Queue()
print "q.size() =", q.size()
q.enqueue("hello")
q.enqueue("world")
q.enqueue("im")
q.enqueue("a")
q.enqueue("queue")
print "q.dequeue() =", q.dequeue()
print "q.top() =", q.top()
print "q.size() =", q.size()