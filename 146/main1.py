class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}


    def get(self, key: int) -> int:
        res = self.cache.get(key, -1)
        if res != -1:
            self.cache.pop(key)
            self.cache[key] = res
        return res


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(list(self.cache.keys())[0])



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
