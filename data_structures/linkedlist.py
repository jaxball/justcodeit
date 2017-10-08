""" Data Structures - Linked List """

class Node:

	def __init__(self, value):
		self.val = value
		self.prev = None
		self.next = None

	def setnext(self, nextNode):
		self.next = nextNode

	def setprev(self, prevNode):
		self.prev = prevNode

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.length = 0
		self.iterator = self.head

	def insert(self, value):
		""" By default we insert at the tail """ 
		newNode = Node(value)

		if self.head == None:
			self.head = newNode
			self.tail = newNode
			self.iterator = self.head
		else:
			self.tail.next = newNode
			newNode.prev = self.tail
			self.tail = newNode
			# newNode.prev = self.tail
		
		self.length += 1

	def remove(self, value):
		curr = self.head
		while curr != None:
			if curr.val == value:
				if curr is self.tail:
					curr.prev.next = None
					self.tail = curr.prev 
					self.length -= 1
					return True 

				# middle element, although self.tail and self.next == None are now the same thing	
				if curr.prev != None:
					curr.prev.next = curr.next
					curr.next.prev = curr.prev
					curr.next = None
					curr.prev = None
					self.length -= 1
					return True

				# curr is head
				self.head = None
				self.length -= 1
				return True

			curr = curr.next 
		return False

	def pop(self):
		if self.tail == None:
			return False
		elif self.head == self.tail:
			self.head = None
			self.tail = None
		else:
			self.tail = self.tail.prev
			self.tail.next.prev = None 	# this is unnecessary
			self.tail.next = None
		self.length -= 1
		return True

	def stepNext(self):
		if self.iterator != None:
			self.iterator = self.iterator.next
		return self.iterator

	def isEmpty(self):
		return self.head == None

	def size(self):
		return self.length

	def printlist(self):
		curr = self.head
		while curr != None:
			print curr.val, "->", 
			curr = curr.next
		print "None"

# Test Cases
ll = LinkedList()
ll.insert("hello")
ll.insert("world")
print "ll.isEmpty() [after 2 inserts] =", ll.isEmpty()
ll.insert("two")
ll.insert("more")
ll.printlist()
print "ll.size() =", ll.size() 
print "invalid remove() =", ll.remove("we")
print "ll.remove('world') =", ll.remove('world')
ll.printlist()
ll.pop()
ll.pop()
print "ll.isEmpty() =", ll.isEmpty()
ll.printlist()
ll.pop()
print "ll.size() =", ll.size()
print "ll.isEmpty() =", ll.isEmpty()

