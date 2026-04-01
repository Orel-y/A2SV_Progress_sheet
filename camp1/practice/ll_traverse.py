class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
head = a

def print_ll(head):
	while head != None:
		print(head.value)
		head = head.next

def insert_at_beg(head, value):
	new_node = Node(value)
	if not head:
		return new_node
	
	new_node.next = head
	head = new_node
	return head

def insert_at_idx(head, value, idx):
	new_node = Node(value)
	ptr = head
	if not head:
		return new_node
	
	while ptr.value != idx:
		ptr = ptr.next
	
	new_node.next = ptr
	ptr = new_node
	return head	

head = insert_at_beg(head, 4)
head = insert_at_beg(head, 5)
head = insert_at_idx(head, 6, 3)
print_ll(head)
	
