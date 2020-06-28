#Problem 1 --> LRU Cache
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_Cache:

    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.hashMap = {}
    
    def push_up(self, node):
        if node.next:
            node.next.prev = node.prev
        if node.prev:
            node.prev.next = node.next
        if node is self.tail:
            self.tail = self.tail.prev
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node
    
    def get(self, key):
        if key in self.hashMap:
            #function to push node to head
            self.push_up(self.hashMap[key])
            return self.hashMap[key].value
        return -1

    def set(self, key, value):
        if key in self.hashMap:
            #function to push node to head
            self.push_up(self.hashMap[key])
            self.hashMap[key].value = value
        if self.capacity > self.size:
            if self.size == 0:
                self.head = Node(key, value)
                self.tail = Node(key, value)
                self.hashMap[key] = Node(key, value)
                self.size = 1
            else:
                self.hashMap[key] = Node(key, value)
                self.size += 1
        else:
            current_tail = self.tail.key
            if self.size == 1:
                self.head = Node(key, value)
                self.tail = Node(key, value)
                self.hashMap[key] = Node(key, value)
            else:
                self.tail = self.tail.prev
                self.tail.next = None
                self.hashMap[key] = Node(key, value)
            del self.hashMap[current_tail]
        self.push_up(self.hashMap[key])

#test 1    
our_cache = LRU_Cache(10)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)       # returns -1 because 9 is not present in the cache

#test 2    
our_cache = LRU_Cache(0)

our_cache.set(1, 1);   #cache size is not valid
our_cache.get(1)       # returns -1 

#test 3    
our_cache = LRU_Cache(-1)

our_cache.set(1, 1);   #cache size is not valid
our_cache.get(1)       # returns -1
        
