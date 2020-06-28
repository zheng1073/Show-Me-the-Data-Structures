#Problem 5: Blockchain
import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
      self.prev = None
    def calc_hash(self, data):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()
    #one of the two
    def __repr__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)
    def __str__(self):
        return ('Timestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}'.format(self.timestamp, self.data, self.previous_hash, self.hash))

class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
    def appendBlock(self, val):
        if val is None or val =="":
            return False
        if self.head is None:
            timeS = datetime.datetime.utcnow()
            self.head = Block(timeS, data, 0)
            self.tail = self.head
            return
        
        timeS = datetime.datetime.utcnow()
        self.tail.next = Block(timeS, data, self.tail.hash)
        self.tail = self.tail.next
        return
    def toList(self):
        out = []
        block = self.head
        while block:
            out.append([block])
            block = block.next
        return out

#Test
test = Blockchain()
test.appendBlock("") #False

test_2 = Blockchain()
test_2.toList() #[] <-- since blockchain is empty, it'll return an empty list

test_3 = Blockchain()
list_1 = ['abc', 'def', 'hij']
for words in list_1:
    test_3.appendBlock(words)
test_3.toList() #should return a list with all the info in it
