""" Data Structures - Binary Search Tree """

class Node:

	def __init__(self, value):
		self.val = value
		self.left = None
		self.right = None

class BST:

	def __init__(self):
		self.root = None
		self.size = 0

	def insert(self, value):
		
		if self.root == None:
			self.root = Node(value)
		else: 
			self.insertAt(self.root, value)
		return self

	def insertAt(self, curr, value): 

		if value <= curr.val:
			if curr.left:
				self.insertAt(curr.left, value)
			else: 
				curr.left = Node(value)
		elif value > curr.val:
			if curr.right: 
				self.insertAt(curr.right, value)
			else:
				# we want to add as child of current node
				curr.right = Node(value)

	def delete(self, value):
		# TODO: find node corresponding to value first
		# then delete and fix BST tree 
		toDelete = self.find(value)
		if toDelete == None:
			return

		pred = self.predecessor(value) 
		if toDelete.left == None and toDelete.right == None:
			# pred = self.predecessor(value) 
			if pred.left.val == value: 
				pred.left = None
			elif pred.right.val == value:
				pred.right = None
			else:
				# this is unexpected error case (DEBUG=unhandled)
		elif toDelete.left and toDelete.right:
			if pred.left.val == value: 
				# toDelete has left subtree
			elif pred.right.val == value:
				# toDelete has right subtree
		elif toDelete.left.val or toDelete.right:
			if pred.left.val == value: 
				pred.left = toDelete.left if toDelete.left else toDelete.right
			elif pred.right.val == value:
				pred.right = toDelete.left if toDelete.left else toDelete.right

		"""
		If we remove the node referenced by our
		local root variable, how do we change the
		left or right field of its parent (if this node
		does not have a pointer back to the
		parent)?

		Solution: Return a reference to the replacement
		reference (or null) as the result and let the
		previous invocation store the result in its local
		root node (which is the parent of the root node
		we want to remove). 
		"""
			

				

	def find(self, value):
		return self.findAt(self.root, value)

	def findAt(self, curr, value):
		if curr == None:
			return curr

		if value == curr.val:
			return curr
		elif value < curr.val:
			return self.findAt(curr.left, value)
		else:
			return self.findAt(curr.right, value)

	def minimum(self):
		if self.root == None: 
			return False

		curr = self.root
		# minVal = curr.val

		while curr.left != None:
			# minVal = min(minVal. curr.val)
			curr = curr.left

		return curr.val

	def maximum(self):
		if self.root == None:
			return False
		
		curr = self.root
		while curr.right != None:
			curr = curr.right
		return curr.val

	def getPredecessor(self, value):
		pass 

	def getSuccessor(self, value):
		pass 

	def getParent(self, currnode):
		pass

	def length(self):
		return self.size

	def printTree(self, rootNode):
		if rootNode != None:
			print "[", rootNode.val, # ", ",
			if rootNode.left:
				print "\nleft: ",
				# print "left: ",		# alternative
			self.printTree(rootNode.left)
			if rootNode.right:
				print "\n\t right: ",
				# print ", right: ",	# alternative printing
			self.printTree(rootNode.right)
			print "]", 
		else: 
			return
			# print "]",

# Test Cases
b = BST()
# b.insert(5).insert(10).insert(2).insert(6).insert(1).insert(12)
b.insert(5).insert(8).insert(10).insert(6).insert(12).insert(7)
b.printTree(b.root)

print 
print "largest elem =", b.maximum()
print "smallest elem =", b.minimum()
print "find(10) =", b.find(10)
print "find(19) =", b.find(19)
