# TernaryHeap.py
#
# Author: Taylor Rose
#
# Generic implementation of a ternary heap. Items are arranged such 
# that eachitem in the heap is less than its children in the heap (if 
# any). Note thatbehavior with identical items is not defined.

class TernaryHeap():

	"Ternary Heap Sort Algorithm"

	

	#
	# init function.  Takes the first item to be stored in the heap.
	#

	def __init__(self, null):

		self.size = 0

		self.heap = []

		self.heapType = 0	

	#	
	# Accessor for the size of the heap
	#

	def getSize(self):

		print self.size

	#
	# Insertion Algorithm
	#

	def insert( self, item ):
	
		if( len(self.heap) == 0 ):		# if heap is empty

			# The data type of the heap. All 						# additional data will be checked 						# against this variable.

			self.heapType = type(item)

			self.heap.append(item)

			self.size = self.size + 1

			return	

		if( type(item) != self.heapType ):	# Check item's type

			print "Cannot insert item of this type into this" 				+ " heap!"

			return

		loc = self.size

		parent = ( loc - 1 ) / 3	# calculate parent node

		self.heap.append(item)		# insert item

		# algorithm inserts new item at the bottom of the heap and 		# then bubbles it up the heap until it is no longer smaller 		# than it's parent.

		while( loc != 0 and self.heap[loc] < self.heap[parent] ):
	
			self.heap[loc] = self.heap[parent]

			self.heap[parent] = item

			loc = parent
	
			parent = ( loc - 1 ) / 3

		self.size = self.size + 1

	#
	# Removal Algorithm
	#

	def remove(self):

		if( self.size <= 0 ):		# Error message if heap is
							# empty
			print "Heap is empty!"

			return

		end = self.size - 1

		output = self.heap[0]		# output of remove()

		loc = 0

		self.heap[0] = self.heap[end]

		self.heap[end] = output

		self.heap.remove( self.heap[end] )

		while( loc < ( end - 1 ) / 3 ):

			if( loc * 3 + 1 != end ):

				low = loc * 3 + 1

			else:

				break

			lowestChild = self.heap[low]

			if( lowestChild > self.heap[loc * 3 + 2] 
				and loc * 3 + 2 != end ):
			
				lowestChild = self.heap[loc * 3 + 2]

				low = loc * 3 + 2

			if( lowestChild > self.heap[loc * 3 + 3]
				and loc  * 3 + 3 != end ):

				lowestChild = self.heap[loc * 3 + 3]

				low = loc * 3 + 3

			if( lowestChild < self.heap[loc] ):

				self.heap[low] = self.heap[loc]

				self.heap[loc] = lowestChild

			loc = low
		
		self.size = self.size - 1

		return output
				

	#
	# toString
	#

	def printH(self):

	# Prints the contents of the heap not neccessarily sorted.  Items 
	# must be removed from heap in order to sort.

		for x in range(self.size):	# iterate through the heap

			print self.heap[x]