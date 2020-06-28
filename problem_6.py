class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    list_1 = []
    list_2 = []
    node1 = llist_1.head
        while node1:
            list_1.append(node1.value)
            node1 = node1.next
    node2 = llist_2.head
        while node2:
            list_2.append(node2.value)
            node2 = node2.next
    
    union_list = []
    for value in list_1:
      if value not in union_list:
        union_list.append(value)
    for value in list_2:
      if value not in union_list:
        union_list.append(value)
        
    return sort(union_list)

def intersection(llist_1, llist_2):
    # Your Solution Here
    list_1 = []
    list_2 = []
    node1 = llist_1.head
        while node1:
            list_1.append(node1.value)
            node1 = node1.next
    node2 = llist_2.head
        while node2:
            list_2.append(node2.value)
            node2 = node2.next
            
    lst = []
    for value in list_1:
      if value in list_2:
        lst.append(value)
        
    return sort(lst)


# Test
list_1 = LinkedList()
list_2 = LinkedList()

union(list_1, list_2) #[] --> returns an empty list since both list_1 and list_2 are empty
intersection(list_1, list_2) #[] --> returns an empty list since both list_1 and list_2 are empty

rando = [1, 5, 7]
rando2 = [3, 1, 6]
for val in rando:
    list_1.append(val)
intersection(list_1, list_2) #[] --> returns an empty list since list_2 is empty so there are no intersections
    
for val in rando2:
    list_2.append(val)
union(list_1, list_2) #[1, 3, 5, 6, 7]
 
    


