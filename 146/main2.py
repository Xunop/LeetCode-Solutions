class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def getNode(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addToHead(node)
            return node
        return None

    def removeNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def addToHead(self, node):
        node.prev = self.dummy
        node.next = self.dummy.next
        node.prev.next = node
        node.next.prev = node

    def get(self, key: int) -> int:
        node = self.getNode(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.getNode(key)
        if node:
            node.value = value
            return
        if len(self.cache) >= self.capacity:
            tail = self.dummy.prev
            self.removeNode(tail)
            del self.cache[tail.key]
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.addToHead(newNode)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
