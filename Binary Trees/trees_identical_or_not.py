class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def check_identical(r1, r2):
	if r1 is None and r2 is None:
		return True

	if r1 is not None and r2 is not None:
		return (r1.data == r2.data and check_identical(r1.left, r2.left) and check_identical(r1.right, r2.right))

	return False

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if check_identical(root1, root2):
    print "Both trees are identical"
else:
    print "Trees are not identical"