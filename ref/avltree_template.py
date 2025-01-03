#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 

	@type key: int or None
	@type value: any
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""
	def get_left(self):
		if not self.is_real_node():
			return None # Self is virtual
		return self.left # Return left child



	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""
	def get_right(self):
		if not self.is_real_node():
			return None # Self is virtual
		return self.right # Return right child


	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""
	def get_parent(self):
		return self.parent


	"""returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""
	def get_key(self):
		return self.key


	"""returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""
	def get_value(self):
		return self.value


	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""
	def get_height(self):
		return self.height


	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""
	def set_left(self, node):
		self.left = node


	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""
	def set_right(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""
	def set_parent(self, node):
		self.parent = node


	"""sets key

	@type key: int or None
	@param key: key
	"""
	def set_key(self, key):
		self.key = key

	"""sets value

	@type value: any
	@param value: data
	"""
	def set_value(self, value):
		self.value = value


	"""sets the height of the node

	@type h: int
	@param h: the height
	"""
	def set_height(self, h):
		self.height = h


	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		if self.key == None:
			return False
		return True


	"""returns a node's balance factor

	@rtype: int
	@returns: difference between left and right sub-tree heights
	"""
	def get_balance_factor(self):
		return self.left.height - self.right.height
	
	"""returns whether a node is a right child of its parent

	@rtype: bool
	@returns: False if node is root or left child, otherwise True
	"""
	def is_right_child(self):
		if self.parent == None:
			return False # In case of root
		if self.parent.right == self:
			return True # Self is a right child
		return False # Self is a left child
	
	"""returns calculated height of a node 

	@rtype: int
	@returns: 1 + maximal height of sub-trees
	"""
	def calculate_height(self):
		return 1 + max(self.right.height, self.left.height)
	
	"""replace pointers of two nodes (swap between nodes) 

	@rtype: None
	@returns: None
	"""
	def replace(self, other):
		self_height = self.get_height()
		self.set_height(other.get_height())
		other.set_height(self_height)
		other.set_parent(self.parent)
		other.set_right(self.right)
		other.set_left(self.left)
		self.right.set_parent(other)
		self.left.set_parent(other)
		if self.is_right_child():
			self.parent.set_right(other)
		else:
			if self.parent != None:
				self.parent.set_left(other)

	def display(self):
		lines, *_ = self._display_aux()
		for line in lines:
			print(line)

	def _display_aux(self):
		"""Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
		if self.right is None and self.left is None:
			line = '%s' % self.key
			width = len(line)
			height = 1
			middle = width // 2
			return [line], width, height, middle

		# Only left child.
		if self.right is None:
			lines, n, p, x = self.left._display_aux()
			s = '%s' % self.key
			u = len(s)
			first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
			second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
			shifted_lines = [line + u * ' ' for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

		# Only right child.
		if self.left is None:
			lines, n, p, x = self.right._display_aux()
			s = '%s' % self.key
			u = len(s)
			first_line = s + x * '_' + (n - x) * ' '
			second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
			shifted_lines = [u * ' ' + line for line in lines]
			return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

		# Two children.
		left, n, p, x = self.left._display_aux()
		right, m, q, y = self.right._display_aux()
		s = '%s' % self.key
		u = len(s)
		first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
		second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
		if p < q:
			left += [n * ' '] * (q - p)
		elif q < p:
			right += [m * ' '] * (p - q)
		zipped_lines = zip(left, right)
		lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
		return lines, n + m + u, max(p, q) + 2, n + u // 2


"""
A class implementing the ADT Dictionary, using an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.tree_size = 0



	"""searches for a AVLNode in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: the AVLNode corresponding to key or None if key is not found.
	"""
	def search(self, key):
		if key == None:
			return None
		
		node = self.root # Start search in root
		while node.is_real_node():
			if node.get_key() == key:
				return node # Key was found

			if node.get_key() < key:
				# Key is greater than current key - search in right sub-tree
				node = node.get_right()
			else:
				# Key is less than current key - search in left sub-tree
				node = node.get_left()

		return None # Key was not found


	"""inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, key, val):
		# Initialize rebalancing operations counter at 0
		rebalance_counter = 0
	
		# Create new node using key and val
		node_to_insert = AVLNode(key,val)
		# Set its left and right child pointers to virtual nodes
		node_to_insert.set_left(AVLNode(None,None))
		node_to_insert.set_right(AVLNode(None,None))
		node_to_insert.get_right().set_parent(node_to_insert)
		node_to_insert.get_left().set_parent(node_to_insert)

		# Insert node as usual (like in BST)
		self.bst_insert(node_to_insert)

		# Tree contains only inserted node, so no rebalancing needed
		if not self.get_root().get_right().is_real_node() and not self.get_root().get_left().is_real_node():
			return rebalance_counter

		# Let y be the inserted node's parent
		y = node_to_insert.get_parent()

		return self.rebalance(1, y)
	

	"""regular Insertion from dictionary (like in BST, without rotations)

	@type node: AVLNode
	@param a: Node to insert to tree
	"""
	def bst_insert(self, node):
		curr_node = self.root # Start from root
		curr_parent = None

		# Tree is empty
		if curr_node == None:
			self.root = node

		# Tree is not empty
		else:
			# While loop until a leaf is reached
			while curr_node.is_real_node():
				curr_parent = curr_node

				if node.key < curr_node.get_key():
					# Node is less than current key, go to left sub-tree
					curr_node = curr_node.get_left()
				else:
					# Node is greater than current key, go to right sub-tree
					curr_node = curr_node.get_right()
						
			if node.key < curr_parent.get_key():
				# Node is less than leaf's key, make it the leaf's left child
				curr_parent.set_left(node)
			else:
				# Node is greater than leaf's key, make it the leaf's right child
				curr_parent.set_right(node)

			# Set node's parent as its real parent
			node.set_parent(curr_parent)

		# Set node's height at 0
		node.set_height(0)

		# Add 1 to tree's size
		self.change_size(1)

	"""performs right rotation in order to fix balance factor after insertions and deletions
	   Updates pointers and heights 

	@type a: AVLNode
	@param a: "criminal" bf node
	@type b: AVLNode
	@param b: "criminal" bf node's child for rotation
	@rtype: None
	@returns: None
	"""
	def right_rotation(self, a, b):
		a_is_right = a.is_right_child() # True if a is a right child, else False

		# Set a's left child pointer to b's right child
		a.set_left(b.get_right())

		# Set a's left child's parent pointer to a
		a.get_left().set_parent(a)

		# Set b's right child pointer to a
		b.set_right(a)

		# Set b's parent pointer to a's parent
		b.set_parent(a.get_parent())

		if a_is_right:
			b.get_parent().set_right(b) # Set b's parent right child pointer to b
		else:
			if a == self.root:
				self.root = b
			else:
				b.get_parent().set_left(b) # Set b's parent left child pointer to b
		
		# Set a's parent pointer to b
		a.set_parent(b)

		# Update a and b's heights, in case they changed
		a.set_height(a.calculate_height())
		b.set_height(b.calculate_height())

	"""performs left rotation in order to fix balance factor after insertions and deletions
	   Updates pointers and heights 

	@type a: AVLNode
	@param a: "Criminal" bf node
	@type b: AVLNode
	@param b: "Criminal" bf node's child for rotation
	@rtype: None
	@returns: None
	"""
	def left_rotation(self, a, b):
		a_is_right=a.is_right_child() # True if a is a right child, else False

		# Set a's right child pointer to b's left child
		a.set_right(b.get_left())

		# Set a's right child's parent pointer to a
		a.get_right().set_parent(a)

		# Set b's left child pointer to a
		b.set_left(a)

		# Set b's parent pointer to a's parent
		b.set_parent(a.get_parent())
		
		if a_is_right:
			b.get_parent().set_right(b) # Set b's parent's right child pointer to b
		else:
			if a == self.root:
				self.root = b
			else:
				b.get_parent().set_left(b) # Set b's parent's left child pointer to b
		
		# Set a's parent pointer to b
		a.set_parent(b)

		# Update a and b's heights, in case they changed
		a.set_height(a.calculate_height())
		b.set_height(b.calculate_height())

	"""rebalances tree

	@type case_num: int
	@param case_num: 1 - if case is insert, 2 - if case is deletion, 3 - if case is join
	@type y: AVLNode
	@param y: parent of node that was inserted/deleted/joined
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def rebalance(self, case_num, y):
		# Initialize rebalancing operations counter at 0
		rebalance_counter = 0

		# While loop until rebalancing is certainly not needed
		while y != None:
			# Save y's parent (in case more than one rebalancing is needed)
			grandpa = y.get_parent()

			# Get balance factor and new height (may have remained the same)
			curr_bf = y.get_balance_factor()
			new_height = y.calculate_height()

			# Current balance factor is OK -> check if height has changed
			if curr_bf < 2 and curr_bf > -2:
				# Height hasn't changed -> return counter
				if new_height == y.get_height():
					return rebalance_counter

				# Height has changed -> update height a rebalance counter and return to loop with y's father
				y.set_height(new_height)
				rebalance_counter += 1
				y = grandpa

			# Current balance factor is not OK -> perform rotations
			else:
				# Current balance factor is -2 -> check right child
				if curr_bf == -2:
					right = y.get_right()
					right_bf = right.get_balance_factor()

					# Right child's balance factor is -1 (or 0 if delete or join) -> perform LEFT rotation
					if right_bf == -1 or (right_bf == 0 and (case_num == 2 or case_num == 3)):
						self.left_rotation(y, right)
						rebalance_counter += 1 # Increase rebalance counter by 1

					# Right child's balance factor is 1 -> perform RIGHT then LEFT rotations
					else:
						self.right_rotation(right, right.get_left())
						self.left_rotation(y, y.get_right())
						rebalance_counter += 2 # Increase rebalance counter by 2

				# Current balance factor is 2 -> check left child
				else:
					left = y.get_left()
					left_bf = left.get_balance_factor()

					# Left child's balance factor is 1 (or 0 if delete) -> perform RIGHT rotation
					if left_bf == 1 or (left_bf == 0 and case_num == 2):
						self.right_rotation(y, left)
						rebalance_counter += 1 # Increase rebalance counter by 1
					
					# Left child's balance factor is -1 -> perform LEFT then RIGHT rotations
					else:
						self.left_rotation(left, left.get_right())
						self.right_rotation(y, y.get_left())
						rebalance_counter += 2 # Increase rebalance counter by 2
				
				# Go back to loop with y's father if y is not root
				y = grandpa

				if case_num == 1:
					return rebalance_counter

		return rebalance_counter
	
	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		# Initialize rebalancing operations counter at 0
		rebalance_counter = 0

		# Save parent of physically deleted node, for rebalancing
		y = node.get_parent()
		suc = self.successor(node)

		# In case deleted node is the root
		if y == None and suc != None:
			y = suc.get_parent()

		# In case the successor is the node's right child
		if suc == node.get_right():
			y = suc

		# Regular deletion of node from Self (like in BST)
		self.bst_delete(node)

		# Perform rebalance with option 2 - deletion
		return self.rebalance(2, y)

	"""regular deletion from dictionary (like in BST, without rotations)

	@type node: AVLNode
	@param a: Node to delete from tree
	"""
	def bst_delete(self, node):
		right_child = node.get_right() # Node's right child
		left_child = node.get_left() # Node's left child

		has_right_child = right_child.is_real_node() # True if node has a right child
		has_left_child = left_child.is_real_node() # True if node has a left child

		parent = node.get_parent() # Node's parent

		# Case 1: Node is a leaf
		if not has_left_child and not has_right_child:
			# If node is the root and the only node in tree
			if parent == None:
				self.root = None
			# If node is a right child
			elif node.is_right_child():
				# Set parent's right child pointer to virtual node
				parent.set_right(AVLNode(None, None)) 
			else:
				# Set parent's left child pointer to virtual node
				parent.set_left(AVLNode(None, None)) 
		
		# Case 2: Node has two children
		elif has_right_child and has_left_child:
			# Find node successor
			suc = self.successor(node)
			# Remove successor from tree
			if suc.is_right_child():
				suc.get_parent().set_right(suc.get_right())
			else:
				suc.get_parent().set_left(suc.get_right())
			suc.get_right().set_parent(suc.get_parent())
			# Replace node with its successor
			node.replace(suc)
			# If node was root, set tree root as its successor
			if self.root == node:
				self.root = suc

		# Case 3 (and last): Node has one child
		else:
			if has_right_child:
				child = right_child # Child is a right child
			else:
				child = left_child # Child is a left child
			
			# If node is root
			if parent == None:
				self.root = child
			# If node is a right child
			elif node.is_right_child():
				# Set parent's right child pointer to node's child
				parent.set_right(child)
			else:
				# Set parent's left child pointer to node's child
				parent.set_left(child)
			
			# Set child's parent pointer to real parent
			child.set_parent(parent)
		
		# Subtract 1 from tree's size
		self.change_size(-1)

		

	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		lst = []
		self.avl_to_array_rec(self.root, lst)
		return lst
	
	"""recursive function that appends (key, value) touple in-order 

	@rtype: None
	@returns: None
	"""
	def avl_to_array_rec(self, node, lst):
		if not node.is_real_node():
			return
		right = node.get_right()
		left = node.get_left()
		self.avl_to_array_rec(left, lst)
		lst.append((node.get_key(), node.get_value()))
		self.avl_to_array_rec(right, lst)

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.tree_size
	
	"""splits the dictionary at the i'th index

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		# Initialize RIGHT and LEFT trees with roots being the children of x
		right = AVLTree()
		if node.get_right().is_real_node():
			right.root = node.get_right()
		left = AVLTree()
		if node.get_left().is_real_node():
			left.root = node.get_left()

		# Set y as x's parent
		y = node.get_parent()

		# Climb up the tree until the tree root is reached
		while y != None:
			grandpa = y.get_parent()
			
			# Create a temp tree
			new_t = AVLTree()
			
			if y.get_key() < node.get_key():
				if y.get_left().is_real_node():
				# Set temp tree as the sub-tree of y's left child
					new_t.root = y.get_left()
					new_t.root.set_parent(None)
				# Join temp tree with LEFT tree and y
				new_t.join_node(left, y)
				left = new_t
			else:
				if y.get_right().is_real_node():
				# Set temp tree as the sub-tree of y's left child
					new_t.root = y.get_right()
					new_t.root.set_parent(None)

				# Join temp tree with RIGHT TREE and y
				right.join_node(new_t, y)
				node = y
			y = grandpa

		return [left, right]


	
	"""joins self with key and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree2
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def join(self, tree2, key, val):
		x = AVLNode(key, val) # Create key node

		return self.join_node(tree2, x)


	"""joins self with node and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type node: AVLNode 
	@param node: The node that is to be joined
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""	
	def join_node(self, tree2, node):
		small_root = self.get_root() # Root whose key < x.key
		big_root = tree2.get_root() # Root whose key > x.key

		if small_root == None and big_root == None:
			self.insert(node.get_key(), node.get_value())
			return 1
		elif small_root == None:
			tree2.insert(node.get_key(), node.get_value())
			self.root = tree2.get_root()
			return 1 + self.get_root().get_height()
		elif big_root == None:
			self.insert(node.get_key(), node.get_value())
			return 1 + self.get_root().get_height()

		h1 = small_root.get_height() # Height of tree with smaller keys
		h2 = big_root.get_height() # Height of tree with bigger keys

		# Check which tree is higher
		# Set short height and tall tree values
		# If height are the same - just join with x as the root
		if h1 == h2:
			node.set_right(big_root)
			node.set_left(small_root)
			big_root.set_parent(node)
			small_root.set_parent(node)

			# Set self as the joined tree
			self.root = node
			self.root.set_height(self.root.calculate_height())
			# Update tree size
			self.change_size(1 + tree2.size())
			return 1 + abs(h1 - h2)
		
		# Self is higher
		elif h1 > h2:
			tall_tree = self
			short_tree = tree2
			is_short_left = False # Short tree's keys are bigger than tall tree's keys

		# Tree2 is heigher
		else:
			tall_tree = tree2
			short_tree = self
			is_short_left = True # Tall tree's keys are bigger than short tree's keys

		curr = tall_tree.get_root()
		short_height = short_tree.get_root().get_height()

		# Let b be the node in tall tree that is the first one to have a height <= short height
		# Loop to find b
		while curr.get_height() > short_height:
			# If shorter tree contains smaller keys - go left
			if is_short_left:
				curr = curr.get_left()
			# If shorter tree contains bigger keys - go right
			else:
				curr = curr.get_right()
		
		b = curr
		# Let c be b's parent
		c = b.get_parent()

		short_tree_root = short_tree.get_root()
		node.set_parent(c)

		# Arranage pointers according to the side of the short tree
		if is_short_left:
			c.set_left(node)
			node.set_right(b)
			node.set_left(short_tree_root)
		else:
			c.set_right(node)
			node.set_left(b)
			node.set_right(short_tree_root)
		
		b.set_parent(node)
		short_tree_root.set_parent(node)

		# Set Self as the joined tree
		self.root = tall_tree.get_root()
		self.root.set_height(self.root.calculate_height())
		self.change_size(1 + tree2.size())
		
		# Rebalance tree
		self.rebalance(3, node)

		return 1 + abs(h1 - h2)


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root

	"""gets node's successor in dictionary 

	@type node: AVLNode
	@param a: Node to find successor to
	@rtype: AVLNode or None
	@returns: Successor of input node, or None if input node is the maximum key in the dictionary
	"""
	def successor(self, node):
		curr = node

		# If node has right child, go right to find successor
		if curr.get_right().is_real_node():
			curr = curr.get_right()
			# Find minimum at right side to find successor
			while curr.get_left().is_real_node():
				curr = curr.get_left()
			return curr
		
		# Node does not have right child
		parent = curr.get_parent()
		# Go up until the node is not the right child
		while parent != None and parent.is_real_node() and curr == parent.right:
			curr = parent
			parent = curr.get_parent()
		
		# Anyway, return parent. If node has the maximum key, None will be returned
		return parent
	
	"""changes the size of the tree by delta

	@type delta: int
	@param delta: delta size to change size by
	"""
	def change_size(self, delta):
		self.tree_size += delta