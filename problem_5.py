#Problem 5: Blockchain

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None
      self.prev = None
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        return sha.hexdigest()
    #one of the two
    def __repr__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)
    def __str__(self):
        return ('Timestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}'.format(self.timestamp, self.data, self.previous_hash, self.hash))

class BlockChain(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def appendBlock(self, val):
        if val is None or val =="":
            return
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

blockchain = BlockLinkedList()

blockchain.append(55)

print(blockchain.tail)


blockchain.append()

print(blockchain.tail)


blockchain.append(123)

print(blockchain.tail)

print(blockchain.head)
