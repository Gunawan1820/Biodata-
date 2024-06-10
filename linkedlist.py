class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

  def delete_at_beginning(self):
    if self.head is None:
      return None
    data = self.head.data
    self.head = self.head.next
    return data

  def print_list(self):
    current = self.head
    while current:
      print(current.data, end=" ")
      current = current.next

ll = LinkedList()
ll.insert_at_beginning(3)
ll.insert_at_beginning(1)
ll.insert_at_end(5)

ll.print_list()

ll.delete_at_beginning()
ll.print_list()