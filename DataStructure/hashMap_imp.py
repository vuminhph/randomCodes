class Hashmap:
    maxSize = 100

    def __init__(self):
        self.storage = [None for _ in range(self.maxSize)]
        self.size = 0

    def hashStr(self, key):
        if isinstance(key, int):
            return key

        result = 5381
        for char in key:
            result = 33 * result + ord(char)
        return result % self.maxSize

    def set(self, key, val):
        hashInt = self.hashStr(key)
        self.storage[hashInt] = val
        return val

    def get(self, key):
        hashInt = self.hashStr(key)
        if self.storage[hashInt] is not None:
            return self.storage[hashInt]
        return None

map = Hashmap()
map.set('jess', '213-559-6840')