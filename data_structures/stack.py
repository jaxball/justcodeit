""" Data Structures - Stack """

class Stack:

	def __init__(self, size=10):
		self.capacity = size
		self.data = []

	def isEmpty(self):
		return self.data == []

	def size(self):
		return len(self.data)

	def push(self, value): 
		if len(self.data) == self.capacity:
			return False
		self.data.append(value)
		return True 

	def pop(self):
		# Remove last element
		lastElem = self.data.pop()
		return lastElem  

	def peek(self): 
		return self.data[-1]

# Test cases
s = Stack()
print "s.isEmpty() =", s.isEmpty()
print "s.size() =", s.size()
# now we push two items
s.push("hello")
s.push("world")
print "s.peek() =", s.peek()
print "s.size() =", s.size()
s.pop()
print "[after 1 pop()]\ns.size() =", s.size()
